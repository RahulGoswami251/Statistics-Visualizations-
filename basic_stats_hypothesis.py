# -*- coding: utf-8 -*-
"""Basic Stats-Hypothesis.ipynb"""


from scipy import stats
p=1-stats.t.cdf(1.41,49)
p*2

import numpy as np
(4-4.6)/(3/np.sqrt(50))

2*stats.t.cdf(-1.41,df=49)

(4-4.2)/(3/np.sqrt(50))

2*stats.t.cdf(-0.47,df=49)

(4-3.9)/(3/np.sqrt(50))

2*stats.t.cdf(-0.23,df=49)

(4-5.3)/(3/np.sqrt(50))

2*stats.t.cdf(-3.06,df=49)

(4-3.7)/(3/np.sqrt(50))

2*stats.t.cdf(-0.70,df=49)

(4-4.1)/(3/np.sqrt(50))

2*stats.t.cdf(-0.23,df=49)

(4-4)/(3/np.sqrt(50))

2*stats.t.cdf(0,df=49)

(4-4.4)/(3/np.sqrt(50))

2*stats.t.cdf(-0.94,df=49)

a=np.array([0.593,0.142,0.329,0.691,0.231,0.793,0.519,0.392,0.418])

a

p=stats.ttest_1samp(a,0.3)[1]
p

p/2

from scipy import stats
import numpy as np

Control=np.array([91, 87, 99, 77, 88, 91])
Treat = np.array([101, 110, 103, 93, 99, 104])

p=stats.ttest_ind(Control,Treat)[1]

p

n1 = 247
p1 = .37

n2 = 308
p2 = .39

population1 = np.random.binomial(1, p1, n1)
population2 = np.random.binomial(1, p2, n2)

population1.mean()

population1

population2.mean()
population2

import statsmodels.api as sm
sm.stats.ttest_ind(population1,population2)

!pip install sklearn

# Load libraries
from sklearn import datasets
# Load digits dataset
iris = datasets.load_iris()

iris

import pandas as pd
df = pd.DataFrame(iris.data)
import scipy.stats as stats
stats.f_oneway(df.iloc[:,0], df.iloc[:,1],df.iloc[:,2])

stats.f_oneway(df.loc[:0],df.loc[:1],df.loc[:2])

from scipy.stats import chi2_contingency

table=[[20,30,15],[20,15,30]]

stats,p,df,expected=chi2_contingency(table)

stats

p

df

expected

alpha=0.05
print("significance=%.f,p=%.f",(alpha,p))

if p>alpha:
    print("Accepts Null H0-Variables are Independent")
else:
    print("Rejects Null Ha-Variables are dependent")