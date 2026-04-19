import pandas as pd

#dataframe is tabular data structure with ros and columns
#2 dimensional

data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
}

#turns the dictionary into dataframe
#has rows and columns
#also has index starting from 0 ==> but also can name with index
df = pd.DataFrame(data, index=["employee1", "employee2", "employee3"])
#print(df)

#print(df.loc["employee2"])

print(df.iloc[0]) #this prints the first row of dataframe

#adding a new column
df["Job"] = ["Engineer", "Doctor", "Artist"]

#print(df)

#add a new row
#need to add a new value to each key in the column
#add multiple {} for multiple rows within the []
#that would look like [{},{},{}]
new_rows = pd.DataFrame([{"Name": "David", "Age": 40, "Job": "Lawyer"}, {"Name": "Eve", "Age": 35, "Job": "Teacher"}], index=["employee4", "employee5"])

#concatenate the new row and existing dataframe
df = pd.concat([df, new_rows])
print(df)
