import pandas as pd 
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression

import pickle

data_set = pd.read_csv("USA_Housing.csv")

x = data_set.iloc[:,:5].values
y = data_set.iloc[:,-2].values

# Splitting the dataset into training and test set.

x_train, x_test, y_train, y_test= train_test_split(x, y, test_size= 0.2, random_state=0)  


regressor= LinearRegression()  
regressor.fit(x_train, y_train)  

y_pred= regressor.predict(x_test) 

print(f"Train Score: {(regressor.score(x_train, y_train)*100)}")  
print(f"Test Score: {(regressor.score(x_test, y_test)*100)}")



pickle.dump(regressor, open('model.pkl','wb'))

model = pickle.load(open('model.pkl','rb'))

# regressor.predict([[98000,10,7,3,25000]])
