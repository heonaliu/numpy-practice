import pandas as pd

#data cleaning
#process of fixing/removing incomplete, incorrect, or irrelevant data from a dataset
# much of the work is done with pandas

df = pd.read_csv("pandas/pokemon.csv")

#drop irrelevant columns
### df = df.drop(columns=["Legendary", "No"])

#handle missing data
### df = df.dropna(subset=["Type2"])
# any columns placed here will drop if there is a NA in that col

#df = df.fillna({"Type2": "None"})
#fill any NA values with None

#3. Fix inconsistent values
#df["Type1"] = df["Type1"].replace({"Grass" : "GRASS", "Fire" : "FIRE", "Water" : "WATER"})


#4. Standardize text
#df["Name"] = df["Name"].str.lower()
#take the col of name and make all lowercase

#df["Legendary"] = df["Legendary"].astype(bool)

df = df.drop_duplicates()
print(df.to_string())