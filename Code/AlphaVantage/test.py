# Author:           Sheldon Reddy
#
# Description:      This script tests the Alpha-Vantage functionality
#                    Extremely Basic at this point - tests Intraday plotting
#
# Vantage Alpa API key: 11T68YL4UZ067FQZ

from alpha_vantage.techindicators import TechIndicators
import matplotlib.pyplot as plt
from alpha_vantage.timeseries import TimeSeries
import numpy as np


ts = TimeSeries(key='YOUR_API_KEY', output_format='pandas')

data, meta_data = ts.get_intraday(symbol='GOOGL',interval='15min', outputsize='full')
data['4. close'].plot()
plt.title('Intraday Times Series for the GOOGL stock (1 min)')
plt.show()
