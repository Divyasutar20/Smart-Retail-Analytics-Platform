import streamlit as st
import pandas as pd

# =========================
# PAGE CONFIG
# =========================

st.set_page_config(
    page_title="AI Insights",
    page_icon="📈",
    layout="wide"
)

# =========================
# LOAD DATA
# =========================

from database import load_data

df = load_data()

# =========================
# TITLE
# =========================

st.title("📈 AI Business Insights")

# =========================
# INSIGHTS
# =========================

top_category = df.groupby(
    "Category"
)["Sales"].sum().idxmax()

top_region = df.groupby(
    "Region"
)["Profit"].sum().idxmax()

lowest_category = df.groupby(
    "Category"
)["Profit"].sum().idxmin()

avg_discount = df["Discount"].mean()

# =========================
# DISPLAY INSIGHTS
# =========================

st.success(
    f"✅ Top performing category: {top_category}"
)

st.info(
    f"🌍 Most profitable region: {top_region}"
)

st.warning(
    f"⚠️ Lowest profit category: {lowest_category}"
)

st.error(
    f"📉 Average discount offered: {avg_discount:.2f}"
)

# =========================
# SMART RECOMMENDATIONS
# =========================

st.markdown("## 💡 Smart Recommendations")

st.write("""
- Focus marketing on top-performing categories.
- Reduce discounts in low-profit segments.
- Expand profitable regions strategically.
- Improve inventory planning using forecasting insights.
""")