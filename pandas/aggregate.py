import pandas as pd

#aggregate functions = 
# functions that return a single value for a given group of values

df = pd.read_csv("pandas/pokemon.csv")

# print(df.mean(numeric_only=True))
# #find the mean of columns of numeric data types
# print(df.sum(numeric_only=True))

# print(df.min(numeric_only=True))

# print(df.max(numeric_only=True))

# print(df.count(numeric_only=True))
#doesn't include any null values in count


# #for a single column
# print(df["Height"].mean())
# #find the mean of columns of numeric data types
# print(df["Height"].min())

# print(df["Height"].max())

# print(df["Height"].sum())

# print(df["Height"].count())


#groupby = split the data into groups based on some criteria
grouped = df.groupby("Type1") #group the data by the "Type1" column
print(grouped["Height"].sum()) #find the mean of the "Height" column for each group
#the sum of all the different types of pokemon heights

print(grouped["Height"].max()) #find the mean of the "Height" column for each group
print(grouped["Height"].count())