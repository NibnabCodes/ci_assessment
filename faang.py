# Imports

# Dates and time
import datetime as dt 

# Yahoo Finance data
import yfinance as yf

# Data frames
#import pandas as pd 

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

