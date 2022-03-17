import pandas as pd
import numpy as np

testdf = (pd.read_csv('core_poi-patterns.csv'))[["latitude", "longitude","raw_visit_counts","raw_visitor_counts"]].dropna()

arr = testdf["raw_visit_counts"].to_list()

arr1 = testdf["latitude"].to_list()
series1 = pd.Series(data=arr1)
s1 = series1.repeat(arr)

arr2 = testdf["longitude"].to_list()
series2 = pd.Series(data=arr2)
s2 = series2.repeat(arr)

arr3 = testdf["raw_visit_counts"].to_list()
series3 = pd.Series(data=arr3)
s3 = series3.repeat(arr)

fullpd = pd.concat([s1, s2, s3], axis=1).reset_index(drop = True)

sum(testdf['raw_visit_counts'])

fullpd.to_csv('fullpd.csv')