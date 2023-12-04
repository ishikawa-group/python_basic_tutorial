## Pandas

Here are examples showcasing basic usages of Pandas:

Loading Data:
Read data from a CSV file into a Pandas DataFrame.
python
Copy code
import pandas as pd

# Load data from a CSV file into a DataFrame
df = pd.read_csv('data.csv')
Viewing Data:
Display the first few rows of the DataFrame.
python
Copy code
# View the first few rows of the DataFrame
print(df.head())
Accessing Data:
Access specific columns or rows in the DataFrame.
python
Copy code
# Access a specific column
column_data = df['Column_Name']

# Access specific rows using iloc (by index)
specific_rows = df.iloc[3:6]

# Access specific rows using loc (by label)
specific_rows = df.loc[df['Column_Name'] == 'Value']
Basic Operations:
Calculate summary statistics and unique values.
python
Copy code
# Summary statistics of numerical columns
summary_stats = df.describe()

# Unique values in a column
unique_values = df['Column_Name'].unique()
Data Manipulation:
Modify the DataFrame by adding or dropping columns and filtering data.
python
Copy code
# Add a new column
df['New_Column'] = df['Column_A'] + df['Column_B']

# Drop a column
df.drop(columns=['Column_Name'], inplace=True)

# Filtering rows based on a condition
filtered_data = df[df['Column_Name'] > 10]
Handling Missing Data:
Handle missing values by filling or dropping them.
python
Copy code
# Check for missing values
missing_values = df.isnull().sum()

# Fill missing values with a specific value
df.fillna(value=0, inplace=True)

# Drop rows with missing values
df.dropna(inplace=True)
Grouping and Aggregation:
Group data and perform aggregate operations.
python
Copy code
# Group by a column and calculate mean
grouped_data = df.groupby('Column_Name').mean()
Merging and Joining DataFrames:
Merge two DataFrames based on a common key.
python
Copy code
# Merge two DataFrames
merged_df = pd.merge(df1, df2, on='Key_Column')
Data Visualization:
Create a simple line plot from DataFrame data.
python
Copy code
# Create a line plot
df.plot(x='Column_X', y='Column_Y', kind='line')
Exporting Data:
Save the DataFrame to a CSV file.
python
Copy code
# Save DataFrame to a CSV file
df.to_csv('new_data.csv', index=False)
These examples cover various basic operations in Pandas for data loading, manipulation, analysis, and visualization. Adjust the code snippets based on your specific data and requirements.



---

Exercise: Analyzing Student Grades

Let's create a small dataset representing student names and their test scores. Then, we'll perform some operations using Pandas.

Import Pandas:
Begin by importing the Pandas library.
python
Copy code
import pandas as pd
Create a DataFrame:
Create a DataFrame with student names and their test scores.
python
Copy code
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Emma'],
    'Test_Score': [85, 70, 90, 60, 75]
}

df = pd.DataFrame(data)
print(df)
Calculate Statistics:
Calculate some statistics of the test scores.
python
Copy code
# Calculate the average test score
average_score = df['Test_Score'].mean()
print("\nAverage Test Score:", average_score)

# Find the highest test score and the student's name
highest_score = df['Test_Score'].max()
student_highest_score = df.loc[df['Test_Score'].idxmax(), 'Name']
print("\nHighest Test Score:", highest_score)
print("Student with the Highest Score:", student_highest_score)
This exercise demonstrates how to create a DataFrame using Pandas, calculate basic statistics like the average and highest test scores, and retrieve information related to those statistics.

You can expand this exercise by adding more data, performing additional calculations, visualizing the data using plots, or exploring more complex operations offered by Pandas for data manipulation and analysis.

---