import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

"""
HOW TO: User runs Udacity Python Project.py in command. Code will prompt user to provide a 
number of inputs (described below). User will have option to filter by city, month, and day
of week. The user will also have the option to view raw data by lines of 5. 

"""


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')       
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
   
    correct_city = 'no'
    while correct_city == 'no':
        city = str(input('Which city would you like to view? Select from: '\
	    'Chicago, New York City, or Washington \n')).lower()
    
        try: 
            pd.read_csv(CITY_DATA[city])
            print('You selected ', city.title())    
            correct_city = input('Is this correct? (yes/no):').lower()
        except:
            print('Oops! It looks like that city name wasn\'t entered correctly. Please try again.')
              
    correct_month = 'no'
    while correct_month == 'no':
        month = str(input('Would you like to filter by month? Please enter the full name of the month \
(e.g. January). \n Type "all" to see data from all months.\n')).lower()
        month_list = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
        if month not in month_list:
            print('Oops! It looks like that month name wasn\'t entered correctly. Please try again. Remember to use the full month name.')

        else:    
            print('Great, filtering on', month.title())
            correct_month = 'yes'
    
    correct_day = 'no'
    while correct_day == 'no':        
        day = str(input('Now, select the day of week you would like to view (e.g. Monday, Tuesday, etc.) \
Type "all" to see data from all days of the week.\n')).lower()
    
        day_list = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']
        if day not in day_list:
            print('Oops! It looks like that day name wasn\'t entered correctly. Please try again. Remember to use the full day name.')

        else:    
            print('Great, filtering on', day.title())
            correct_day = 'yes'
        
        
    print('-'*40)
    return city, month, day

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])

    print('Hello! Let\'s explore some US bikeshare data!')
    five_request = input('First, would you like to see the raw data? (yes/no) \n').lower()
    counter_start = 0
    counter_end = 5
    while five_request == 'yes':
        print(df[counter_start:counter_end])
        counter_start += 5 
        counter_end += 5
        five_request = input('Would you like to see 5 more rows of data? (yes/no) \n').lower()
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])

    df['month'] = pd.DatetimeIndex(df['Start Time']).month
    df['day_of_week'] = pd.DatetimeIndex(df['Start Time']).weekday_name
    df['hour'] = pd.DatetimeIndex(df['Start Time']).hour
    
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
        
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month

    count_months = df['month'].value_counts
    popular_month = df.mode()['month'][0]
    popular_month_dt = pd.to_datetime(popular_month)

    #convert month to month name for readability 
    print('The most popular month is:', popular_month_dt.strftime("%B")) 
    
    # TO DO: display the most common day of week
    count_days = df['day_of_week'].value_counts()
    popular_day = df.mode()['day_of_week'][0] 
    
    print('The most popular day of week is:' ,popular_day) 

    # TO DO: display the most common start hour
    popular_hour = df.mode() ['hour'] [0]
    print('Most Frequent Start Hour:', popular_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station

    popular_start = df.mode() ['Start Station'] [0]
    print('The most popular start station is: ', popular_start)

    # TO DO: display most commonly used end station
    popular_end = df.mode() ['End Station'] [0]
    print('The most popular end station is: ', popular_end)

    # TO DO: display most frequent combination of start station and end station trip
    df['start_end_combo'] = df['Start Station'] + df['End Station']
    popular_start_end = df.mode() ['start_end_combo'] [0]
    print('The most popular combination of start and end stations is: ', popular_start_end)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    df['trip_time'] = df['End Time'] - df['Start Time']
    total_travel_time = df['trip_time'].sum()
    print('The total travel time in this dataset is ', total_travel_time)

    # TO DO: display mean travel time
    
    mean_travel_time = df['trip_time'].mean()
    print('The mean travel time in this dataset is ', mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df.groupby('User Type')['User Type'].count()
    print('Bikeshare users make up the following user types: ', user_types)

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        gender_counts = df.groupby('Gender')['Gender'].count()
        print('Bikeshare users make up the following genders: ', gender_counts)
    else:
        print('Gender data is not avaialble in Washington.')

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        earliest_birthyear = df['Birth Year'].min()
        print('The earliest birth year is: ', int(earliest_birthyear))
        
        recent_birthyear = df['Birth Year'].max()
        print('The most recent birth year is: ', int(recent_birthyear))
        
        common_birthyear = df['Birth Year'].mode()
        print('The most common birth year is: ', int(common_birthyear)) 
    
    else:
        print('Birth year data is not available in Washington.')
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
