# -*- coding: utf-8 -*-
"""Normal Disribution
"""

import pandas as pd
import numpy as np

from scipy import stats

beml_df = pd.read_csv("BEML.csv")
beml_df[0:5]
beml_df.columns

glaxo_df = pd.read_csv("GLAXO.csv")
glaxo_df[0:5]

beml_df = beml_df[['Date', 'Close']]
glaxo_df = glaxo_df[['Date', 'Close']]

beml_df

'''The DataFrames have a date column, so we can
create a DatetimeIndex index from this column Date. It will ensure that the rows are sorted by time in
ascending order.'''
glaxo_df = glaxo_df.set_index(pd.DatetimeIndex(glaxo_df['Date']))
beml_df = beml_df.set_index(pd.DatetimeIndex(beml_df['Date']))

glaxo_df

# Commented out IPython magic to ensure Python compatibility.
import matplotlib.pyplot as plt
import seaborn as sn
# %matplotlib inline
plt.plot(glaxo_df.Close);
plt.xlabel('Time');
plt.ylabel('Close Price');

plt.plot(beml_df.Close);
plt.xlabel('Time');
plt.ylabel('Close');

glaxo_df['gain'] = glaxo_df.Close.pct_change(periods = 1)
beml_df['gain'] = beml_df.Close.pct_change(periods = 1)

beml_df

#drop first row since it is NaN
glaxo_df = glaxo_df.dropna()
beml_df = beml_df.dropna()

#Plot the gains
plt.figure(figsize = (8, 6));
plt.plot(glaxo_df.index, glaxo_df.gain);
plt.xlabel('Time');
plt.ylabel('gain');

sn.distplot(glaxo_df.gain, label = 'Glaxo');
plt.xlabel('gain');
plt.ylabel('Density');
plt.legend();

sn.distplot(beml_df.gain, label = 'BEML');
plt.xlabel('gain');
plt.ylabel('Density');
plt.legend();

print('Mean:', round(glaxo_df.gain.mean(), 4))
print('Standard Deviation: ', round(glaxo_df.gain.std(), 4))

print('Mean: ', round(beml_df.gain.mean(), 4))
print('Standard Deviation: ', round(beml_df.gain.std(), 4))

from scipy import stats
#Probability of making 2% loss or higher in Glaxo
stats.norm.cdf( -0.02,
loc=glaxo_df.gain.mean(),
scale=glaxo_df.gain.std())

#Probability of making 2% gain or higher in Glaxo
1 - stats.norm.cdf(0.02,
loc=glaxo_df.gain.mean(),
scale=glaxo_df.gain.std())

stats.norm.interval(0.95,loc=glaxo_df.gain.mean(),scale=glaxo_df.gain.std())

"""### Inclass Exercise

### Compute 2% loss or gain for BEML
"""

#Probability of making 2% loss or higher in BEML
from scipy import stats
stats.norm.cdf(-0.02,loc=beml_df.gain.mean(),scale=beml_df.gain.std())

stats.norm.interval(0.95,loc=beml_df.gain.mean(),scale=beml_df.gain.std())

1-stats.norm.cdf(0.02,loc=beml_df.gain.mean(),scale=beml_df.gain.std())

from scipy import stats
stats.norm.cdf(-0.05,loc=1990,scale=2500)
stats.norm.ppf(0.975,139)
stats.t.ppf(0.975,139)

1-stats.norm.cdf(0.05,loc=1990,scale=2500)

import math
1990+1.64*2500/math.sqrt(140)
1990+1.98*2833/math.sqrt(140)
1990-1.98*2833/math.sqrt(140)

1990-1.64*2500/math.sqrt(140)

1990+1.96*2500/math.sqrt(140)

