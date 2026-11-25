from sklearn.ensemble import RandomForestClassifier

X = [[1000,4],[1500,6],[2000,8],[1200,3]]
y = [1,2,3,0]   # price range

model = RandomForestClassifier()
model.fit(X, y)

pred = model.predict([[1800,7]])
print("Predicted Price Range:", pred)
