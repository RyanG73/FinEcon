import pandas as pd
import seaborn as sns
import numpy as np
import time
from pandas_datareader.data import DataReader
from datetime import date
import matplotlib.pyplot as plt
from Functions import *

start_time = time.time()

# Set the start date
start = date(1950,1,1)

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

_ = plt.plot(econ_data['Unemployment Rate'],econ_data['Participation Rate'], marker='.', linestyle='none')
_ = plt.xlabel('Participation Rate')
_ = plt.ylabel('Participation Rate')
_ = plt.margins(0.2)
plt.show()
print(np.corrcoef(econ_data['Unemployment Rate'],econ_data['Participation Rate']))

_ = sns.scatterplot(x='DATE',y='Participation Rate',data=econ_data,hue='decade',size='Unemployment Rate',size_norm=(2,15))
_ = plt.xlabel('Date')
_ = plt.ylabel('Participation Rate')
_ = plt.margins(0.2)
plt.show()

print("--- %s minutes ---" % round((time.time() - start_time)/60,3))


