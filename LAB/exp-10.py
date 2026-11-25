from sklearn.mixture import GaussianMixture
import numpy as np

X = np.array([[1],[2],[8],[9]])

gmm = GaussianMixture(n_components=2)
gmm.fit(X)

print(gmm.predict(X))
