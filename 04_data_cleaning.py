import pandas as pd
df = pd.read_csv("tips.csv")


#check missing values
print(df.isnull().sum())        #it will show how many null values are there in each column


#handle missing values
# 1->
    #remove null values
print(df.dropna())     

#2 ->
    #fill null values
print(df.fillna(0))               #it is used based on situation

