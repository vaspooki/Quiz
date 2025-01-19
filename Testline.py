import json
import pandas as pd

with open('API.json', 'r') as file:
    data = json.load(file)

print(data)

# with open('QuizSubmissionData.json', 'r') as file:
#     data = json.load(file)

# print(data)

# with open('QuizEndpoint.json', 'r') as file:
#     data = json.load(file)

# print(data)

df = pd.DataFrame(data)

print(df.columns)
print(df.head())
print(df.tail())
print(df.info())
print(df.describe())
print(df.dtypes)
print(df.shape)
print(df.size)
print(df.ndim)
print(df.memory_usage())

The difficulty level is not available from APIs. Therefore, analysis is not made n that basis.

# print(df)
