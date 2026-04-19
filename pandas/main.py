import pandas as pd
#print(pd.__version__)
#series = pandas one dimensional array
#create array
data = [100,102,104,200,202]
series = pd.Series(data, index=['a','b','c','d','e'])
print(series[series >= 200]) #prints any value that is greater than or equal 200

#loc and iloc can be used to locate certain values/index of values

calories = {"day1": 420, "day2": 380, "day3": 390}
series = pd.Series(calories)

print(series.loc["day2"]) #loc is used to locate the index of the value

series.loc["day3"] += 400

print(series.iloc[2]) #iloc is used to locate the position of the value
