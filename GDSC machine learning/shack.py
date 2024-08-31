import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

df = pd.read_csv('shake shack nutrition.csv')

sns.set()
# sns.pairplot(df,hue='Calories',height=2)
df.head()
df.info()

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

plt.show()
X = df[['Total Fat', 'Trans Fat', 'Sat Fat', 'Cholesterol', 'Sodium', 'Total Carb', 'Fiber','Sugars','Protein']]
Y = df['Calories']

print(X)
print(Y)

scaler = preprocessing.StandardScaler().fit(X)
X_scaled = scaler.transform(X)
print(X_scaled[:10])

X_train, X_test, y_train, y_test = train_test_split(np.asarray(X_scaled), np.asarray(Y), random_state=42)
print(X_train[:3])
print(y_train[:3])
print()
print(X_test[:3])
print(y_test[:3])

model = LinearRegression().fit(X_train, y_train)

weight = model.coef_
bias = model.intercept_

print("Weight:", weight)
print("Bias:", bias)

y_predict = model.predict(X_test)

print("Model predict:")
print(y_predict)
print()
print("Real data")
print(y_test)

print(f"Train Accuracy: {model.score(X_train, y_train)}")
print(f"Test Accuracy: {model.score(X_test, y_test)}")
print(f"Train MSE: {mean_squared_error(y_train, model.predict(X_train))}")
print(f"Test MSE: {mean_squared_error(y_test, model.predict(X_test))}")

index = np.random.randint(154)

X_reg, y_reg = X_scaled, Y

print("Predict:", model.predict([X_reg[index]]))
print("Actual:", y_reg[index])

print(
model.predict([
    [25.0, 10.0, 0.5, 95.0, 1200.0, 28.0, 1.0, 5.0, 28.0],
    [35.0, 15.0, 1.0, 110.0, 1300.0, 30.0, 0.5, 7.0, 32.0],
    [28.0, 12.0, 0.8, 100.0, 1225.0, 27.0, 0.2, 6.0, 30.0]
]))