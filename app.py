import streamlit as st
from login import login

# =========================
# SESSION STATE
# =========================

if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

# =========================
# LOGIN CHECK
# =========================

if not st.session_state["logged_in"]:

    login()

    st.stop()


import streamlit as st
import pandas as pd
import plotly.express as px

# =========================
# PAGE CONFIG
# =========================

st.set_page_config(
    page_title="Smart Retail Analytics Platform",
    page_icon="📊",
    layout="wide"
)

# =========================
# CUSTOM CSS
# =========================

st.markdown("""
<style>

.stApp {
    background: linear-gradient(to right, #141E30, #243B55);
    color: white;
}

h1, h2, h3 {
    color: #00E5FF;
}

[data-testid="metric-container"] {
    background-color: rgba(255,255,255,0.1);
    border-radius: 15px;
    padding: 15px;
    border: 1px solid rgba(255,255,255,0.2);
}

</style>
""", unsafe_allow_html=True)

# =========================
# HOME PAGE
# =========================

st.markdown("""
# 🧠 Smart Retail Analytics Platform
""")

st.markdown("""
### 🚀 AI-Powered Business Intelligence Dashboard

This platform provides:

✅ Sales Analytics  
✅ Business Insights  
✅ AI Forecasting  
✅ Interactive Visualizations  
✅ Smart Recommendations  
✅ Report Generation  

Use the sidebar to navigate between pages.
""")

st.image(
    "https://images.unsplash.com/photo-1551288049-bebda4e38f71",
    width='stretch'
)

st.success("✅ Platform Loaded Successfully")

st.markdown("---")

# =========================
# LOAD DATA
# =========================

from database import load_data

df = load_data()

# =========================
# FILTERS
# =========================

st.sidebar.title("📌 Filters")
if st.sidebar.button("🚪 Logout"):

    st.session_state["logged_in"] = False

    st.rerun()

region = st.sidebar.multiselect(
    "Select Region",
    options=df["Region"].unique(),
    default=df["Region"].unique()
)

category = st.sidebar.multiselect(
    "Select Category",
    options=df["Category"].unique(),
    default=df["Category"].unique()
)

filtered_df = df[
    (df["Region"].isin(region)) &
    (df["Category"].isin(category))
]

# =========================
# KPI SECTION
# =========================

total_sales = filtered_df["Sales"].sum()
total_profit = filtered_df["Profit"].sum()
total_orders = filtered_df["Order ID"].nunique()
avg_sales = filtered_df["Sales"].mean()

col1, col2, col3, col4 = st.columns(4)

col1.metric("💰 Total Sales", f"${total_sales:,.0f}")
col2.metric("📈 Total Profit", f"${total_profit:,.0f}")
col3.metric("📦 Orders", total_orders)
col4.metric("🛒 Avg Sales", f"${avg_sales:.2f}")

st.markdown("---")

# =========================
# SALES BY CATEGORY
# =========================

sales_category = filtered_df.groupby(
    "Category"
)["Sales"].sum().reset_index()

fig1 = px.bar(
    sales_category,
    x="Category",
    y="Sales",
    title="Sales by Category",
    text_auto=True
)

st.plotly_chart(fig1, width='stretch')

# =========================
# SALES BY REGION
# =========================

sales_region = filtered_df.groupby(
    "Region"
)["Sales"].sum().reset_index()

fig2 = px.pie(
    sales_region,
    names="Region",
    values="Sales",
    title="Region-wise Sales Distribution"
)

st.plotly_chart(fig2, width='stretch')

# =========================
# MONTHLY SALES TREND
# =========================

filtered_df["Order Date"] = pd.to_datetime(
    filtered_df["Order Date"]
)

filtered_df["Month"] = filtered_df[
    "Order Date"
].dt.to_period("M").astype(str)

monthly_sales = filtered_df.groupby(
    "Month"
)["Sales"].sum().reset_index()

fig3 = px.line(
    monthly_sales,
    x="Month",
    y="Sales",
    title="Monthly Sales Trend",
    markers=True
)

st.plotly_chart(fig3, width='stretch')

# =========================
# AI BUSINESS INSIGHTS
# =========================

st.markdown("## 🤖 AI Business Insights")

top_category = sales_category.sort_values(
    by="Sales",
    ascending=False
).iloc[0]["Category"]

top_region = sales_region.sort_values(
    by="Sales",
    ascending=False
).iloc[0]["Region"]

insight1 = (
    f"✅ {top_category} category generated the highest sales."
)

insight2 = (
    f"🌍 {top_region} region contributed the most revenue."
)

profit_margin = (
    total_profit / total_sales
) * 100

insight3 = (
    f"📈 Current profit margin is {profit_margin:.2f}%."
)

st.success(insight1)
st.info(insight2)
st.warning(insight3)

# =========================
# SMART RECOMMENDATIONS
# =========================

st.markdown("## 💡 Smart Recommendations")

if profit_margin < 10:
    st.error(
        "⚠️ Profit margin is low. Focus on high-performing products and reduce discounts."
    )
else:
    st.success(
        "✅ Business performance is healthy. Consider expanding top-selling categories."
    )

# =========================
# DOWNLOAD REPORT
# =========================

st.markdown("## 📂 Download Report")

csv = filtered_df.to_csv(
    index=False
).encode("utf-8")

st.download_button(
    label="📥 Download Filtered Report",
    data=csv,
    file_name="retail_report.csv",
    mime="text/csv"
)

# =========================
# FOOTER
# =========================

st.markdown("---")

st.markdown(
    "<center>🚀 Developed by Divya Jitendra Sutar</center>",
    unsafe_allow_html=True
)