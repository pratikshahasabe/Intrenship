import numpy as np
import pandas as pd

df=pd.read_csv('trainingdata.txt')

features=['Amount of time he slepe']
response=['Amount of time he was active']

X=df[features]
y=df[response]

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2, random_state=0)

from sklearn.linear_model import LinearRegression
from sklearn import metrics

model=LinearRegression()
model.fit(X_train, y_train)

accuracy=model.score(X_test,y_test)
print(accuracy*100,'%')

model.predict(X_test)


import pickle
pickle.dump(model, open('model.pkl','wb'))

model = pickle.load(open('model.pkl', 'rb'))
print(model.predict([[24]]))