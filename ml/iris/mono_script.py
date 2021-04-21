import joblib
from sklearn import datasets
from sklearn import neighbors
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

print("--------------------------------------")

# import some data to play with
iris = datasets.load_iris()
# print(iris['DESCR'])
X = iris.data
y = iris.target

# we are going to split the data
# part of the data will be used for training
# part of the data for test
X_train, X_test, y_train, y_test = train_test_split(X, y)

# the model is not trained yet, just a definition
model_decision_tree = DecisionTreeClassifier()

# fit is needed to train the model
model_decision_tree.fit(X_train, y_train)

# give the input and return the output
prediction_train = model_decision_tree.predict(X_train)

# never seen this data before
prediction_test = model_decision_tree.predict(X_test)

# accuracy 
print("Prediction Train model_decision Tree ")
print(accuracy_score(y_train, prediction_train))

print("Prediction Test Model Decision Tree")
print(accuracy_score(y_test, prediction_test))

print("--------------------------------------")

model_decision_KNC = neighbors.KNeighborsClassifier()
model_decision_KNC.fit(X_train, y_train)

prediction_train = model_decision_KNC.predict(X_train)
prediction_test = model_decision_KNC.predict(X_test)

print("Prediction Train model_decision KNC ")
print(accuracy_score(y_train, prediction_train))

print("Prediction Test Model Decision KNC")
print(accuracy_score(y_test, prediction_test))

print("--------------------------------------")
print("Save Results")

joblib.dump(model_decision_tree, "tree.pkl")
joblib.dump(model_decision_KNC, "knc.pkl")
print("--------------------------------------")
