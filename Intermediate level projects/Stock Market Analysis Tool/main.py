
## Stock Market Analysis Tool
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

class StockMarketAnalysis:
    def __init__(self, ticker):
        # Initialize with the stock ticker symbol
        self.ticker = ticker
        # Fetch historical data for the given ticker
        self.data = self.fetch_data()

    def fetch_data(self):
        """
        Fetch historical market data for the given ticker.
        """
        stock_data = yf.download(self.ticker, start="2020-01-01", end="2023-01-01")
        return stock_data

    def calculate_moving_average(self, window):
        """
        Calculate the moving average for the stock data.
        """
        self.data[f'{window}d_MA'] = self.data['Close'].rolling(window=window).mean()

    def plot_data(self):
        """
        Plot the historical stock data along with moving averages.
        """
        plt.figure(figsize=(14, 7))
        plt.plot(self.data['Close'], label='Close Price')
        
        # Plot moving averages if they exist
        ma_columns = [col for col in self.data.columns if 'MA' in col]
        for ma in ma_columns:
            plt.plot(self.data[ma], label=ma)

        plt.title(f"{self.ticker} Stock Price and Moving Averages")
        plt.xlabel("Date")
        plt.ylabel("Price")
        plt.legend()
        plt.grid()
        plt.show()

    def add_technical_indicator(self):
        """
        Add a simple technical indicator (e.g., Relative Strength Index - RSI).
        """
        delta = self.data['Close'].diff(1)
        gain = delta.where(delta > 0, 0)
        loss = -delta.where(delta < 0, 0)

        avg_gain = gain.rolling(window=14).mean()
        avg_loss = loss.rolling(window=14).mean()

        rs = avg_gain / avg_loss
        self.data['RSI'] = 100 - (100 / (1 + rs))

    def plot_rsi(self):
        """
        Plot the RSI (Relative Strength Index).
        """
        plt.figure(figsize=(14, 7))
        plt.plot(self.data['RSI'], label='RSI', color='purple')
        plt.axhline(70, linestyle='--', alpha=0.5, color='red')
        plt.axhline(30, linestyle='--', alpha=0.5, color='green')
        plt.title(f"{self.ticker} Relative Strength Index (RSI)")
        plt.xlabel("Date")
        plt.ylabel("RSI")
        plt.legend()
        plt.grid()
        plt.show()

# Create an instance of the StockMarketAnalysis class
ticker = input("Enter the stock ticker symbol: ").upper()
analysis = StockMarketAnalysis(ticker)

# Calculate moving averages with different windows
analysis.calculate_moving_average(20)
analysis.calculate_moving_average(50)
analysis.calculate_moving_average(200)

# Add and plot the RSI
analysis.add_technical_indicator()
analysis.plot_data()
analysis.plot_rsi()
