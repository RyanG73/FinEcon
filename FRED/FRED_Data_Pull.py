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
import sys
from defs import ecdf
import sidetable
start_time = time.time()

# DEXUSEU = Exchange Rate
# LFWA64TTUSM647S = working age population

# Set the start date
start = date(1950,1,1)
"""
# Define the series codes
series = ['UNRATE', 'CIVPART']

# Import the data
econ_data = DataReader(series,'fred',start)

# Assign new column labels
econ_data.columns = ['Unemployment Rate','Participation Rate']
econ_data = econ_data.reset_index()
econ_data['decade'] = econ_data['DATE'].astype(str).str[2:3]
econ_data['decade'] = econ_data['decade'].astype(str)
econ_data['decade'] = econ_data['decade'] + "0s"
# Plot econ_data
_ = econ_data.plot(subplots=True,title='Labor Market')
plt.margins(.2)
# Show the plot
plt.show()
data = econ_data['Unemployment Rate']
x,y = ecdf(data)
_ = plt.plot(x, y, marker='.', linestyle='none')
_ = plt.xlabel('Unemployment Rate')
_ = plt.ylabel('CDF')
_ = plt.margins(0.2)
plt.show()

_ = plt.plot(econ_data['Unemployment Rate'],econ_data['Participation Rate'], marker='.', linestyle='none',)
_ = plt.xlabel('Participation Rate')
_ = plt.ylabel('Participation Rate')
_ = plt.margins(0.2)

plt.show()
print(np.corrcoef(econ_data['Unemployment Rate'],econ_data['Participation Rate']))

econ_data['decade'] = econ_data['']

_ = sns.scatterplot(x='DATE',y='Participation Rate',data=econ_data,hue='decade',size='Unemployment Rate',size_norm=(2,15))
_ = plt.xlabel('Date')
_ = plt.ylabel('Participation Rate')
_ = plt.margins(0.2)
plt.show()
"""
# Define the series codes
series = ['ATNHPIUS45780Q','ATNHPIUS10420Q','ATNHPIUS17460Q','ATNHPIUS18140Q','ATNHPIUS17140Q']
# Import the data
econ_data = DataReader(series,'fred',start)

# Assign new column labels
econ_data.columns = ['Toledo','Akron','Cleveland','Columbus','Cincinnati']
econ_data = econ_data.reset_index()
econ_data2 = econ_data.melt(id_vars=['DATE'])
#econ_data['decade'] = econ_data['DATE'].astype(str).str[2:3]
#econ_data['decade'] = econ_data['decade'].astype(str)
#econ_data['decade'] = econ_data['decade'] + "0s"
#econ_data['Working Population'] = econ_data['Working Population'] / 1000000
#econ_data['Population'] = econ_data['Population'] / 1000
_ = sns.lineplot(x='DATE',y='value',data=econ_data2,hue='variable')
_ = plt.xlabel('Date')
_ = plt.ylabel('Index')
plt.show()

print("--- %s minutes ---" % round((time.time() - start_time)/60,3))


def bootstrap_replicate_1d(data, func):
    bs_sample = np.random.choice(data, len(data))
    return func(bs_sample)

def draw_bs_reps(data, func, size=1):
    bs_replicates = np.empty(size)
    for i in range(size):
        bs_replicates[i] = bootstrap_replicate_1d(data,func)
    return bs_replicates


#draw_bs_reps(econ_data['Unemployment Rate'],np.mean,size=10000)

# Take 10,000 bootstrap replicates of the mean: bs_replicates
#bs_replicates = draw_bs_reps(econ_data['Unemployment Rate'],np.mean,size=10000)

# Compute and print SEM
#sem = np.std(econ_data['Unemployment Rate']) / np.sqrt(len(econ_data['Unemployment Rate']))
#print(sem)

# Compute and print standard deviation of bootstrap replicates
#bs_std = np.std(bs_replicates)
#print(bs_std)

# Make a histogram of the results
#_ = plt.hist(bs_replicates, bins=50)
#_ = plt.xlabel('Mean Unemployment')
#_ = plt.ylabel('PDF')

#econ_data2.stb.freq(['variable'],value='value')

# Show the plot
#plt.show()
#print(np.percentile(bs_replicates,[2.5,97.5]))

