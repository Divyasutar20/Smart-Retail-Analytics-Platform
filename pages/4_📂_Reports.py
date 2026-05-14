import streamlit as st
import pandas as pd

# =========================
# PAGE CONFIG
# =========================

st.set_page_config(
    page_title="Reports",
    page_icon="📂",
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

st.title("📂 Business Reports")

# =========================
# DATA PREVIEW
# =========================

st.subheader("📊 Dataset Preview")

st.dataframe(df.head())

# =========================
# DOWNLOAD CSV
# =========================

csv = df.to_csv(index=False).encode("utf-8")

st.download_button(
    label="📥 Download Full Dataset",
    data=csv,
    file_name="business_report.csv",
    mime="text/csv"
)

# =========================
# KPI SUMMARY
# =========================

st.subheader("📈 KPI Summary")

total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()
orders = df["Order ID"].nunique()

col1, col2, col3 = st.columns(3)

col1.metric(
    "💰 Total Sales",
    f"${total_sales:,.0f}"
)

col2.metric(
    "📈 Total Profit",
    f"${total_profit:,.0f}"
)

col3.metric(
    "📦 Orders",
    orders
)

st.success(
    "✅ Report generated successfully."
)