from sklearn import linear_model
from pandas import DataFrame
import pandas as pd
import pandas
import matplotlib.pyplot as plt

input_data = pandas.read_table("height.csv", sep=",", header=0, names=("weight", "height"))

plt.scatter(input_data["weight"], input_data["height"])
#plt.show()

predictor = pd.DataFrame(input_data, columns=["weight"])
outcome = pd.DataFrame(input_data, columns=["height"])

lm = linear_model.LinearRegression()
lm_model = lm.fit(predictor, outcome)

predicted_heights = lm.predict(predictor)

#print("Predicted:")
#print(predicted_heights[0:6])
#print("Actual:")
#print(outcome[0:6])

r_squared = lm.score(predictor, outcome)
print(r_squared)