# Crypto Market Data Analysis, Visualization, and Predictive Modeling

## Project Description

This project involves comprehensive analysis and forecasting of four major cryptocurrencies: Bitcoin (BTC), Ethereum (ETH), Litecoin (LTC), and Binance Coin (BNB). It covers data collection from public APIs, data cleaning, exploratory data analysis (EDA), time series forecasting using ARIMA, Prophet, and LSTM models, and the development of an interactive dashboard for visualization and model comparison.

The goal is to provide insights into cryptocurrency price dynamics and demonstrate effective predictive modeling techniques with an accessible user interface.

---

## Features

- Data Collection: Historical price and volume data over multiple time ranges and intervals.
- Data Cleaning: Handling missing values and outliers for reliable analysis.
- Exploratory Data Analysis: Statistical summaries, trend visualization, and correlation analysis.
- Predictive Modeling: Time series forecasting with ARIMA, Prophet, and LSTM, including model evaluation.
- Interactive Dashboard: User-friendly interface built with Streamlit for exploring data and forecasts.

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/lidiaworkineh/crypto-forecasting-project.git
cd crypto-forecasting-project
 2. Create and activate a virtual environment (optional but recommended):

python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

 3. Install dependencies:

pip install -r requirements.txt

Usage

Running the Dashboard

To launch the interactive dashboard, run:

streamlit run app.py

This will open a local web server where you can interact with historical data, forecasts, and model comparisons.

Project Structure

├── datasets/           # Cleaned and transformed CSV files
├── models/             # Trained model files
├── src/                # Source code scripts and modules
├── app.py              # Streamlit dashboard application
├── requirements.txt    # Project dependencies
├── README.md           # Project documentation

Dependencies

Key Python libraries used in this project:
 • pandas
 • numpy
 • matplotlib
 • seaborn
 • statsmodels
 • fbprophet (or prophet)
 • tensorflow / keras
 • streamlit
 • scikit-learn
 • plotly

Please refer to requirements.txt for the complete list.

Acknowledgements
 • Data sourced from Yahoo Finance and CoinGecko APIs.
 • Forecasting methodologies inspired by Forecasting: Principles and Practice (Hyndman & Athanasopoulos).
 • Prophet model developed by Facebook Research.
 • LSTM implementation based on standard deep learning practices.

Contributors
 • lidiya workineh
 
