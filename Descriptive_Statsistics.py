# -*- coding: utf-8 -*-
"""flightsexample """

import pandas as pd
import numpy as np

flights=pd.read_csv("flights.csv path")

flights

flights.head(10)
flights.tail(10)

flights.head(50)

flights.dtypes

flights.ndim

flights.values

flights.columns

flights.shape

flights.size

flights.axes

flights[:20]
flights[:50]
flights[:10]

flights.mean()

flights.median()
flights.SCHED_ARR.median()

len(flights.columns)

flights.columns

flights.SCHED_ARR.min()

flights.SCHED_ARR.describe()

flights.SCHED_ARR.mean()

flights.SCHED_ARR.max()

flights.SCHED_ARR.std()
flights.std()

flights.sample(10)

flights.describe()

flights.head(20).mean()

flights.groupby(['AIRLINE']).mean()

flights.MONTH>5
flights[flights["MONTH"]>5]

flights[['AIRLINE','ORG_AIR','DEST_AIR']]

flights.iloc[:,0:10]

flights.loc[:0]

flights.iloc[:,0:]
flights.iloc[1:3,0:4]

flights.loc[:2]

flights.iloc[0:10,2:3]

flights.iloc[:,2:]

flights.loc[:2]

flights.loc[:4].columns

import matplotlib.pyplot as plt

