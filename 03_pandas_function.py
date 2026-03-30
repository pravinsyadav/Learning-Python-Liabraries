import pandas as pd
df = pd.read_csv("tips.csv")                  #loads file 
print(df.head())                              #df means your data and df.head() means print first 5 records
print(df.tail())                              # it will print last 5 records
print(df.shape)            # it gives no of rows and columns 
#here we are using print becuase file is .py if our file is .ipynb then here we are using notebook 
# there we dont need to write print we just write df.shape like this

print(df.columns)           # it will print names of all columns 

print(df.info)            # it will show datatypes or structure of data 

print(df.describe)         # it will show statistics

print(df["tip"])       # it will print a mentioned column values
print(df[["total_bill","tip"]])         # it will print values of two columns 

print(df.iloc[0])         # it will print first row index based 
print(df.loc[0])         # label based