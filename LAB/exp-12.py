from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier

iris = load_iris()
model = KNeighborsClassifier(n_neighbors=5)
model.fit(iris.data, iris.target)

print(model.predict([iris.data[0]]))
