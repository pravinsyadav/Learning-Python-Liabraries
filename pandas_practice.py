import pandas as pd
df = pd.read_csv("tips.csv")                  #loads file 
print(df.head())                              #df means your data and df.head() means print first 5 records
print(df.shape)            # it gives no of rows and columns 
#here we are using print becuase file is .py if our file is .ipynb then here we are using notebook 
# there we dont need to write print we just write df.shape like this