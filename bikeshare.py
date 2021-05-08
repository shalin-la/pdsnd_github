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
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
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

        # TO DO: get user input for month (all, january, february, ... , june)
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

        # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
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
        # use the index of the months list to get the corresponding int
        #months = ['january', 'february', 'march', 'april', 'may', 'june']
        # month = months.index(month) + 1

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
    month_mode = df['month'].mode()[0]

    # TO DO: display the most common day of week
    df['day_of_week'] = df['Start Time'].dt.day_name()
    day_mode = df['day_of_week'].mode()[0]

    # TO DO: display the most common start hour
    s_hour_mode = df['s_hour'].mode()[0]

    # TO DO: display the most common end hour
    e_hour_mode = df['e_hour'].mode()[0]

    # TO DO: display the most day of the month
    dom_mode = df['day_of_month'].mode()[0]

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

    # TO DO: display most commonly used start station
    s_station_mode = df['Start Station'].mode()[0]

    # TO DO: display most commonly used end station
    e_station_mode = df['End Station'].mode()[0]

    # TO DO: display most frequent combination of start station and end station trip
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

    # TO DO: display total travel time
    trip_total = df['Trip Duration'].sum()

    # TO DO: display mean travel time
    trip_mean = df['Trip Duration'].mean()

    print("Statistics on trip durations")
    print('Total trip hours: {} hours'.format(trip_total/(60*60)))
    print('Average duration of a trip is: {} in minutes'.format(trip_mean/60))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('_'*50)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    """ The info on uer types will be common to all cities, so seperated from the if statement"""

    # TO DO: Display counts of user types
    cust_num = len(df[df['User Type'] == 'Customer'])
    sub_num = len(df[df['User Type'] == 'Subscriber'])
    dep_num = len(df[df['User Type'] == 'Dependent']) # Chicago ONLY!!
    unspec_num = len(df[df['User Type'].isna()]) # New York ONLY!


    """ Seperating Washington from if statement as it does not have user gender or age """

    if city != 'washington':
        # TO DO: Display counts of gender
        """ Not for washington """

        male_count = len(df[df['Gender'] == 'Male'])
        female_count = len(df[df['Gender'] == 'Female'])
        undisc_count = df.shape[0] - (male_count + female_count)

        # TO DO: Display earliest, most recent, and most common year of birth
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


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
