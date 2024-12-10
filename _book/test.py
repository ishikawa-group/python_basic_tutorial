from sklearn.datasets import load_iris
from sklearn import tree
import matplotlib.pyplot as plt

iris = load_iris()
X, y = iris.data[:, 2:4], iris.target
clf = tree.DecisionTreeClassifier()
clf = clf.fit(X, y)
tree.plot_tree(clf, filled=True)
plt.show()

from mlxtend.plotting import plot_decision_regions
import numpy as np

fig, ax = plt.subplots(figsize=(7, 7))
plot_decision_regions(X, y, clf=clf)
plt.xlabel('petal length [cm]')
plt.ylabel('petal width [cm]')
plt.legend(loc='upper left')
plt.tight_layout()
plt.show()
