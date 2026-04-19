import pandas as pd

df = pd.read_csv("pandas/pokemon.csv")
print(df)
#print entire dataframe == df.to_string() 

#for json files use pd.read_json instead