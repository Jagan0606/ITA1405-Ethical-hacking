import pandas as pd

data = pd.read_csv("training_data.csv")
concepts = data.iloc[:, :-1].values
target = data.iloc[:, -1].values

def candidate_elimination(concepts, target):
    s = concepts[0].copy()
    g = [['?' for _ in range(len(s))]]

    for i, instance in enumerate(concepts):
        if target[i] == "Yes":
            for j in range(len(s)):
                if instance[j] != s[j]:
                    s[j] = '?'
        else:
            for j in range(len(s)):
                if s[j] != instance[j]:
                    g.append([s[k] if k == j else '?' for k in range(len(s))])
    return s, g

s, g = candidate_elimination(concepts, target)
print("Specific Hypothesis:", s)
print("General Hypothesis:", g)
