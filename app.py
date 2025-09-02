import streamlit as st
import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

st.set_page_config(page_title="Stock Market Analyzer", layout="wide")

st.title('📈 Stock Market Analysis & Prediction Engine')
st.write("Select an exchange and enter a stock ticker to get historical data, technical indicators, and a price prediction.")

# --- 1. User Input for Ticker and Exchange ---
st.sidebar.header('User Input')
exchange = st.sidebar.selectbox('Select Exchange', ('US Markets', 'NSE (India)', 'BSE (India)'))
default_ticker = 'AAPL' if exchange == 'US Markets' else 'RELIANCE'
ticker_symbol = st.sidebar.text_input('Enter Stock Ticker', default_ticker).upper()

# --- Caching the data loading function ---
@st.cache_data
def load_data(ticker, start, end):
    try:
        data = yf.download(ticker, start=start, end=end)
        if data.empty:
            return None
        return data
    except Exception as e:
        return None

if st.sidebar.button('Analyze Stock'):
    # --- Determine Ticker Suffix and Currency ---
    ticker_to_fetch = ticker_symbol
    currency_symbol = '$'
    currency_name = 'USD'

    if exchange == 'NSE (India)':
        if not ticker_symbol.endswith('.NS'):
            ticker_to_fetch = f"{ticker_symbol}.NS"
        currency_symbol = '₹'
        currency_name = 'INR'
    elif exchange == 'BSE (India)':
        if not ticker_symbol.endswith('.BO'):
            ticker_to_fetch = f"{ticker_symbol}.BO"
        currency_symbol = '₹'
        currency_name = 'INR'

    with st.spinner(f'Fetching and analyzing data for {ticker_to_fetch}...'):
        # --- 2. Fetch Data ---
        start_date = '2020-01-01'
        end_date = pd.to_datetime('today').strftime('%Y-%m-%d')
        stock_data = load_data(ticker_to_fetch, start_date, end_date)

        if stock_data is None:
            st.error(f"Could not fetch data for '{ticker_to_fetch}'. Please check the ticker symbol and selected exchange.")
        else:
            st.success(f"Data for {ticker_to_fetch} loaded successfully!")
            
            # --- Display Raw Data ---
            st.subheader('Recent Stock Data')
            st.dataframe(stock_data.tail())

            # --- 3. Calculate SMAs ---
            stock_data['SMA_50'] = stock_data['Close'].rolling(window=50).mean()
            stock_data['SMA_200'] = stock_data['Close'].rolling(window=200).mean()

            # --- 4. Visualize Data and SMAs ---
            st.subheader('Stock Price History with Moving Averages')
            fig, ax = plt.subplots(figsize=(14, 7))
            ax.plot(stock_data['Close'], label='Closing Price', alpha=0.6)
            ax.plot(stock_data['SMA_50'], label='50-Day SMA', linestyle='--')
            ax.plot(stock_data['SMA_200'], label='200-Day SMA', linestyle='--')
            ax.set_title(f'{ticker_to_fetch} Price History')
            ax.set_xlabel('Date')
            ax.set_ylabel(f'Price ({currency_name})')
            ax.legend()
            ax.grid(True)
            st.pyplot(fig)

            # --- 5. Prepare Data for ML ---
            stock_data['Next_Close'] = stock_data['Close'].shift(-1)
            final_data = stock_data.dropna()
            
            features = ['Close', 'SMA_50', 'SMA_200']
            X = final_data[features]
            y = final_data['Next_Close']

            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
            
            # --- 6. Train Model ---
            model = LinearRegression()
            model.fit(X_train, y_train)

            # --- 7. Make a Prediction for the Next Day ---
            last_row = stock_data[features].tail(1)
            next_day_prediction = model.predict(last_row)
            
            st.subheader('Prediction for the Next Trading Day')
            st.metric(label=f"Predicted Closing Price for {ticker_symbol}", value=f"{currency_symbol}{next_day_prediction[0]:.2f}")

            # --- 8. Evaluate and Visualize Model Performance ---
            st.subheader('Model Performance on Historical Data')
            predictions = model.predict(X_test)
            mse = mean_squared_error(y_test, predictions)
            st.write(f"**Mean Squared Error (MSE):** {mse:.2f}")
            st.write("This metric shows the average squared difference between the actual and predicted prices on the test data. Lower is better.")

            # --- Plotting predictions vs actual ---
            y_test_sorted = y_test.sort_index()
            test_df = pd.DataFrame({
                'Actual': y_test_sorted,
                'Predicted': model.predict(X.loc[y_test_sorted.index])
            })
            
            fig2, ax2 = plt.subplots(figsize=(14, 7))
            ax2.plot(test_df['Actual'], label='Actual Prices', color='blue', alpha=0.7)
            ax2.plot(test_df['Predicted'], label='Predicted Prices', color='red', linestyle='--')
            ax2.set_title('Model Predictions vs. Actual Prices (on Test Data)')
            ax2.set_xlabel('Date')
            ax2.set_ylabel(f'Price ({currency_name})')
            ax2.legend()
            ax2.grid(True)
            st.pyplot(fig2)


