## Pandas

* *pandas* is a Python library for data processing and analysis. Pandas provides a great range of methods to modify and operate on data; in particular, it allows queries and joins of tables.
* In pandas, you can use various types (for example, integers, dates, floating-point numbers, and strings) in a single table.
* Another valuable tool provided by pandas is its ability to ingest from a great variety of file formats and databases, like SQL, Excel files, JSON, and comma-separated values (CSV) files.

* It is built around a data structure called the **Series** and **DataFrame**.

### loading the library
```python
import pandas as pd
```

### Basic

#### Making a Series
* basic
```python{cmd}
import pandas as pd
sales = ["David", "Bob", "Josh"]
series = pd.Series(data=sales)
print(series)
```
* You can set the column name if you like.
```python{cmd}
import pandas as pd
sales  = ["David", "Bob", "Josh"]
column = "Members"
series = pd.Series(data=sales, name=column)
print(series)
```

#### Making a DataFrame
* DataFrame is more useful than Series, so it is more often used.
* DataFrame assembles Series, so you can think like the Series is a vector and DataFrame is a matrix.
```python {cmd}
import pandas as pd
sales = [["P001", "Windows", 85000],
         ["P002", "Mac", 120000],
         ["P003", "Windows", 200000],
         ["P002", "Mac", 130000]]
columns = ["Product ID", "OS", "Price"]
df = pd.DataFrame(data=sales, columns=columns)
print(df)
```

#### Statictics
```python
df["Price"].min()
df["Price"].max()
df["Price"].mean()
```

#### Sort
* ascending: from low value to high value
* descending: from high value to low value
```python
df = df.sort_values(by="Price")  # ascending
df = df.sort_values(by="Price", ascending=False)  # descending
```

#### Print several rows
```python
print(df.head())
```

#### Taking subgroup
```python
df_win = df[df["OS"]=="Windows"]
df_mac = df[df["OS"]=="Mac"]
```

#### Importing from CSV (comma separated file) file
```python{cmd}
import pandas as pd
df = pd.read_csv("sample.csv")
print(df.head())
```

## Exercise
* Suppose you have sales data in a CSV file (sales_data.csv) containing a column named "Sales".
1. Load this data into a Pandas DataFrame and see the DataFrame with `df.head()` function.
2. Calculate the total, average, max, min sales with `.sum()`, `mean()`, `max()`, and `min()` functions.
<a href="./answer.md#pandas">answer</a>

---

Here are examples showcasing basic usages of Pandas:


* Access a specific column
```python
column_data = df['Column_Name']
```

* Access specific rows using iloc (by index)
```python
specific_rows = df.iloc[3:6]
```

* Access specific rows using loc (by label)
```python
specific_rows = df.loc[df['Column_Name'] == 'Value']
```

* Summary statistics of numerical columns
```python
summary_stats = df.describe()
```

* Unique values in a column
```python
unique_values = df['Column_Name'].unique()
```

* Add a new column
```python
df['New_Column'] = df['Column_A'] + df['Column_B']
```

* Drop a column
```python
df.drop(columns=['Column_Name'], inplace=True)
```

* Filtering rows based on a condition
```python
filtered_data = df[df['Column_Name'] > 10]
```

* You can fill missing values with specific value (in this case, 0)
```python
df.fillna(value=0, inplace=True)
```
* Drop rows with missing values
```python
df.dropna(inplace=True)
```
* Grouped data
```python
# Grouping and Aggregation:
# Group by a column and calculate mean
grouped_data = df.groupby('Column_Name').mean()
```
* You can merge two DataFrames into one, using some colum ans the key.
```python
merged_df = pd.merge(df1, df2, on='Key_Column')
```
* You can create a simple plot
```python
df.plot(x='Column_X', y='Column_Y', kind='line')
```

* You can export th DataFrame to a CSV file
```python
df.to_csv('new_data.csv', index=False)
```

---

## Exercise 2
