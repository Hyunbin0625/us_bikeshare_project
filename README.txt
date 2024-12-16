# US-Bike-Share: Udacity Python for Data Science Programming 

## Overview
This project analyzes the usage patterns of bikeshare services in **Chicago**, **New York City**, and **Washington**.  
Using Python, it uncovers trends in bike usage, identifies popular stations, examines trip durations, and provides user statistics.

---

## Project Features

### Data Loading and Filtering
- Users can filter data by city, month (January to June), and day of the week.
- Invalid inputs are efficiently handled to ensure smooth user interaction.

### Usage Statistics
- Analyze the most frequently used months, days, and hours.
- Identify the most popular start and end stations and frequent trip routes.

### Trip Duration Analysis
- Calculate total travel time, average travel time, and minimum travel time.
- Display results in a clear, human-readable format.

### User Statistics
- Provide distributions of user types (e.g., Subscribers vs. Customers).
- Display gender distribution and birth year statistics (if available).

### Text-Based Graphs
- Visualize bike usage trends by month and day using text-based bar graphs.

### Raw Data Display Feature
5-Row Raw Data Output: Displays raw data in increments of 5 rows upon user request.
After displaying 5 rows, the user is prompted to see more data. If the user inputs yes, the next 5 rows are displayed.
If the user inputs no or there is no more data to display, the process stops.
Users can view raw data after applying filters to the dataset, providing detailed insights when desired.

---

## How to Run the Project

### Required Software
- Python 3.x
- Libraries: pandas, numpy, time

---

## Dataset
This project uses public bikeshare system data provided by **Motivate**.  
The dataset includes the following columns:

- Start Time, End Time: The start and end times of trips  
- Trip Duration: Duration of trips in seconds  
- Start Station, End Station: Names of the start and end stations  
- User Type: Type of user (Subscriber or Customer)  
- Gender, Birth Year: Gender and birth year (not available in all datasets)



