import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
import plotly.express as px

# =========================
# PAGE CONFIG
# =========================

st.set_page_config(
    page_title="SQL Analytics",
    page_icon="📊",
    layout="wide"
)

# =========================
# DATABASE CONNECTION
# =========================

engine = create_engine(
    "mysql+pymysql://root:@localhost:3307/smart_retail_db"
)

# =========================
# TITLE
# =========================

st.title("📊 Advanced SQL Business Analytics")

# =========================
# TOP SELLING PRODUCTS
# =========================

query1 = """
SELECT 
    `Product Name`,
    SUM(Sales) AS Total_Sales
FROM sales_data
GROUP BY `Product Name`
ORDER BY Total_Sales DESC
LIMIT 10
"""

top_products = pd.read_sql(query1, engine)

st.subheader("🏆 Top Selling Products")

fig1 = px.bar(
    top_products,
    x="Total_Sales",
    y="Product Name",
    orientation='h',
    title="Top 10 Products by Sales"
)

st.plotly_chart(fig1, width='stretch')

# =========================
# REGION-WISE PROFIT
# =========================

query2 = """
SELECT 
    Region,
    SUM(Profit) AS Total_Profit
FROM sales_data
GROUP BY Region
ORDER BY Total_Profit DESC
"""

region_profit = pd.read_sql(query2, engine)

st.subheader("🌍 Region-wise Profit Analysis")

fig2 = px.pie(
    region_profit,
    names="Region",
    values="Total_Profit",
    title="Profit Distribution by Region"
)

st.plotly_chart(fig2, width='stretch')

# =========================
# CATEGORY ANALYSIS
# =========================

query3 = """
SELECT 
    Category,
    SUM(Sales) AS Total_Sales,
    SUM(Profit) AS Total_Profit
FROM sales_data
GROUP BY Category
"""

category_data = pd.read_sql(query3, engine)

st.subheader("📦 Category Performance")

fig3 = px.bar(
    category_data,
    x="Category",
    y="Total_Profit",
    color="Category",
    title="Profit by Category"
)

st.plotly_chart(fig3, width='stretch')

# =========================
# TOP CUSTOMERS
# =========================

query4 = """
SELECT 
    `Customer Name`,
    SUM(Sales) AS Total_Sales
FROM sales_data
GROUP BY `Customer Name`
ORDER BY Total_Sales DESC
LIMIT 10
"""

top_customers = pd.read_sql(query4, engine)

st.subheader("👥 Top Customers")

st.dataframe(top_customers)

# =========================
# AI INSIGHTS
# =========================

st.markdown("## 🤖 AI Insights")

best_region = region_profit.iloc[0]["Region"]

best_category = category_data.sort_values(
    by="Total_Profit",
    ascending=False
).iloc[0]["Category"]

st.success(
    f"✅ {best_region} region generated highest profit."
)

st.info(
    f"📈 {best_category} category is the most profitable."
)

st.warning(
    "⚠️ Focus marketing on top-performing products and regions."
)