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
start_time = time.time()
start = date(2019,1,1)
end = date(2019,12,31)
ticker = 'HBAN'
data_source = 'google'
stock_data = DataReader(ticker,data_source,start,end)


sp = "/Users/ryangerda/PycharmProjects/Finance/SP500_20200521.xlsx"
sp = pd.read_excel(sp)
sp['Symbol'] = sp['Symbol'].str.lower()
stocks = sp['Symbol'].tolist()
stocks = list(map(lambda st: str.replace(st, ".", "-"), stocks))
stocks2 = ['msft', 'aapl']

n = 1
df = pd.DataFrame()
for i in stocks:
    sym = yq.Ticker(str(i))
    try:
        infor = sym.key_stats
        for d in infor.values():
            shares = d['sharesOutstanding']
        data = sym.history(period="max")
        data['Symbol'] = str(i)
        data['Shares'] = shares
        data['Market Capitalization'] = data['Shares'] * data['close']
        data = data.reset_index()
        data = pd.merge(data,sp[['Symbol','Sector']],how='left',on='Symbol')
        data = data.rename(columns={'index': 'Date'})
    except:
        continue
    print(str(i) + " " + str(n))
    df = df.append(data, ignore_index=True)
    n = n+1

#writer = pd.ExcelWriter('data.xlsx', engine='xlsxwriter')
#df.to_excel(writer, sheet_name='Data', index=False)
#writer.save()


narrow = df[['Date','Market Capitalization','Sector']]
group = narrow.groupby(['Sector','Date']).sum()
group['pct'] = group['Market Capitalization'] / group.groupby(['Date'])['Market Capitalization'].agg('sum')
group = group.reset_index(drop=False)
group = group[group['Date'] <= '5/21/2020']
sns.palplot(sns.color_palette("muted"))
ax = sns.lineplot(x="Date", y="pct", hue="Sector",data=group)

#narrow2 = df[['Date','Market Capitalization','Sector','Symbol']]
##n2 = narrow2[narrow2['Sector'] == 'Consumer Staples']
#n3 = n2[n2['Market Capitalization'] > 100000000000]
#sns.lineplot(x="Date", y="Market Capitalization", hue="Symbol",data=n3)

print("--- %s minutes ---" % round((time.time() - start_time)/60,3))