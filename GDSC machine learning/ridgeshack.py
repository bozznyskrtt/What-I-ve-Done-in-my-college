import pandas as pd
import seaborn as sb
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

df = pd.read_csv('shake shack nutrition.csv')


def range_to_average(cell):
    # Check if the cell is already a float
    if isinstance(cell, (float, np.int64)):
        return cell
    parts = str(cell).split(' - ')  # Convert to string before splitting
    if len(parts) == 2:
        return (float(parts[0]) + float(parts[1])) / 2
    else:
        try:
            return float(cell)
        except ValueError:
            return None


lis = [2, 3, 4, 7, 8, 10, 11]
for i in lis:
    df.iat[97, i] = range_to_average(df.iat[97, i])
    print(df.iat[97, i])
    df.iat[98, i] = range_to_average(df.iat[98, i])
    print(df.iat[98, i])

df.drop(['Category','Menu'],axis = 1,inplace= True)

X = df[['Total Fat', 'Trans Fat', 'Sat Fat', 'Cholesterol', 'Sodium', 'Total Carb', 'Fiber','Sugars','Protein']]
Y = df['Calories']
poly = preprocessing.PolynomialFeatures(degree=3)
poly_features = poly.fit_transform(X)
scaler = preprocessing.StandardScaler().fit(poly_features)
X_scaled = scaler.transform(poly_features)
X_train, X_test, y_train, y_test = train_test_split(np.asarray(X_scaled), np.asarray(Y), random_state=42)
print(X_train[:3])
print(y_train[:3])
print()
print(X_test[:3])
print(y_test[:3])

model_ridge = Ridge(alpha=3.00).fit(X_train, y_train)
weight_ridge = model_ridge.coef_
bias_ridge = model_ridge.intercept_

print("Weight:")
print(weight_ridge)
print()
print("Bias:")
print(bias_ridge)
y_predict_ridge = model_ridge.predict(X_test)
print("Model predict:")
print(y_predict_ridge)
print()
print("Real data:")
print(y_test)

print(f"Train Accuracy: {model_ridge.score(X_train, y_train)}")
print(f"Test Accuracy: {model_ridge.score(X_test,y_test)}")
print(f"Train MSE: {mean_squared_error(y_train, model_ridge.predict(X_train))}")
print(f"Test MSE: {mean_squared_error(y_test, model_ridge.predict(X_test))}")