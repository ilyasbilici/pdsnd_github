import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    city = input("Please insert the city name: ").lower()

    if city not in ['chicago', 'new york city', 'washington']:
        city = input("Please insert the city name: ").lower()

    # get user input for month (all, january, february, ... , june)

    month = input("Please insert month name: ").lower()
    if month not in ['january','february','march','april','may','june','all']:
        month = input("Please insert month name: ").lower()

    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("Please insert day of week: ").lower()
    if day not in ['monday','tuesday','wednesday','thursday','friday','saturday','sunday','all']:
        day = input("Please insert day name: ").lower()

    print('-' * 40)
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
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    if month in ['january', 'february', 'march', 'april', 'may', 'june']:
        list_month = ['january', 'february', 'march', 'april', 'may', 'june']
        month = list_month.index(month) + 1
        df = df[df['month'] == month]
    else:
       print ('your choise is fail')

    if day in ['monday','tuesday','wednesday','thursday','friday','saturday','sunday']:
        df = df[df['day_of_week'] == day.title()]
    else:
        print ('your choise is fail')

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month


    # display the most common day of week


    # display the most common start hour
    print('the most common month is....:')
    print (df['month'].mode()[0])

    # display the most common day of week
    print('the most common day of week is...:')
    print (df['day_of_week'].mode()[0])

    # display the most common start hour
    df['hour']=df['Start Time'].dt.hour
    print('the most common start hour is...:')
    print(df['hour'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station


    # display most commonly used end station


    # display most frequent combination of start station and end station trip

    print ('the most commonly used start station is....:' )
    print (df['Start Station'].mode()[0])

    print('the most commonly used end station is...:')
    print (df['End Station'].mode()[0])

    df['combination'] = df['Start Station'] + '  ' + df['End Station']
    print('the most most frequent combination of start station and end station trip is... :')
    print (df['combination'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time


    # display mean travel time

    print("The total travel time is:")
    print (df['Trip Duration'].sum())

    print("The mean travel time is: {}")
    print (df['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types


    # Display counts of gender


    # Display earliest, most recent, and most common year of birth
    user_types=df['User Type'].value_counts()
    print(user_types)

    if not 'Gender' in df:
        print("There is no gender information in this city.")
    else:
        print(df['Gender'].value_counts())

    if not 'Birth_Year' in df:
        print("There is no birth year information in this city.")
    else:
        print(df['Birth_Year'].min())
        print(df['Birth_Year'].max())
        print(df['Birth Year'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def user_repeat(df):
    view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n')
    start_loc = 0
    if view_data == 'yes':
        while (True):
            print(df.iloc[start_loc:start_loc+5])
            start_loc += 5
            view_data = input("Do you wish to continue?: ").lower()
            if view_data == 'no':
               break
    if view_data == 'no':
       return
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        user_repeat(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
   main()
