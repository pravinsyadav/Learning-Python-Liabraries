import pandas as pd

df = pd.read_csv("tips.csv")

print(df.columns)


# rename columns
df.rename(columns={"total_bill":"bill"},inplace=True)
df.rename(columns={"sex":"gender"},inplace=True)
print(df.columns)


# change datatype
df["size"] = df["size"].astype(int)


#create new column
df["tip_percentage"] = (df["tip"]/df["bill"])*100
print(df.columns)
print(df.loc[0:3])


# sort data 
print(df.sort_values(by="bill",ascending=False))         # ascending false means in descending order .. highest first
print(df.sort_values(by="bill",ascending=True))         # ascending true means in ascending order .. lowest first


# unique values
print(df["day"].unique())


# value counts
print(df["gender"].value_counts())
# or 
print(df.groupby("gender")["gender"].count())


# rename tip to total_tip
df.rename(columns={"tip":"total_tip"},inplace=True)
print(df.columns)


# delete column
df.drop("tip_percentage", axis=1, inplace=True)
print(df.columns)


# Remove Duplicate Records Based on Column
df.drop_duplicates(subset="bill")


# Find Employees with Second Highest bill
df["bill"].sort_values(ascending=False).iloc[1]


# Replace Missing bill with Average bill
df["bill"].fillna(df["bill"].mean())


# Sort Data by Multiple Columns
df.sort_values(["bill","gender"],ascending=[True,True])