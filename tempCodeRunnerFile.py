import pandas as pd
df = pd.read_csv("tips.csv")                  #loads file 
print(df.head())                              #df means your data and df.head() means print first 5 records
print(df.tail())