import streamlit as st
import pandas as pd
from database import load_data
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import letter

# =========================
# PAGE CONFIG
# =========================

st.set_page_config(
    page_title="PDF Reports",
    page_icon="📄",
    layout="wide"
)

# =========================
# LOAD DATA
# =========================

df = load_data()

# =========================
# TITLE
# =========================

st.title("📄 Executive PDF Reports")

# =========================
# KPI CALCULATIONS
# =========================

total_sales = df["Sales"].sum()

total_profit = df["Profit"].sum()

total_orders = df["Order ID"].nunique()

top_category = df.groupby(
    "Category"
)["Sales"].sum().idxmax()

# =========================
# DISPLAY KPIs
# =========================

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
    total_orders
)

st.success(
    f"🏆 Top Category: {top_category}"
)

# =========================
# GENERATE PDF FUNCTION
# =========================

def generate_pdf():

    file_name = "business_report.pdf"

    doc = SimpleDocTemplate(
        file_name,
        pagesize=letter
    )

    styles = getSampleStyleSheet()

    elements = []

    title = Paragraph(
        "Smart Retail Analytics Report",
        styles['Title']
    )

    elements.append(title)

    elements.append(Spacer(1, 20))

    content = f'''
    <b>Total Sales:</b> ${total_sales:,.2f}<br/>
    <b>Total Profit:</b> ${total_profit:,.2f}<br/>
    <b>Total Orders:</b> {total_orders}<br/>
    <b>Top Category:</b> {top_category}<br/>
    '''

    paragraph = Paragraph(
        content,
        styles['BodyText']
    )

    elements.append(paragraph)

    doc.build(elements)

    return file_name

# =========================
# BUTTON
# =========================

if st.button("📥 Generate PDF Report"):

    pdf_file = generate_pdf()

    with open(pdf_file, "rb") as file:

        st.download_button(
            label="⬇️ Download PDF",
            data=file,
            file_name="business_report.pdf",
            mime="application/pdf"
        )

    st.success("✅ PDF Report Generated Successfully")