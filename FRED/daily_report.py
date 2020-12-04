import pandas as pd
import seaborn as sns
import numpy as np
import time
from pandas_datareader.data import DataReader
from datetime import date
import matplotlib.pyplot as plt
from Functions import *

# ______________________________________________________ START TIME
start_time = time.time()

# ______________________________________________________ FRED START
start = date(2018,1,1)

# Define the series codes
# DEXUSEU = U.S. / Euro Foreign Exchange Rate
# UNRATE = USA Unemployment Rate
# A191RL1Q225SBEA = Real GDP
# NA000334Q = Gross Domestic Product
# Initial Claims = Jobless claims
# MORTGAGE30US = 30-Year Fixed Rate Mortgage Average in the United States
# ATNHPIUS18140Q = All-Transactions House Price Index for Columbus, OH (MSA)
# CEXRSA = S&P/Case-Shiller OH-Cleveland Home Price Index
# DTWEXBGS = Trade Weighted U.S. Dollar Index: Broad, Goods and Services
# CBBTCUSD = Coinbase Bitcoin
# APU0000708111 = eggs
# GASREGCOVW = US Regular Conventional Gas Price
# FEDFUNDS = Effective Federal Funds Rate
# CSUSHPINSA = S&P/Case-Shiller U.S. National Home Price Index
# T10YIE = 10-Year Breakeven Inflation Rate
# NASDAQCOM = NASDAQ
# DJIA = Dow Jones Industrial Average
# SAVINGS = Total Savings Deposits at all Depository Institutions
# SP500 = S&P 500
# CLVMNACSCAB1GQUK = Real Gross Domestic Product for United Kingdom
# CLVMNACSCAB1GQDE = Real Gross Domestic Product for Germany

series = ['DEXUSEU','UNRATE']

# ______________________________________________________ CONNECT TO FRED
econ_data = DataReader(series,'fred',start)

# ______________________________________________________ CLEAN DATA
econ_data.columns = ['U.S. / Euro Foreign Exchange Rate','USA Unemployment Rate']
econ_data = econ_data.reset_index()
econ_data['decade'] = econ_data['DATE'].astype(str).str[2:3]
econ_data['decade'] = econ_data['decade'].astype(str)
econ_data['decade'] = econ_data['decade'] + "0s"

#
fig, ax = plt.subplots(figsize=(15, 5))
sns.lineplot(x='DATE',y="U.S. / Euro Foreign Exchange Rate",data=econ_data,hue=econ_data.decade.tolist(),ax=ax)
#plt.xlabel('Date')
#plt.ylabel('U.S. / Euro Foreign Exchange Rate')
#plt.margins(0.2)
plt.show()