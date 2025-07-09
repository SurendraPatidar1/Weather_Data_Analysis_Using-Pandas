# Weather Data Analysis Using Pandas(Python)
![](https://github.com/SurendraPatidar1/Weather_Data_Analysis_Using-Pandas/blob/main/OIP.jpg)

## 🌦️ Overview
This project involves analyzing a weather dataset to extract meaningful insights about weather conditions, wind speed, visibility, humidity, and other meteorological factors. Using Python and the Pandas library, we perform exploratory data analysis (EDA) by answering specific questions about the dataset, such as finding unique values, calculating summary statistics, identifying conditions like clear weather or snow, and filtering records based on multiple criteria.

## 🎯 Objectives
Identify unique values and frequencies for specific weather attributes (e.g., wind speed, weather condition).

Count occurrences of specific weather events, such as clear weather, fog, or snow.

Detect and handle missing (null) values in the dataset.

Rename columns to improve clarity and consistency.

Calculate descriptive statistics including mean, standard deviation, and variance for numeric columns.

Group the data by weather condition and compute aggregated metrics (mean, min, max).

Filter and extract records based on complex conditions, such as:

Wind speed above a threshold with specific visibility.

Weather being clear with high humidity.

Weather being clear or visibility exceeding a certain level.

Improve understanding of how different weather parameters interact under certain conditions.

- **Dataset Link:** [Movies Dataset](https://github.com/SurendraPatidar1/Weather_Data_Analysis_Using-Pandas/blob/main/file.csv)

## Business Problems and Solutions

<!-- Import the pandas library to access pandas in-builts functions and methods -->
import pandas as pd
<!-- Read the Weather csv data for analysis using read_csv -->
data = pd.read_csv(r"C:\Users\surendra\Downloads\file.csv")

# Q)1. Find all the unique 'Wind Speed' values in the data.
data.nunique() 
print(data.nunique()) --> It gives the count of all unique values

 <!-- data['Wind Speed_km/h'].nunique() -->
print(data['Wind Speed_km/h'].nunique()) --> it gives only the wind-speed column unique count

data['Wind Speed_km/h'].unique()
print(data['Wind Speed_km/h'].unique()) it gives the acutal unique values of the wind-speed


# Q)2. Find the number of times when the 'Weather is exactly clear'.
#Three-Ways --> value_counts() , Filtering ,Groupby 
print(data.Weather.value_counts())
print(data[data.Weather == 'Clear'])
print(data.groupby('Weather').get_group('Clear'))

# Q)3. Find the number of times when the 'Wind Speed was exactly 4km/hr'.
print(data[data['Wind Speed_km/h'] == 4])

# Q)4. Find out all the Null Values in the data.
print(data.isnull().sum())

# Q)5. Rename the column name 'Weather' of the dataframe to 'Weather Condition'.

change = data.rename(columns={'Weather' : 'Weather Condition'})
print(change)

# Q)6. What is the mean 'Visibility_km' ?
print(data.Visibility_km.mean()) 

# Q)7. What is the Standard Deviation of 'Pressure' in this data ?
print(data.Press_kPa.std())

# Q)8.What is the Variance of 'Relative Humidity' in the data.
# It find the variance of the rel humanity column 
print(data['Rel Hum_%'].var())

# Q)9. Find all instances when 'Snow' was recorded.
# We have to three ways to find the snow count
print(data['Weather'].value_counts())
print(data[data['Weather'] == 'Snow'])
print (data[data['Weather'].str.contains('Snow')])

# Q)10. Find all instances when 'Wind Speed is above 24 and Visibility is 25'.
print(data) Visibility_km Wind Speed_km/h
print(data[(data['Wind Speed_km/h'] > 24) & (data['Visibility_km'] == 25)])\

# Q)11. What is the mean value of each column against "Weather Condition".
grouped_result = data.groupby('Weather')
print(grouped_result.mean(numeric_only=True))
 
# Q)12. What is the Minimum and Maximum Value of each column against each 'Weather Condition ?.
print(data.groupby('Weather').min())
print(data.groupby('Weather').max())

# Q)13. Find all the records where 'Weather is Fog' ?
print(data[data['Weather'] == 'Fog'])

# Q)14. Find all the instances when 'Weather is Clear' or 'Visibility is above 40' ?
print(data[(data['Weather'] == 'Clear') | (data['Visibility_km'] > 40)])

# Q)15. Find all the Instances When - 'Weather is Clear and Realtive Humidity is above
#     A:- 'Weather is Clear and Realtive Humidity is greater than 50 ?
#     OR
#     B:- 'Visibility is Above 40'?
print(
    data[
        ((data['Weather'] == 'Clear') & (data['Rel Hum_%'] > 50))   |
        (data['Visibility_km'] > 40)
    ]
)

