import pandas as pd

df1 = pd.DataFrame({
    "id": [1,2,3],
    "name": ["pravin","vishal","naruu"]
})

df2 = pd.DataFrame({
    "id": [1,2,4],
    "salary": [50000, 60000, 70000]
})


# inner join 
# merge is for combining data from two tables 
print(pd.merge(df1,df2,on="id",how="inner"))


# left join    -> all data from left and matching from right 
print(pd.merge(df1,df2, on="id", how="left"))


# right join    -> all data from right and matching from left 
print(pd.merge(df1,df2, on="id", how="right"))


# outer join  -> all data from both tables 
print(pd.merge(df1,df2, on="id", how="outer"))


# cross join
print(pd.merge(df1,df2, how="cross"))