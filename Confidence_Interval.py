# -*- coding: utf-8 -*-
"""Confidence_Interval"""


from scipy import stats
import pandas as pd
import numpy as np

glaxo_df=pd.read_csv('glaxo.csv')
glaxo_df
glaxo_df.columns

glaxo_df_ci = stats.norm.interval(0.95,
loc = glaxo_df.high.mean(),
scale = glaxo_df.high.std())
print( 'Gain at 95% confidence interval is:', np.round(glaxo_df_ci, 4))

beml_df=pd.read_csv('beml_df.csv')

beml_df_ci = stats. norm.interval(0.95,
loc=beml_df.gain.mean(),
scale=beml_df.gain.std())

from scipy import stats
stats.norm.ppf(.975)

stats.norm.interval(0.95,0,1)

