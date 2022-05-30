#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import time

import pandas as pd

import numpy as np





sCITY_DATA = { 'chicago': r'/Users/keeratkaur/Downloads/all-project-files/chicago.csv', 'Chicago': r'/Users/keeratkaur/Downloads/all-project-files/chicago.csv',
             'New York City': r'/Users/keeratkaur/Downloads/all-project-files/new_york_city.csv', 'New york city': r'/Users/keeratkaur/Downloads/all-project-files/new_york_city.csv',
              'new york city': r'/Users/keeratkaur/Downloads/all-project-files/new_york_city.csv', 'washington': r'/Users/keeratkaur/Downloads/all-project-files/washington.csv',
             'Washington': r'/Users/keeratkaur/Downloads/all-project-files/washington.csv' }

""" providing path to all data file saved on my local drive"""



#Function to figure out the filtering requirements of the user
def get_filters():
    """
    Asks user to specify a city, month, and day.
    Args:
        None.
    Returns:
        str (city): city name 
        str (month): name of the month 
        str (day): name of the day of week
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    #Initializing an empty city variable to store city choice from user
    #You will see this repeat throughout the program
    scity = ''

    while scity not in sCITY_DATA.keys():
        print("\nWelcome. Please choose your city:")
        print("\n1. Chicago 2. New York City 3. Washington")
       
        
        scity = input().lower()

        if scity not in sCITY_DATA.keys():
            print("\nPlease check your input, it's a invalid format.")
            print("\nRestarting...")

    print(f"\nYou have chosen {scity.title()} as your city.")


    sMONTH_DATA = {'january': 1, 'february': 2, 'march': 3, 'april': 4, 'may': 5, 'june': 6, 'all': 7}
    smonth = ''
    while smonth not in sMONTH_DATA.keys():
        print("\nPlease enter the month:")
        print("\nAccepted input:\nFull month name; not case sensitive (e.g. may or May).\nFull month name (e.g. May).")
    
        smonth = input().lower()

        if smonth not in sMONTH_DATA.keys():
            print("\nInvalid input. Please try again.")
            print("\nRestarting...")

    print(f"\nYou have chosen {smonth.title()} as your month.")

    
    sDAY_LIST = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    sday = ''
    while sday not in sDAY_LIST:
        print("\nPlease enter a day in the week of your choice for which you're seeking the data:")
        print("\nAccepted input:\nDay name; not case sensitive (e.g. friday or FRIDAY).\nDay name  (e.g. Friday).")
        
        sday = input().lower()

        if sday not in sDAY_LIST:
            print("\nInvalid input. Please try again in one of the accepted input formats.")
            print("\nRestarting...")

    print(f"\nYou have chosen {sday.title()} as your day.")
    print(f"\nYou have chosen to view data for city: {scity.upper()}, month/s: {smonth.upper()} and day/s: {sday.upper()}.")
    print('-'*80)
    #Returning all selections
    return scity, smonth, sday

#Function to load data from .csv files
def load_data(scity, smonth, sday):
    """
    Loads data for the specified city and filters by month and day if applicable.
    Args:
        tarun1 (str): name of the city
        tarun2 (str): name of the month 
        tarun3 (str): name of the day of week 
    Returns:
        df: Pandas DataFrame containing city data filtered by month and day
    """
    #Load data for city
    print("\nLoading data...")
    df = pd.read_csv(sCITY_DATA[scity])

    df['Start Time'] = pd.to_datetime(df['Start Time'])

    #Extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    #df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['day_of_week'] = df['Start Time'].dt.day_name()

    #Filter by month 
    if smonth != 'all':
        #Use the index of the months list
        smonths = ['january', 'february', 'march', 'april', 'may', 'june']
        smonth = smonths.index(smonth) + 1

        #Filter by month to create the new dataframe
        df = df[df['month'] == smonth]
       

    #Filter by day of week
    if sday != 'all':
        #Filter by day of week
        df = df[df['day_of_week'] == sday.title()]
        

    #Returns the selected file as a dataframe (df) with relevant columns
    return df

#Function to compute all the time-related statistics 
def time_stats(df):
    """Displays statistics on the most frequent times of travel.
    Args:
        tarun1 (df): The data frame you wish to work with.
    Returns:
        None.
    """

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    #Uses mode method to find the most popular month
    popular_month = df['month'].mode()[0]

    print(f"Most Popular Month (1 = January,...,6 = June): {popular_month}")

    #Uses mode method to find the most popular day
    popular_day = df['day_of_week'].mode()[0]

    print(f"\nMost Popular Day: {popular_day}")

    #Extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour

    #Uses mode method to find the most popular hour
    popular_hour = df['hour'].mode()[0]

    print(f"\nMost Popular Start Hour: {popular_hour}")
    print(f"\nThis took {(time.time() - start_time)} seconds.")
    print('-'*80)

#Function to calculate station related statistics
def station_stats(df):
    """Displays statistics on the most popular stations and trip.
    Args:
        tarun1 (df): The data frame you wish to work with.
    Returns:
        None.
    """

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    
    common_start_station = df['Start Station'].mode()[0]

    print(f"The most commonly used start station: {common_start_station}")

    
    common_end_station = df['End Station'].mode()[0]

    print(f"\nThe most commonly used end station: {common_end_station}")

    
    df['Start To End'] = df['Start Station'].str.cat(df['End Station'], sep=' to ')
    combo = df['Start To End'].mode()[0]

    print(f"\nThe most frequent combination of trips are from {combo}.")

    print(f"\nThis took {(time.time() - start_time)} seconds.")
    print('-'*80)

#Function for trip duration related statistics
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration.
    Args:
        tarun1 (df): The data frame you wish to work with.
    Returns:
        None.
    """

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()


    total_duration = df['Trip Duration'].sum()
    """ creating the new variable to compute the stats for the total trip duration for each rental"""
   
    minute, second = divmod(total_duration, 60)
   
    hour, minute = divmod(minute, 60)
    print(f"The total trip duration is {hour} hours, {minute} minutes and {second} seconds.")

    
    average_duration = round(df['Trip Duration'].mean())
    
    mins, sec = divmod(average_duration, 60)
    #This filter prints the time in hours, mins, sec format if the mins exceed 60
    if mins > 60:
        hrs, mins = divmod(mins, 60)
        print(f"\nThe average trip duration is {hrs} hours, {mins} minutes and {sec} seconds.")
    else:
        print(f"\nThe average trip duration is {mins} minutes and {sec} seconds.")

    print(f"\nThis took {(time.time() - start_time)} seconds.")
    print('-'*80)

