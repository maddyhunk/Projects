import numpy as np
import pandas as pd

import pickle

data_set = pd.read_csv("Covid Dataset.csv")

X = data_set.iloc[:,:-1].values
Y = data_set.iloc[:,-1].values

from sklearn.model_selection import train_test_split
X_train , X_test , Y_train , Y_test = train_test_split(X , Y , test_size = 0.2 , random_state = 0)


from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression()
classifier.fit(X_train,Y_train)

y_pred = classifier.predict(X_test)

from sklearn.metrics import accuracy_score
accuracy = (accuracy_score(Y_test,y_pred))*100
print(f"Accuracy of your model: {accuracy} %")



pickle.dump(classifier, open('model.pkl','wb'))

model = pickle.load(open('model.pkl','rb'))


