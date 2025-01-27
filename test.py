import time
import shutil
import termplotlib as tpl
from tradingview_ta import TA_Handler, Interval

def fetch_price(symbol, exchange):
    """Fetch the latest price of a symbol from TradingView."""
    try:
        analysis = TA_Handler(
            symbol=symbol,
            screener="crypto",
            exchange=exchange,
            interval=Interval.INTERVAL_1_MINUTE
        )
        price = analysis.get_analysis().indicators["close"]
        return price
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


def clear_console():
    print("\033[H\033[J", end="")

def check_gnuplot():
    return shutil.which("gnuplot") is not None

# Example usage
symbol = "1000PEPEUSDT.P"  # Replace with your trading pair
exchange = "BYBIT"  # Replace with the exchange name
prices = []  # List to store prices
time_intervals = 10

if not check_gnuplot():
    print("Gnuplot is not installed or not found in PATH. Please install Gnuplot to use this script.")
else:
    while True:
        price = fetch_price(symbol, exchange)
        if price is not None:
            clear_console()
            # print(price)
            prices.append(price)  # Add the price to the list
            if len(prices) > time_intervals:  # Keep only the last N prices
                prices.pop(0)

            # Plot the graph
            fig = tpl.figure()
            fig.plot(range(len(prices)), prices, label="Price (USDT)", width=50, height=15)
            fig.show()
        
        time.sleep(1)  # Add a delay to avoid excessive CPU usagepy