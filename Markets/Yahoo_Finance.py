import pandas as pd
import seaborn as sns
import numpy as np
import datetime
import time
import cv2
import pytesseract
import re
import yfinance as yf
import yahooquery as yq
from pandas_datareader.data import DataReader
from datetime import date
import matplotlib.pyplot as plt
start_time = time.time()

start = date(2016,5,15)
end = date.today()
ticker = 'HBAN'
data_source = 'yahoo'
stock_data = DataReader(ticker,data_source,start,end)


sns.lineplot(x=stock_data.index, y="Close",data=stock_data)
#sns.barplot(x=stock_data.index, y="Volume",data=stock_data)
plt.show()

#narrow2 = df[['Date','Market Capitalization','Sector','Symbol']]
##n2 = narrow2[narrow2['Sector'] == 'Consumer Staples']
#n3 = n2[n2['Market Capitalization'] > 100000000000]
#sns.lineplot(x="Date", y="Market Capitalization", hue="Symbol",data=n3)

print("--- %s minutes ---" % round((time.time() - start_time)/60,3))