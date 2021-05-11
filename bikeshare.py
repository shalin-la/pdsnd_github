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
    #gets user input for city (chicago, new york city, washington).
    while True:
    # gets user input for city (chicago, new york city, washington).
        city = input("Please choose a city from Chicago, Washington or New York: ").strip()
        if city.lower() == 'chicago':
            city = 'chicago'
        elif city.lower() == 'new york':
            city = 'new york city'
        elif city.lower() == 'washington':
            city = 'washington'
        else:
            print('Sorry that is not a valid input! Please try again!')
            break

        # gets user input for month (all, january, february, ... , june)
        filter1 = input("Do you want to filter by a month? Type:(yes/no)")
        if filter1.lower() == 'yes':
            month = input("Please select a month from January, February, March, April, May or June?").title()
            if month not in ['January','February','March', 'April', 'May', 'June']:
                print('Sorry that is not a valid input! Please try again!')
                break
        elif filter1.lower() == 'no':
            month = 'all'
        else:
            print('Sorry that is not a valid input! Please try again!')
            break

        # gets user input for day of week (all, monday, tuesday, ... sunday)
        filter2 = input("Do you want to filter by a day? Type:(yes/no)")
        if filter2.lower() == 'yes':
            day = input("Please select a day from Sunday to Saturday: ").title()
            if day not in ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']:
                print('Sorry that is not a valid input! Please try again!')
                break
        elif filter2.lower() == 'no':
            day = 'all'
        else:
            print('Sorry that is not a valid input! Please try again!')
            break

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
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time and End Time columns to datetime
    df['Start Time'] =pd.to_datetime(df['Start Time'])
    df['End Time'] =pd.to_datetime(df['End Time'])

    # extract month and day of week from Start Time to create new columns
    df['s_hour'] = df['Start Time'].dt.hour
    df['e_hour'] = df['End Time'].dt.hour
    df['month'] = df['Start Time'].dt.month_name()
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['day_of_month'] = df['Start Time'].dt.day


    # filter by month if applicable
    if month != 'all':
        df = df[df['month'] == month]                   # filter by month to create the new dataframe

    # filter by day of week if applicable
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]       # filter by day of week to create the new dataframe

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()


    month_mode = df['month'].mode()[0]                 # Display the most common month
    df['day_of_week'] = df['Start Time'].dt.day_name() # Display the most common day of week
    day_mode = df['day_of_week'].mode()[0]
    s_hour_mode = df['s_hour'].mode()[0]                # Display the most common start hour
    e_hour_mode = df['e_hour'].mode()[0]                # Display the most common end hour
    dom_mode = df['day_of_month'].mode()[0]             # Display the most day of the month

    print("Statistics on times of travel")
    print('Most Frequent start hour is:', s_hour_mode)
    print('Most Frequent return hour is:', e_hour_mode)
    print('Most popular month is:', month_mode)
    print('Most popular day is:', day_mode)
    print('Most Frequent day of month is:', dom_mode)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('_'*50)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()


    s_station_mode = df['Start Station'].mode()[0]      # Display most commonly used start station
    e_station_mode = df['End Station'].mode()[0]        # Display most commonly used end station

    # Dsplay most frequent combination of start station and end station trip
    route_mode = (df['Start Station'] + ' to ' + df['End Station']).mode()[0]

    print("Statistics on location of stations")
    print('Most popular start station is: ', s_station_mode)
    print('Most popular end station is: ', e_station_mode)
    print('Most popular route is from: ', route_mode)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('_'*50)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()


    trip_total = df['Trip Duration'].sum()          # Display total travel time
    trip_mean = df['Trip Duration'].mean()          # Display mean travel time

    print("Statistics on trip durations")
    print('Total trip hours: {} hours'.format(trip_total/(60*60)))
    print('Average duration of a trip is: {} in minutes'.format(trip_mean/60))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('_'*50)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    cust_num = len(df[df['User Type'] == 'Customer'])
    sub_num = len(df[df['User Type'] == 'Subscriber'])
    dep_num = len(df[df['User Type'] == 'Dependent']) # Chicago ONLY!!
    unspec_num = len(df[df['User Type'].isna()]) # New York ONLY!




    if city != 'washington':

        """ Not for washington """
        # Display counts of gender
        male_count = len(df[df['Gender'] == 'Male'])
        female_count = len(df[df['Gender'] == 'Female'])
        undisc_count = df.shape[0] - (male_count + female_count)

        # Display earliest, most recent, and most common year of birth
        """ Not for washington """

        earliest_year = df['Birth Year'].min()
        most_recent_year = df['Birth Year'].max()
        popular_birth_year = df['Birth Year'].mode()[0]

        print("Statistics on bikeshare users")
        print('Number of customers:',cust_num)
        print('Number of subscribers:',sub_num)
        print('Number of Dependents:',dep_num)
        print('Number of unspecified user:',unspec_num,'\n')
        print('-'*20)
        print("Statistics on the gender of bikeshare users")
        print('Number of males:', male_count)
        print('Number of females:', female_count)
        print('Undisclosed gender', undisc_count,'\n')
        print('-'*20)
        print("Statistics on the age of bikeshare users")
        print('The oldest user was born in:', earliest_year)
        print('The youngest user was born in:', most_recent_year)
        print('The most year that bikeshare users were born in:',popular_birth_year)
    else:
        print("Statistics on bikeshare users")
        print('Number of customers:',cust_num)
        print('Number of subscribers:',sub_num)
        print('Number of Dependents:',dep_num)
        print('Number of unspecified user:',unspec_num,'\n')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('_'*50)

def raw_data(df):
    """ Raw data is displayed upon request by users
    Requested in rubric that 5 lines of raw data to be displayyed
    """
    idx = 0

    print('Would you like to see 5 rows of raw data used to derive statistics?')
    data_iter = input('Please type (yes/no):')
    while True:
        if data_iter.lower() =='no':
            return
        elif data_iter.lower() =='yes':
            print(df[idx:idx + 5])
            idx += 5
        data_iter = input('\n Would you like to see five more rows? Please type (yes/no):')

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
