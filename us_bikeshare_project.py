import time
import pandas as pd
import numpy as np

# City data file paths
CITY_DATA = {
    'chicago': 'chicago.csv',
    'new york city': 'new_york_city.csv',
    'washington': 'washington.csv'
}

def get_filters():
    """
    Asks the user to specify a city, month (as a number), and day (as a number) for analysis.
    Includes error handling for invalid inputs.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by ("all" for no filter)
        (str) day - name of the day to filter by ("all" for no filter)
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    # Get user input for city
    while True:
        city = input("Please select a city to analyze (Chicago, New York City, Washington): ").strip().lower()
        if city in CITY_DATA:
            break
        print("Invalid input. Please try again.")

    # Get user input for month (as a string)
    while True:
        month = input("Please enter the month to analyze\n"
                      "\t(January, February, March, April, May, June) or 'all' for no filter: ").strip().lower()
        if month in ['january', 'february', 'march', 'april', 'may', 'june', 'all']:
            break
        print("Invalid input. Please try again.")

    # Get user input for day (as a string)
    while True:
        day = input("Please enter the day to analyze\n"
                    "\t(Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday) or 'all' for no filter: ").strip().lower()
        if day in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']:
            break
        print("Invalid input. Please try again.")

    print('-' * 40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and applies filters for month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by ("all" for no filter)
        (str) day - name of the day to filter by ("all" for no filter)
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # Load data
    df = pd.read_csv(CITY_DATA[city])

    # Clean Data
    #Columns unnamed = 0  drop
    df.drop(columns='Unnamed: 0', inplace=True)

    # Missing values
    df.fillna(method='ffill', inplace=True)

    # Convert Start Time to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # Extract month and day of week
    df['month'] = df['Start Time'].dt.month_name().str.lower()
    df['day_of_week'] = df['Start Time'].dt.day_name().str.lower()

    # Apply month filter
    if month != 'all':
        df = df[df['month'] == month]

    # Apply day filter
    if day != 'all':
        df = df[df['day_of_week'] == day]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # Display the most common month
    common_month = df['month'].mode()[0]
    print(f"Most common month: {common_month}")

    # Display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print(f"Most common day of week: {common_day}")

    # Display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print(f"Most common start hour: {common_hour} o'clock")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # Display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print(f"Most popular start station: {common_start_station}")

    # Display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print(f"Most popular end station: {common_end_station}")

    # Display most frequent combination of start and end station
    df['station_combination'] = df['Start Station'] + " -> " + df['End Station']
    common_combination = df['station_combination'].mode()[0]
    print(f"Most frequent trip: {common_combination}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)

def format_time(seconds):
    """
    Converts a duration in seconds to hours, minutes, and seconds.

    Args:
        seconds (int or float): Total duration in seconds.
    Returns:
        str: Formatted time as 'X hours, Y minutes, Z seconds'.
    """
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    seconds = int(seconds % 60)
    return f"{hours} hours, {minutes} minutes, {seconds} seconds"

def trip_duration_stats(df):
    """Displays statistics on the total, average, and minimum trip duration."""
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # Calculate total, mean, and minimum trip durations
    total_travel_time = df['Trip Duration'].sum()
    mean_travel_time = df['Trip Duration'].mean()
    min_travel_time = df['Trip Duration'].min()

    # Display results using the format_time function
    print(f"Total travel time: {format_time(total_travel_time)}")
    print(f"Mean travel time: {format_time(mean_travel_time)}")
    print(f"Minimum travel time: {format_time(min_travel_time)}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def user_stats(df):
    """Displays statistics on bikeshare users."""
    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Total entries in the dataset
    total_entries = len(df)

    # Display counts of user types with percentages
    user_types = df['User Type'].value_counts()
    print("User types:")
    for user_type, count in user_types.items():
        percentage = (count / total_entries) * 100
        print(f"  {user_type}: {count} ({percentage:.2f}%)")

    # Display counts of gender with percentages, if available
    if 'Gender' in df:
        genders = df['Gender'].value_counts()
        print("\nGender:")
        for gender, count in genders.items():
            percentage = (count / total_entries) * 100
            print(f"  {gender}: {count} ({percentage:.2f}%)")
    else:
        print("\nGender data not available.")

    # Display earliest, most recent, and most common year of birth, if available
    if 'Birth Year' in df:
        earliest_year = int(df['Birth Year'].min())
        most_recent_year = int(df['Birth Year'].max())
        common_year = int(df['Birth Year'].mode()[0])
        print("\nYear of birth stats:")
        print(f"  Earliest year: {earliest_year}")
        print(f"  Most recent year: {most_recent_year}")
        print(f"  Most common year: {common_year}")
    else:
        print("\nYear of birth data not available.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def text_based_graph(data, title, xlabel):
    """
    Displays a text-based bar graph for the given data.

    Args:
        data (dict): Dictionary where keys are labels and values are counts.
        title (str): The title of the graph.
        xlabel (str): Label for the x-axis.

    Returns:
        None: Prints the text-based graph directly.
    """
    print(f"\n{title}")
    print(f"{xlabel}")
    print("-" * 40)
    
    max_length = 50  # Maximum length of the graph line
    max_value = max(data.values())  # Largest value in the data
    
    for key, value in data.items():
        bar_length = int((value / max_value) * max_length)  # Scale bar length
        bar = '*' * bar_length  # Create bar with '*'
        print(f"{key:<15}: {bar} ({value})")  # Print label, bar, and count

def visualize_usage_by_month_and_day(df):
    """
    Visualizes bike usage by month and day using text-based graphs.

    Args:
        df (DataFrame): The bikeshare data containing 'Start Time' column.

    Returns:
        None: Prints text-based graphs.
    """

    # Extract months and days from 'Start Time'
    df['Month'] = df['Start Time'].dt.month_name()
    df['Day'] = df['Start Time'].dt.day_name()

    # Month usage
    month_counts = df['Month'].value_counts().reindex([
        'January', 'February', 'March', 'April', 'May', 'June'
    ], fill_value=0).to_dict()

    # Day usage
    day_counts = df['Day'].value_counts().reindex([
        'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'
    ], fill_value=0).to_dict()

    # Display text-based graphs
    text_based_graph(month_counts, "Bike Usage by Month", "Month Usage Graph")
    text_based_graph(day_counts, "Bike Usage by Day", "Day Usage Graph")

def raw_data(df):
    """
    Displays 5 rows of raw data at a time upon user request.
    
    Args:
        df (DataFrame): The filtered bikeshare data.
    """
    start_index = 0
    while True:
        # Display 5 rows of data
        print(df.iloc[start_index:start_index + 5])
        start_index += 5
        
        # Check if the user wants to continue
        more_data = input("\nWould you like to see 5 more rows of raw data? Enter yes or no: ").strip().lower()
        if more_data != 'yes' or start_index >= len(df):
            print("\nNo more raw data to display.")
            break

def main():
    """Manages the program execution."""
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        visualize_usage_by_month_and_day(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        # Show raw data
        while True:
            raw_input = input("\nWould you like to see raw data? Enter yes or no: ").strip().lower()
            if raw_input == 'yes':
                raw_data(df)
                break
            elif raw_input == 'no':
                break
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")

        restart = input('\nWould you like to restart? Enter yes or no: ').strip().lower()
        if restart != 'yes':
            break

        restart = input('\nWould you like to restart? Enter yes or no: ').strip().lower()
        if restart != 'yes':
            break

if __name__ == "__main__":
    main()
