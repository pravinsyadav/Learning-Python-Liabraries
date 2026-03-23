import pandas as pd
df = pd.read_csv("tips.csv")

print(df.columns)

#syntax of group by 
# df.groupby("column_name")["target_column"].operation()


# total tip by gender
print(df.groupby("sex")["tip"].sum())


# avg bill by day 
print(df.groupby("day")["total_bill"].mean())


# count values
print(df.groupby("sex")["tip"].count())


# multiple aggregations
print(df.groupby("day")["total_bill"].agg(["sum","mean","max","min"]))


# group multiple columns 
print(df.groupby(["sex","day"])["total_bill"].mean())


# total bill per day 
print(df.groupby("day")["total_bill"].sum())


