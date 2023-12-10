# from sklearn.datasets import load_iris
# from sklearn.model_selection import train_test_split
# from sklearn.ensemble import RandomForestClassifier

# X, y = load_iris(return_X_y=True)
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=27)

# model = RandomForestClassifier(n_estimators=25,
#                                max_features=3,
#                                oob_score=True,
#                                random_state=42)

# model.fit(X_train, y_train)

# y_pred = model.predict(X_test)

# y_proba = model.predict_proba(X_test)
# print(y_proba[7])
# print(y_pred[7])

# print(model.oob_score_)
# print(model.oob_decision_function_[6])
# print(model.oob_decision_function_[7])


# print(len(model.estimators_))

# # make a prediction using 0th tree
# tree = model.estimators_[0]
# print(tree.predict(X_test[:10]))

import os
