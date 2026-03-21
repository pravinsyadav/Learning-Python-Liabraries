import pandas as pd
data = {
    "name": ["Pravin", "Amit"],
    "salary": [50000, 60000]
}
df = pd.DataFrame(data)     # it will create table with index 
print(df)