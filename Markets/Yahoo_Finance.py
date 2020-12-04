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

start = date(2020,1,1)
end = date.today()
ticker = 'PENN'
data_source = 'yahoo'
penn = DataReader(ticker,data_source,start,end)
penn = penn.reset_index()
penn['Symbol'] = 'PENN'

ticker = 'MGM'
data_source = 'yahoo'
mgm = DataReader(ticker,data_source,start,end)
mgm = mgm.reset_index()
mgm['Symbol'] = 'MGM'

ticker = 'WYNN'
data_source = 'yahoo'
wynn = DataReader(ticker,data_source,start,end)
wynn = wynn.reset_index()
wynn['Symbol'] = 'WYNN'

combined = penn.append(mgm).append(wynn)


sns.lineplot(x="Date", y="Volume",data=combined,hue="Symbol"); plt.show()
#sns.barplot(x=stock_data.index, y="Volume",data=stock_data)
plt.show()

#narrow2 = df[['Date','Market Capitalization','Sector','Symbol']]
##n2 = narrow2[narrow2['Sector'] == 'Consumer Staples']
#n3 = n2[n2['Market Capitalization'] > 100000000000]
#sns.lineplot(x="Date", y="Market Capitalization", hue="Symbol",data=n3)

print("--- %s minutes ---" % round((time.time() - start_time)/60,3))