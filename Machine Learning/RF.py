from sklearn import datasets
iris=datasets.load_iris()
print(iris.target_names)
print(iris.feature_names)
print(iris.data[:5,])
print(iris.target)

import pandas as pd
data=pd.DataFrame({
    'sepal length':iris.data[:,0],
    'sepal width':iris.data[:,1],
    'petal length': iris.data[:,2],
    'petal width':iris.data[:,3],
    'species': iris.target
})

data.head()
data.tail()

from sklearn.model_selection import train_test_split

X=data[['sepal length','sepal width','petal length','petal width']]
y=data['species']

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3)

from sklearn.ensemble import RandomForestClassifier

clf=RandomForestClassifier(n_estimators=100)
clf.fit(X_train,y_train)
y_pred=clf.predict(X_test)

from sklearn import metrics
print("Accuracy",metrics.accuracy_score(y_test,y_pred))

feature_imp=pd.Series(clf.feature_importances_,index=iris.feature_names)
feature_imp.sort_values(ascending=False)

import matplotlib.pyplot as plt 
import seaborn as sns
%matplotlib inline
sns.barplot(x=feature_imp,y=feature_imp.index)

plt.xlabel('Feature Importance Score')
plt.ylabel('Features')
plt.title('Visualizing Important Features')
plt.legend()
plt.show()

X=data[['petal width','petal length','sepal length']]
y=data['species']
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.5,random_state=5)
clf2=RandomForestClassifier(n_estimators=100)
clf2.fit(X_train,y_train)
y_pred=clf2.predict(X_test)
print("Accuracy",metrics.accuracy_score(y_test,y_pred))