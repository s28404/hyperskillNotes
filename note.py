from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import precision_score, f1_score

data = load_iris()

X = data.data
y = data.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=27)

model = LogisticRegression()

model.fit(X_train, y_train)
 
y_pred = model.predict(X_test)

y_proba = model.predict_proba(X_test)
print(y_proba[0])
print(y_pred[0])

precision = precision_score(y_test, y_pred, average='macro')
print(precision)

f1 = f1_score(y_test, y_pred, average='macro')
print(f1)