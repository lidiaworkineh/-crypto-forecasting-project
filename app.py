import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Crypto Forecasting Dashboard")

coin = st.selectbox("Select Cryptocurrency", ['BTC', 'ETH', 'LTC', 'BNB'])
data_path = f"datasets/{coin}_forecast_results.csv"

@st.cache_data
def load_data(path):
    return pd.read_csv(path)

df = load_data(data_path)

st.subheader("Actual vs Predicted Prices")
fig = px.line(df, x='Date', y=['Actual', 'Predicted'], title=f"{coin} Forecast")
st.plotly_chart(fig)

st.subheader("Model Performance Metrics")
st.write(df[['Model', 'RMSE', 'MAE', 'MAPE']].drop_duplicates())