import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from sklearn.tree import DecisionTreeClassifier
from sklearn import metrics
from sklearn import tree

data=pd.read_csv("./Downloads/house-prices-advanced-regression-techniques/train.csv")
data.head()
header = list(data)