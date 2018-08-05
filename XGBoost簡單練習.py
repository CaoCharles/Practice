# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 10:33:55 2018

@author: fishburger1013
"""
#用鐵達尼號資料做簡單的XGBoost練習
#%%載入套件
import numpy as np
import pandas as pd
pd.options.mode.chained_assignment = None
#%%讀取資料
titanic = pd.read_csv('C:\\Users\\fishburger1013\\Desktop\\titanic\\train.csv')

#%%刪除遺失值
titanic = titanic[titanic['Age'].notnull()]
titanic = titanic[titanic['Sex'].notnull()]
titanic = titanic[titanic['Pclass'].notnull()]
titanic = titanic[titanic['Survived'].notnull()]
titanic
#%%
X = titanic[['Pclass','Age','Sex']]
y = titanic[['Survived']]

#%%
from sklearn.model_selection import train_test_split
#%%把資料拆成測試和驗證資料
X_train,X_val,y_train,y_val = train_test_split(X,y,test_size=0.2)

#%%
X_train['Sex'] = X_train['Sex'].map({'female':0,'male':1})
X_val['Sex'] = X_val['Sex'].map({'female':0,'male':1})

#%%
X_train = pd.DataFrame(X_train,dtype=np.float)
X_val = pd.DataFrame(X_val,dtype=np.float)
y_train = pd.DataFrame(y_train,dtype=np.str)
y_val = pd.DataFrame(y_val,dtype=np.str)
#%%
from xgboost import XGBClassifier

#%%
xgbc = XGBClassifier()

#%%
xgbc.fit(X_train,y_train)
#%%
print('驗證資料集準確率為',xgbc.score(X_train,y_train))
#%%
print('驗證資料集準確率為',xgbc.score(X_val,y_val))

#%%
from sklearn.metrics import classification_report, confusion_matrix
#%%
print(confusion_matrix(xgbc.predict(X_val),y_val))
#%%









