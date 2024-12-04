import pandas as pd
import numpy as np

# Load the dataset
file_path = "AQI_Data (1).csv"  # Replace with your file's path if different
data = pd.read_csv(file_path)

# Display the first 8 rows
print("First 8 rows:")
print(data.head(8))

# Display the last 5 rows
print("\nLast 5 rows:")
print(data.tail(5))

# Show the dtype and number of non-null values in each column
print("\nData types and non-null values:")
print(data.info())

# Compute mean AQI, max PM2.5, and min PM10 values for each city
if 'City' in data.columns and 'AQI' in data.columns and 'PM2.5' in data.columns and 'PM10' in data.columns:
    city_stats = data.groupby('City').agg({
        'AQI': np.mean,
        'PM2.5': np.max,
        'PM10': np.min
    })
    city_stats.rename(columns={
        'AQI': 'Mean AQI',
        'PM2.5': 'Max PM2.5',
        'PM10': 'Min PM10'
    }, inplace=True)
    print("\nCity-wise statistics:")
    print(city_stats)
else:
    print("\nRequired columns (City, AQI, PM2.5, PM10) are not present in the dataset.")

# Create a pivot table to summarize the dataset
pivot_table = df.pivot_table(index='City', values='PM2.5', aggfunc='max')

# Display the resulting pivot table
print(pivot_table)

# Save the pivot table to a csv file
pivot_table.to_csv('pivot.csv', index=True)