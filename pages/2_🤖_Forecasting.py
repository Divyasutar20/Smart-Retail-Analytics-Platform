import streamlit as st
import pandas as pd
import plotly.express as px
from sklearn.linear_model import LinearRegression
import numpy as np

# =========================
# PAGE CONFIG
# =========================

st.set_page_config(
    page_title="Sales Forecasting",
    page_icon="🤖",
    layout="wide"
)

# =========================
# LOAD DATA
# =========================

from database import load_data

df = load_data()

# =========================
# DATE PROCESSING
# =========================

df["Order Date"] = pd.to_datetime(df["Order Date"])

monthly_sales = df.groupby(
    df["Order Date"].dt.to_period("M")
)["Sales"].sum().reset_index()

monthly_sales["Order Date"] = monthly_sales[
    "Order Date"
].astype(str)

monthly_sales["Month_Num"] = np.arange(len(monthly_sales))

# =========================
# MODEL TRAINING
# =========================

X = monthly_sales[["Month_Num"]]
y = monthly_sales["Sales"]

model = LinearRegression()
model.fit(X, y)

# =========================
# FUTURE PREDICTION
# =========================

future_months = 6

future_x = np.arange(
    len(monthly_sales),
    len(monthly_sales) + future_months
).reshape(-1, 1)

future_predictions = model.predict(future_x)

future_df = pd.DataFrame({
    "Month_Num": future_x.flatten(),
    "Forecasted Sales": future_predictions
})

# =========================
# TITLE
# =========================

st.title("🤖 AI Sales Forecasting")

# =========================
# FORECAST METRICS
# =========================

predicted_growth = (
    (future_predictions[-1] - future_predictions[0])
    / future_predictions[0]
) * 100

st.metric(
    "📈 Predicted Growth",
    f"{predicted_growth:.2f}%"
)

# =========================
# FORECAST CHART
# =========================

fig = px.line(
    monthly_sales,
    x="Month_Num",
    y="Sales",
    title="Historical Sales Trend",
    markers=True
)

fig.add_scatter(
    x=future_df["Month_Num"],
    y=future_df["Forecasted Sales"],
    mode='lines+markers',
    name='Forecast'
)

st.plotly_chart(fig, width='stretch')

# =========================
# AI INSIGHTS
# =========================

st.markdown("## 🧠 Forecast Insights")

if predicted_growth > 0:
    st.success(
        f"✅ Sales are expected to grow by {predicted_growth:.2f}% in upcoming months."
    )
else:
    st.error(
        "⚠️ Sales may decline in future months."
    )

st.info(
    "📊 Forecast generated using Linear Regression model."
)