#!/usr/bin/env python3

# imports
# Dates and time
import datetime as dt

# Yahoo Finance data
import yfinance as yf

# Data frames
import pandas as pd

# Plot
import matplotlib.pyplot as plt

# File system operations
import os

# File pattern matching
import glob


# Collect data for all FAANG stocks over the past 5 days
df = yf.download(
    tickers=["META", "AAPL", "AMZN", "NFLX", "GOOG"],
    period="5d"
)


# Create function
def get_data():
    """Download 5 days of hourly data for FAANG stocks."""
    
    tickers = ["META", "AAPL", "AMZN", "NFLX", "GOOG"]

    data = yf.download(
        tickers=tickers,
        period="5d",
        interval="1h",
        auto_adjust=False
    )

    return data

# Get local date & time
local = dt.datetime.now().strftime("%Y%m%d-%H%M%S")

# Save data as CSV
get_data().to_csv(
    "./data/"  # save to data folder
    + local
    + ".csv"
)


def plot_data():
    # Get all files from the data folder
    list_of_files = glob.glob("./data/*")
    # Get the latest file
    latest_file = max(list_of_files, key=os.path.getctime)

    # Read CSV with multi-index headers
    df2 = pd.read_csv(latest_file, header=[0, 1], index_col=0)
    # Convert index to datetime to allow for date formatting
    df2.index = pd.to_datetime(df2.index)

    # Define tickers
    faang = ["AAPL", "AMZN", "GOOG", "META", "NFLX"]

    # Extract date from filename and format for readability
    date_str = os.path.basename(latest_file).split("-")[0]
    date = dt.datetime.strptime(date_str, "%Y%m%d").strftime("%Y-%m-%d")

    # Group by date and take last close price of each day
    last_per_day = df2["Close"][faang].groupby(df2.index.date).last()
    # Select last 5 days
    last_5_days = last_per_day.tail(5)

    # Plot data
    last_5_days.plot(figsize=(12, 6), marker="o")  # Set figsize and markers for clarity

    # Add titles and labels
    plt.title(f"{date}")
    plt.xticks(rotation=45)  # Rotate x-axis for readability
    plt.xlabel("Date")
    plt.ylabel("Close Price")
    plt.legend(loc="upper right", bbox_to_anchor=(1, 0.9)) # Adjust position of ledgend
    plt.grid(True)
    plt.tight_layout()

    # Save plot
    filename = os.path.join("./plots", f"{local}.png")
    plt.savefig(filename, dpi=300)

    plt.show()


plot_data()
