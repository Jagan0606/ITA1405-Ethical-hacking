from sklearn.tree import DecisionTreeClassifier

X = [[25,30000],[40,70000],[35,50000]]
y = ['Bad','Good','Good']

model = DecisionTreeClassifier()
model.fit(X, y)

print(model.predict([[30,40000]]))
