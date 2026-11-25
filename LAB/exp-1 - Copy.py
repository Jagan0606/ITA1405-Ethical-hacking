def find_s(training_data):
    hypothesis = training_data[0][:-1]

    for instance in training_data:
        if instance[-1] == "Yes":
            for i in range(len(hypothesis)):
                if hypothesis[i] != instance[i]:
                    hypothesis[i] = '?'
    return hypothesis

data = [
    ['Sunny','Warm','Normal','Strong','Warm','Same','Yes'],
    ['Sunny','Warm','High','Strong','Warm','Same','Yes'],
    ['Rainy','Cold','High','Strong','Warm','Change','No']
]

print("Most Specific Hypothesis:", find_s(data))
