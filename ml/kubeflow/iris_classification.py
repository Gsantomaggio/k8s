import os

import joblib
from sklearn import datasets
from sklearn import neighbors
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier


def download_data():
    print("Download data")
    os.mkdir("models")
    iris = datasets.load_iris()
    X = iris.data
    y = iris.target
    return X, y


def split_training_test():
    X, y = download_data()
    print("Split training")
    return train_test_split(X, y)


def decision_tree_test():
    X_train, X_test, y_train, y_test = split_training_test()
    model_decision_tree = DecisionTreeClassifier()
    model_decision_tree.fit(X_train, y_train)

    prediction_train = model_decision_tree.predict(X_train)
    prediction_test = model_decision_tree.predict(X_test)

    acc_training = accuracy_score(y_train, prediction_train)
    print("Accuracy Train model_decision Tree: {}".format(acc_training))

    acc_test = accuracy_score(y_test, prediction_test)
    print("Accuracy Test Model Decision Tree: {0}".format(acc_test))
    return acc_training, acc_test


def kf_decision_tree_test():
    acc_training, acc_test = decision_tree_test()
    text_file = open("/tmp/output", "w")
    text_file.write("{0}".format(acc_test))
    text_file.close()


def decision_kneighbors_test():
    X_train, X_test, y_train, y_test = split_training_test()
    model_decision_KNC = neighbors.KNeighborsClassifier()
    model_decision_KNC.fit(X_train, y_train)

    prediction_train = model_decision_KNC.predict(X_train)
    prediction_test = model_decision_KNC.predict(X_test)

    acc_training = accuracy_score(y_train, prediction_train)
    print("accuracy Train KNeighborsClassifier:{}".format(acc_training))

    acc_test = accuracy_score(y_test, prediction_test)
    print("accuracy Test KNeighborsClassifier:{0}".format(acc_test))

    return acc_training, acc_test


def kf_decision_kneighbors_test():
    acc_training, acc_test = decision_kneighbors_test()
    text_file = open("/tmp/output", "w")
    text_file.write("{0}".format(acc_test))
    text_file.close()


def get_results():
    path_tree = os.path.abspath("models/tree.pkl")
    path_knc = os.path.abspath("models/knc.pkl")
    return path_tree, path_knc


def decision_kneighbors():
    X_train, y_train, = download_data()
    model_decision_KNC = neighbors.KNeighborsClassifier()
    model_decision_KNC.fit(X_train, y_train)

    prediction_train = model_decision_KNC.predict(X_train)

    acc_training = accuracy_score(y_train, prediction_train)
    print("accuracy Train KNeighborsClassifier:{}".format(acc_training))
    joblib.dump(model_decision_KNC, "models/knc.pkl")


def decision_tree():
    X_train, y_train = download_data()
    model_decision_tree = DecisionTreeClassifier()
    model_decision_tree.fit(X_train, y_train)

    prediction_train = model_decision_tree.predict(X_train)

    acc_training = accuracy_score(y_train, prediction_train)
    print("Accuracy Train model_decision Tree: {}".format(acc_training))
    joblib.dump(model_decision_tree, "models/tree.pkl")


if __name__ == '__main__':
    import sys

    globals()[sys.argv[1]]()
