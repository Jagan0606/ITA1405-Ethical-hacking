from sklearn.naive_bayes import GaussianNB

X = [[50000,750],[30000,600],[45000,720],[25000,580]]
y = [1,0,1,0]   # 1=Approved, 0=Rejected

model = GaussianNB()
model.fit(X, y)

result = model.predict([[40000,700]])
print("Loan Status:", result)
