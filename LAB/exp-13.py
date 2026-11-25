from sklearn.linear_model import LinearRegression

X = [[2010],[2015],[2020]]
y = [300000,500000,700000]

model = LinearRegression()
model.fit(X, y)

print(model.predict([[2018]]))
