from sklearn.linear_model import LinearRegression

X = [[2000,10],[1500,5],[3000,15],[1000,3]]
y = [25000,18000,35000,12000]

model = LinearRegression()
model.fit(X, y)

pred = model.predict([[2200,12]])
print("Predicted Sales:", pred)
