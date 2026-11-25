from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder

X = [['Sunny','Hot'],['Overcast','Hot'],['Rain','Mild']]
y = ['No','Yes','Yes']

le = LabelEncoder()
X = [[le.fit_transform(col)[i] for col in zip(*X)] for i in range(len(X))]

model = DecisionTreeClassifier(criterion='entropy')
model.fit(X, y)

print("Prediction:", model.predict(X))
