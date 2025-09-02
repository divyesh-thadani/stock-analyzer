# 📈 Stock Market Analysis & Prediction Engine

A web-based application built with Python and Streamlit that provides real-time stock market analysis, visualization, and price prediction. This tool allows users to analyze stocks from multiple exchanges, including US Markets (NASDAQ/NYSE) and Indian Markets (NSE/BSE).

*(Replace this line with a screenshot of your running application)*

## ✨ Features

* **Multi-Exchange Support:** Analyze stocks from US Markets, National Stock Exchange (NSE) of India, and Bombay Stock Exchange (BSE) of India.
* **Real-time Data:** Fetches up-to-date historical stock data using the `yfinance` library.
* **Technical Analysis:** Automatically calculates and plots key technical indicators, including 50-day and 200-day Simple Moving Averages (SMAs).
* **Price Prediction:** Utilizes a Linear Regression model to predict the closing price for the next trading day.
* **Interactive UI:** A clean, user-friendly interface built with Streamlit that allows for easy input of stock tickers.
* **Performance Visualization:** Displays charts for historical price action and a comparison of the model's predictions versus actual prices on test data.

## 🛠️ Technologies Used

* **Backend:** Python
* **Web Framework:** Streamlit
* **Data Manipulation:** Pandas, NumPy
* **Data Fetching:** yfinance
* **Machine Learning:** Scikit-learn
* **Plotting:** Matplotlib

## 🚀 Setup and Installation

Follow these steps to set up and run the project on your local machine.

### 1. Prerequisites

* Python 3.9 or higher
* `pip` (Python package installer)

### 2. Clone the Repository

```bash
git clone https://github.com/divyesh-thadani/stock-analyzer.git
cd stock-analyzer
```

### 3. Create a Virtual Environment

It is highly recommended to use a virtual environment to manage project dependencies.

**On macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**On Windows:**
```bash
python -m venv venv
.\venv\Scripts\activate
```

### 4. Install Dependencies

Install all the required libraries from the `requirements.txt` file.

```bash
pip install -r requirements.txt
```

## ▶️ How to Run the Application

Once the setup is complete, you can launch the Streamlit app with the following command:

```bash
streamlit run app.py
```

Your web browser will automatically open a new tab with the application running at `http://localhost:8501`.

## 📋 Requirements.txt

Create a `requirements.txt` file with the following dependencies:

```
streamlit>=1.28.0
pandas>=1.5.0
numpy>=1.24.0
yfinance>=0.2.18
scikit-learn>=1.3.0
matplotlib>=3.7.0
```

## 🔧 Usage

1. **Select Market**: Choose between US Markets or Indian Markets from the dropdown menu.
2. **Enter Stock Symbol**: Input the stock ticker symbol (e.g., AAPL for Apple, RELIANCE.NS for Reliance Industries).
3. **Analyze**: Click the analyze button to fetch data and generate predictions.
4. **View Results**: Review the technical analysis charts and price predictions.

## 📊 Supported Stock Exchanges

### US Markets
- **NASDAQ**: Use standard ticker symbols (e.g., AAPL, GOOGL, MSFT)
- **NYSE**: Use standard ticker symbols (e.g., JPM, JNJ, WMT)

### Indian Markets
- **NSE**: Add `.NS` suffix to ticker symbols (e.g., RELIANCE.NS, TCS.NS)
- **BSE**: Add `.BO` suffix to ticker symbols (e.g., RELIANCE.BO, TCS.BO)

## 🎯 Key Components

### Data Collection
- Utilizes `yfinance` library to fetch historical stock data
- Supports multiple timeframes and intervals
- Handles data cleaning and preprocessing

### Technical Analysis
- **Simple Moving Averages (SMA)**: 50-day and 200-day moving averages
- **Price Visualization**: Interactive charts showing price trends
- **Volume Analysis**: Trading volume patterns

### Machine Learning Prediction
- **Linear Regression Model**: Predicts next-day closing prices
- **Feature Engineering**: Uses historical price data and technical indicators
- **Model Evaluation**: Displays prediction accuracy metrics

## 🚨 Disclaimer

**Important:** This application is for educational and informational purposes only. The predictions and analysis provided should not be considered as financial advice. Always consult with qualified financial advisors before making investment decisions. Past performance does not guarantee future results.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🐛 Known Issues

- API rate limits may affect data fetching for multiple requests
- Prediction accuracy varies based on market volatility
- Some international markets may have limited data availability

## 🔮 Future Enhancements

- [ ] Add more technical indicators (RSI, MACD, Bollinger Bands)
- [ ] Implement advanced ML models (LSTM, Prophet)
- [ ] Add portfolio analysis features
- [ ] Include fundamental analysis metrics
- [ ] Support for cryptocurrency markets
- [ ] Real-time alerts and notifications
- [ ] Mobile-responsive design improvements

## 📞 Support

If you encounter any issues or have questions:
- Open an issue on GitHub
- Check the documentation
- Review the troubleshooting section

## 👨‍💻 Author

**Divyesh Thadani**
- GitHub: [@divyesh-thadani](https://github.com/divyesh-thadani)

## 🙏 Acknowledgments

- Thanks to the `yfinance` library for providing easy access to financial data
- Streamlit team for the excellent web app framework
- The open-source community for various Python libraries used in this project

---

⭐ If you found this project helpful, please consider giving it a star on GitHub!