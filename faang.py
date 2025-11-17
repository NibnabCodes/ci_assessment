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

import os

import glob

# Collect data for all FAANG 
# stocks over past 5 days
df = yf.download(['META', 'AAPL', 'AMZN', 'NFLX', 'GOOG'], period='5d')  

# Create function 
def get_data():
    tickers = ["META", "AAPL", "AMZN", "NFLX", "GOOG"] # assign tickers
    data = yf.download( #
        tickers=tickers, #
        period="5d", #
        interval="1h", #
        auto_adjust=False #
    )

    return data

# get local date & time
local = dt.datetime.now().strftime("%Y%m%d-%H%M%S")

# Save data as csv
get_data().to_csv("./data/" +  # save to data folder 
                  local
                  + ".csv")

def plot_data():
    list_of_files = glob.glob('./data/*')  # get all files from data folder
    latest_file = max(list_of_files, key=os.path.getctime) # get latest file

    df2 = pd.read_csv(latest_file, header=[0,1], index_col=0)
    df2.index = pd.to_datetime(df2.index) # convert index to datetime to allow for date formatting

    faang = ['AAPL', 'AMZN', 'GOOG', 'META', 'NFLX'] # define tickers

    date_str = os.path.basename(latest_file).split("-")[0] # extract 1st 8 digits from filename to get date
    date = dt.datetime.strptime(date_str, "%Y%m%d").strftime("%Y-%m-%d") # format date for readability

    last_per_day = df2['Close'][faang].groupby(df2.index.date).last() # group by date and take last close price of each day
    last_5_days = last_per_day.tail(5) # select last 5 days 
    
    # plot data
    last_5_days.plot(figsize=(12,6), marker='o') # set figsize and markers for clarity

    # add titles & labels
    plt.title(f"{date}")
    plt.xticks(rotation=45) # rotate x axis for readability 
    plt.xlabel("Date")
    plt.ylabel("Close Price")
    plt.grid(True)
    plt.tight_layout()

    plots_folder = "./plots" # save to plots folder

    timestamp = dt.datetime.now().strftime("%Y%m%d-%H%M%S") # format filename to current date
    filename = os.path.join(plots_folder, f"{timestamp}.png") # join filename and filename/ create filename
    plt.savefig(filename, dpi=300)

    plt.show()

plot_data()
