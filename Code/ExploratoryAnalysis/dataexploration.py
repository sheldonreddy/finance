#   Author:             Sheldon Reddy
#   Date:               20180703
#
#   Description:        Exploratory Analysis of S&P500 stocks
#
#   Operations:         1. Basic
#                               a. Read in CSV data
#                               b. Clean data using NaNs
#                               c. Print operations
#                               d. Perform basic plots
#                                                           i. high vs date
#                                                           ii. volume vs date
#

# Imports
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import datetime as dt
import matplotlib.dates as mdates
import seaborn as sns

# a. REAN IN CSV DATA
# b. CLEAN DATA
# Replace NULL Data with NaN
data = pd.read_csv("NFLX_data.csv",  na_values=['no info', '.'])

# c. PRINT OPERATIONS

# Print the data columns
print("\nData Columns: \n", data.columns, "\n")

# Print the first 5 rows
print("\n Header: \n", data.head());

# Print the data - uncomment when required
# print("Data: \n", data)

# Print stock data info
print("Stock info: \n")
print(data.info())

# Print stock data types
print("\nData Types:")
print("Date: ", data['date'].dtypes)
print("Open: ", data['open'].dtypes)
print("High: ", data['high'].dtypes)
print("Low: ", data['low'].dtypes)
print("Close: ", data['close'].dtypes)
print("Volume: ", data['volume'].dtypes)
print("Name: ", data['Name'].dtypes)

# d. PLOT DATA USING matplotlib

# i. Plot High VS. Date

# Convert date to a readable form
x = [dt.datetime.strptime(d,'%Y-%m-%d').date() for d in data['date']]
y = data['high']

# Start and EndDates (#YYYY-MM-DD)
# startdate = ('2013-01-01')
# enddate = ('2014-01-01')

#  Axis config
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m/%d/%Y'))
plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=60))               # 60 Day intervals
plt.gca().yaxis.set_major_locator(ticker.MultipleLocator(100))                  # Y axis tick spacing 100

# Plot
plt.plot(x, y, color="red")
plt.grid(True)
plt.ylim(0)
# plt.xlim(startdate, enddate) # Uncomment for viewing data within a set timeframe only
plt.xticks(rotation=90, fontsize=10)
plt.title('NFLX')
plt.ylabel('Stock Price For ' + 'high')
plt.xlabel('Date')
plt.show()

# ii. Plot Volume VS. Date

# Convert date to a readable form
x = [dt.datetime.strptime(d,'%Y-%m-%d').date() for d in data['date']]
y = data['volume']

# Axis Config
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m/%d/%Y'))
plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=60))

# Plot
plt.plot(x, y, color="orange")
plt.grid(True)
plt.xticks(rotation=90, fontsize=10)
plt.ylabel('NFLX Volume')
plt.xlabel('Date')
plt.show()

