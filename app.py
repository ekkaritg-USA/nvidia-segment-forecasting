
import streamlit as st
import pandas as pd
import plotly.graph_objs as go
import os

# Page configuration
st.set_page_config(
    page_title="NVIDIA Segment Forecasting",
    layout="wide",
    page_icon="📈"
)

st.title("📊 NVIDIA Segment-Level Revenue Forecasting (FY2024–FY2027)")

# File paths
data_dir = "data"
charts_dir = "charts"

# Segment mapping for display
segment_files = {
    "Gaming": "Gaming_Forecast_Prophet_Tuned.csv",
    "Data Center": "Data_Center_Forecast_Prophet_Tuned.csv",
    "Pro Viz": "Pro_Viz_Forecast_Prophet_Tuned.csv",
    "Automotive": "Automotive_Forecast_Prophet_Tuned.csv",
    "OEM & Other": "OEM_Other_Forecast_Prophet_Tuned.csv"
}

chart_files = {
    "Gaming": "Project_3_Figure_1_NVIDIA_Gaming_Revenue_Forecast.png",
    "Data Center": "Project_3_Figure_2_NVIDIA_Data_Center_Revenue_Forecast.png",
    "Pro Viz": "Project_3_Figure_3_NVIDIA_Pro_Viz_Revenue_Forecast.png",
    "Automotive": "Project_3_Figure_4_NVIDIA_Automotive_Revenue_Forecast.png",
    "OEM & Other": "Project_3_Figure_5_NVIDIA_OEM_Other_Revenue_Forecast.png"
}

# Sidebar segment selector
segment = st.sidebar.selectbox("Select Segment", list(segment_files.keys()))

# Load forecast CSV
forecast_path = os.path.join(data_dir, segment_files[segment])
forecast_df = pd.read_csv(forecast_path)
forecast_df["ds"] = pd.to_datetime(forecast_df["ds"])

# Plotly chart
fig = go.Figure()
fig.add_trace(go.Scatter(
    x=forecast_df["ds"], y=forecast_df["yhat"],
    mode='lines', name='Forecast',
    line=dict(color='orange')
))
fig.add_trace(go.Scatter(
    x=forecast_df["ds"], y=forecast_df["yhat_upper"],
    mode='lines', name='Upper Bound',
    line=dict(color='rgba(255,165,0,0.3)'), showlegend=False
))
fig.add_trace(go.Scatter(
    x=forecast_df["ds"], y=forecast_df["yhat_lower"],
    mode='lines', name='Lower Bound', fill='tonexty',
    line=dict(color='rgba(255,165,0,0.3)'), fillcolor='rgba(255,165,0,0.1)',
    showlegend=True
))

fig.update_layout(
    title=f"{segment} Revenue Forecast (Tuned Prophet)",
    xaxis_title="Quarter",
    yaxis_title="Revenue ($M)",
    margin=dict(l=20, r=20, t=40, b=20),
    template="plotly_white"
)

st.plotly_chart(fig, use_container_width=True)

# Display underlying forecast data
with st.expander("🔍 View Forecast Table"):
    st.dataframe(forecast_df.head(12))

# Show static chart image
image_path = os.path.join(charts_dir, chart_files[segment])
with st.expander("🖼 View Forecast Image"):
    st.image(image_path, use_column_width=True)

st.markdown("---")
st.markdown("Built by **Ekkarit** — Segment-Level Financial Forecasting, FY2014–FY2027")
