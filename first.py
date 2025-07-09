import pandas as pd
data = pd.read_csv(r"C:\Users\surendra\Downloads\file.csv")
# print(data)
# How to analyze the dataFrame
#  .head() --> It shows the first N rows (By default first 5 rows)
data.head()
# print(data.head()) 

# .tail() --> It shows the last N rows (By default bottom 5 rows)
data.tail()
# print(data.tail())

# .shape() --> Total number of rows and total number of columns in the data
data.shape 
# print(data.shape)  #(rows,column)

# .index --> The attribute provides the index of the dataframe
data.index
# print(data.index) #RangeIndex(start=0, stop=8784, step=1)

# .columns --> it shows name of each columns.
data.columns
# print(data.columns)

# .dtypes --> it shows datatype of each columns.
data.dtypes
# print(data.dtypes)

# .unique() --> In a column , it shows the unique values. it can be applied on a single column only.
# not on the whole dataFrame
data['Weather'].unique()
# print(data['Weather'].unique())

# .nunique() --> It shows the total number of unique values. it can be applied on a single column as well as whole dataframe.
data.nunique()
# print(data.nunique())

# .count() --> It shows the total no. of non-vlaues in each columns. it can be applied on a single column as well as on whole dataframe
data.count()
# print(data.count()) 

# .value_counts --> It shows the Unique vlaues with their counts. it can be applied on a single column only.
data['Weather'].value_counts()
# print(data['Weather'].value_counts())

# .info() --> It provides basic information about the dataFrame.
data.info()
# print(data.info())








