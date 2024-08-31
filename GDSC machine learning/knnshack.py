import pandas as pd
import seaborn as sb
import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix
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

print(df['Category'].unique())
cat_lis = df['Category'].unique()
print(cat_lis)


def cat_to_number():
    count = 0
    for i in df['Category']:
        k = 0
        for j in  cat_lis:
            if i == j:
               df.iat[count,0] = k
            k+=1
        count+=1


cat_to_number()
print(df['Category'][1])
print(df['Category'][1])
print(df.iat[0,2])
print(df['Category'][1])
print(df['Category'])
df.drop(['Menu'],axis = 1,inplace= True)

y_lis = []
for i in df['Category']:
    y_lis.append(i)
print(y_lis)
X = df[['Calories', 'Total Fat', 'Trans Fat', 'Sat Fat', 'Cholesterol', 'Sodium', 'Total Carb',  'Sugars', 'Protein']]
Y = y_lis

scaler = preprocessing.StandardScaler().fit(X)
X_scaled = scaler.transform(X)
print(X_scaled[:10])

X_train, X_test, y_train, y_test = train_test_split(np.asarray(X_scaled), np.asarray(Y), random_state=42)
print(X_train[:3])
print(y_train[:3])
print()
print(X_test[:3])
print(y_test[:3])

knn = KNeighborsClassifier().fit(X_train, y_train)

y_raw_predict_knn = knn.predict_proba(X_test)
y_predict_knn = knn.predict(X_test)

print("Model raw prediction:")
print(y_raw_predict_knn)

print("Model prediction")
print(y_predict_knn)
print("Actual")
print(X_test)

print("round 2")
print(knn.predict(X_test))

for i in range(153):
    print(knn.predict([X_scaled[i]]),end=' ')
print()

print(f"Train Accuracy: {knn.score(X_train, y_train)}")
print(f"Test Accuracy: {knn.score(X_test, y_test)}")
conf_matrix_knn = confusion_matrix(y_test, y_predict_knn)
print(conf_matrix_knn)

print(knn.predict([
    [1620.0, 35.0, 15.0, 1.5, 590.0, 1700.0, 30.0, 8.0, 540.0],
    [1480.0, 22.0, 10.0, 0.5, 60.0, 1000.0, 20.0, 4.0, 30.0],
    [710.0, 40.0, 18.0, 2.0, 120.0, 2000.0, 35.0, 10.0, 45.0]
]))

print(knn.predict(X_test))
