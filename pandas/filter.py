import pandas as pd

df = pd.read_csv("pandas/pokemon.csv")

#Filtering = keeping the rows that match a condition

# tall_pokemon = df[df["Height"]>= 1.0]
# print(tall_pokemon)

heavy = df[df["Weight"] >= 100.0]
#print(len(heavy))


legendary = df[df["Legendary"] == 1]
#print(legendary)

water = df[(df["Type1"]=="Water") | (df["Type2"]=="Water")]
print(water)

ff_pokemon = df[(df["Type1"]=="Fire") & (df["Type2"]=="Flying")]
print(ff_pokemon)

rows = df.loc[df["Type1"]=="Fire", ["Name", "Type1", "Type2"]]
print(rows)