#Function to calculate user statistics
def user_stats(df):
    """Displays statistics on bikeshare users.
    Args:
        tarun1 (df): The data frame you wish to work with.
    Returns:
        None.
    """

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    #The total users are counted using value_counts method
    #They are then displayed by their types (e.g. Subscriber or Customer)
    user_type = df['User Type'].value_counts()

    print(f"The types of users by number are given below:\n\n{user_type}")

    #This try clause is implemented to display the numebr of users by Gender
    #However, not every df may have the Gender column, hence this...
    try:
        gender = df['Gender'].value_counts()
        print(f"\nThe types of users by gender are given below:\n\n{gender}")
    except:
        print("\nThere is no 'Gender' column in this file.")

    
    try:
        earliest = int(df['Birth Year'].min())
        recent = int(df['Birth Year'].max())
        common_year = int(df['Birth Year'].mode()[0])
        print(f"\nThe earliest year of birth: {earliest}\n\nThe most recent year of birth: {recent}\n\nThe most common year of birth: {common_year}")
    except:
        print("There are no birth year details in this file.")

    print(f"\nThis took {(time.time() - start_time)} seconds.")
    print('-'*80)

#Function to display the data frame itself as per user request
def display_data(df):
    """Displays 5 rows of data from the csv file for the selected city.
    Args:
        tarun1 (df): The data frame you wish to work with.
    Returns:
        None.
    """
    BIN_RESPONSE_LIST = ['yes', 'no']
    rdata = ''
    #counter variable is initialized as a tag to ensure only details from
    #a particular point is displayed
    counter = 0
    while rdata not in BIN_RESPONSE_LIST:
        print("\nDo you wish to view the raw data?")
        print("\nAccepted responses:\nYes or yes\nNo or no")
        rdata = input().lower()
        #the raw data df is displayed
        if rdata == "yes":
            print(df.head())
        elif rdata not in BIN_RESPONSE_LIST:
            print("\nPlease check your input.")
            print("Input does not seem to match any of the accepted responses.")
            print("\nRestarting...\n")

    #Extra while loop here to ask user if they want to continue viewing data
    while rdata == 'yes':
        print("Do you wish to view more raw data?")
        counter += 5
        rdata = input().lower()
        #If user opts for it, this displays next 5 rows of data
        if rdata == "yes":
             print(df[counter:counter+5])
        elif rdata != "yes":
             break

    print('-'*80)

#Main function to call all the previous functions
def main():
    while True:
        scity, smonth, sday = get_filters()
        df = load_data(scity, smonth, sday)

        display_data(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
    main()


# In[ ]:




