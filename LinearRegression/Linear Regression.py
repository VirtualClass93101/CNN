import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from sklearn.tree import DecisionTreeClassifier
from sklearn import metrics
from sklearn import tree

data=pd.read_csv("./Downloads/house-prices-advanced-regression-techniques/train.csv")
na_data = data.isnull().sum()[data.isnull().sum()>0].sort_values()
# Electrical         1 供電類型 

# MasVnrType         8 外牆表面
# MasVnrArea         8 外牆面積

# BsmtQual          37 地下室高度
# BsmtCond          37 地下室狀況(棒,差...)
# BsmtFinType1      37 上述的裝潢

# BsmtExposure      38 走去草皮前的一塊地方
# BsmtFinType2      38 上述的質量(讚的可活動空間,可住宿...)

# GarageCond        81 車庫
# GarageQual        81
# GarageFinish      81
# GarageType        81
# GarageYrBlt       81

# LotFrontage      259
# FireplaceQu      690
# Fence           1179
# Alley           1369
# MiscFeature     1406
# PoolQC          1453

#眾數填補
data["Electrical"].fillna('SBrkr',inplace=True)

#當作沒有
data["MasVnrType"].fillna('None',inplace=True)
data["MasVnrArea"].fillna(0.0,inplace=True)

#眾數填補
data["BsmtQual"].fillna('TA',inplace=True)
data["BsmtCond"].fillna('TA',inplace=True)
data["BsmtFinType1"].fillna('Unf',inplace=True)

#眾數填補
data["GarageCond"].fillna('TA',inplace=True)
data["GarageQual"].fillna('TA',inplace=True)
data["GarageFinish"].fillna('Unf',inplace=True)
data["GarageType"].fillna('Attchd',inplace=True)
data["GarageYrBlt"].fillna(2005,inplace=True)

#平均數填補
data["LotFrontage"].fillna(data['LotFrontage'].mean(),inplace=True)
#眾數填補
data["FireplaceQu"].fillna('NA',inplace=True)
data["Fence"].fillna('NA',inplace=True)
data["Alley"].fillna('NA',inplace=True)
data["MiscFeature"].fillna('NA',inplace=True)
#捨棄
data.drop(['PoolQC'],axis=1)
