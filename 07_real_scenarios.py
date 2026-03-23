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


