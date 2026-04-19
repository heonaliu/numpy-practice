import pandas as pd

df = pd.read_csv("pandas/pokemon.csv", index_col = "Name")

#selection by column
# print(df["Weight"])
# print(df["Name"].to_string())

# print(df[["Name", "Height", "Weight"]].to_string())

#selection by row
#print(df.loc["Bulbasaur":"Venusaur"]) #prints rows from Bulbasaur to Venusaur of the dataframe
#data for pikachu
print(df.loc["Pikachu", ["Height", "Weight"]])
#pass a list as second argument to display only wanted columns

print(df.iloc[0:11, 0:3])

pokemon = input("Enter the name of the pokemon: ")

try:
    print(df.loc[pokemon])
except KeyError:
    print("Pokemon not found in the dataframe.")