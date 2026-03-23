import pandas as pd
df = pd.read_csv("tips.csv")

#IMP->
    # always use (&) (|) instead of 'and' 'or'
    

#print rows where total bill is less than 25 (total_bill < 25)
print(df[df["total_bill"]<25]) 


#it will print only male records 
print(df[df["sex"]=="Male"])


# multiple conditions 
print(df[(df["total_bill"] < 25) & (df["sex"] == "Male")])


# show rows where tip is greater than 5 ( tip > 5)
print(df[df["tip"] > 5])


#show rows where total bill > 20 and day = sunday 
print(df[(df["total_bill"] > 20) & (df["day"]=="Sun")])


#it will print first 3 records 
print(df.iloc[0:3])


#it will calculate avg of total_bill
print(df["total_bill"].mean())


