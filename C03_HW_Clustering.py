import seaborn as sns
iris = sns.load_dataset('iris')
X_iris = iris.drop('species', axis = 1)
y_iris = iris['species']
from sklearn.cross_validation import train_test_split
Xtrain, Xtest, ytrain, ytest = train_test_split(X_iris, y_iris, random_state = 1)
from sklearn.naive_bayes import GaussianNB # 選擇模型類別
model = GaussianNB()                       # 實體化模型
model.fit(Xtrain, ytrain)                  # 對資料擬合此模型
y_model = model.predict(Xtest)             # 針對新資料進行預測
from sklearn.metrics import accuracy_score
print(accuracy_score(ytest, y_model))
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
model = PCA(n_components = 2)
model.fit(X_iris)
X_2D = model.fit_transform(X_iris)
iris['PCA1'] = X_2D[:, 0]
iris['PCA2'] = X_2D[:, 1]
sns.lmplot("PCA1", "PCA2", hue = 'species', data = iris, fit_reg = False)
plt.show()
           
# from sklearn.mixture import GMM  # 選擇模型類型
# model = GMM(n_components = 3, covariance_type = 'diag') # 不需要使用超參數及實體化模型
# model.fit(X_iris)
# y_gmm = model.predict(X_iris)
# 
# iris['cluster'] = y_gmm
# sns.lmplot("PCA1", "PCA2", data = iris, hue = 'species', col = 'cluster', fit_reg = False)
   
           
           