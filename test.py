import pandas as pd
sales = [["P001", "Windows", 85000],
         ["P002", "Mac", 120000],
         ["P003", "Windows", 200000],
         ["P002", "Mac", 130000]]
columns = ["Product ID", "OS", "Price"]
df = pd.DataFrame(data=sales, columns=columns)
print(df)
price = df["Price"]
print(price)
print(df.iloc[0,0])
print(df.describe())
df["2xPrice"] = df["Price"]*2
print(df)
df.drop(columns=["2xPrice"], inplace=True)
print(df)
filt = df[df["Price"] > 100000]
print(filt)