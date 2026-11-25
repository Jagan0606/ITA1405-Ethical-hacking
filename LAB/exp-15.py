from sklearn.datasets import load_iris
from sklearn.naive_bayes import GaussianNB

iris = load_iris()
model = GaussianNB()
model.fit(iris.data, iris.target)

print(model.predict([iris.data[1]]))
