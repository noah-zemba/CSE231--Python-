import csv
from datetime import datetime
from operator import itemgetter

COLUMNS = ["date",  "average temp", "high temp", "low temp", "precipitation", \
           "snow", "snow depth"]

TOL = 0.02

BANNER = 'This program will take in csv files with weather data and compare \
the sets.\nThe data is available for high, low, and average temperatures,\
\nprecipitation, and snow and snow depth.'    


MENU = '''
        Menu Options:
        1. Highest value for a specific column for all cities
        2. Lowest value for a specific column for all cities
        3. Average value for a specific column for all cities
        4. Modes for a specific column for all cities
        5. Summary Statistics for a specific column for a specific city
        6. High and low averages for each category across all data
        7. Quit
        Menu Choice: '''
        
      
        
def open_files():
    ''' Open files prompts for names of cities seperated by commas
    and converts them to a list before checking if it is possible
    to open a csv file using each city name.'''
    city_name = input("Enter cities names: ")
    city_list = city_name.split(",")
    fp_list = []
    fp_name_list = []
    # Each city
    for city in city_list:
        try:
            # Adds the ".csv" so it can be opened
            file_name = city + ".csv"
            # Attempt to open .csv file
            csv_file = open(file_name, "r", encoding="utf-8")
            # Adds the city name and the file pointer to the 
            # respective lists
            fp_name_list.append(city)
            fp_list.append(csv_file)
        except:
            # This means that the user either misspelled the name or
            # the .csv doesn't exist
            print("\nError: File {} is not found".format(file_name))
    return fp_name_list, fp_list
def read_files(cities_fp):
    ''' From a list of file pointers, the function adds
    each line from each .csv file to a list after converting 
    to tuples. Each .csv has their own list that is then 
    appended to  list that holds every list from each .csv file.'''
    return_list = []
    # For each .csv
    for fp in cities_fp:
        # Skips both headers
        fp.readline()
        fp.readline() 
        # This is emptied every time a new file is being looped through
        new_list = []
        # For each line (list) in the current file
        for line in csv.reader(fp):
            count = 0
            # Checks that each index isn't an empty string
            # and then tries to convert it to a float
            while count < 7:
                # Changes the value of the index from  "" to None
                if line[count] == "":
                    line[count] = None
                # Tries to convert to float, will skip the date string and 
                # any indexes containing None
                try:
                    line[count] = float(line[count])
                except:
                    pass
                count+=1
            # Creates tuple full of all necessary and converted to float info.
            # The tuple is reinitalized every time through
            new_tuple = (line[0],line[1],line[2],line[3],line[4],line[5],line[6])
            # Appends the tuple to the list for each file
            new_list.append(new_tuple)
        # Appends the list of for the current file to the final list
        return_list.append(new_list)
    return return_list
def get_data_in_range(master_list, start_str, end_str):
    ''' Filters the master_list to only include tuples
    that are within the specified date range (inclusive).'''
    start_date = datetime.strptime(start_str, "%m/%d/%Y").date()
    end_date = datetime.strptime(end_str, "%m/%d/%Y").date()
    return_list = []
    # big_list is the list for each file pointer
    for big_list in master_list:
        # Creates a new empty list for each file list
        new_list = []
        # individual_list is each list in the large file list
        for individual_list in big_list:
            # Converts the date to a useable type? Not sure what data
            # type to call it, but it allows it to be compared with other dates
            # with math operators
            date = datetime.strptime(individual_list[0], "%m/%d/%Y").date()
            # If date is in range of the provided start and end date (both inclusive)
            if start_date <= date <= end_date:
                new_list.append(individual_list)
        return_list.append(new_list)
    return return_list
def get_min(col, data, cities): 
    ''' Using the col as an index, get_min loops
    through the data and finds the minimum value
    of the column for each city.'''
    return_list = []
    all_values_none = True
    # Used to track index of city names
    count = 0
    # Data for each city in master list
    for list_of_tuples in data:
        minimum = 100000
        # For each tuple in each cities list of tuples
        for tuples in list_of_tuples:
            # As long as the value at the index of the column isn't None
            # and if the value is smaller than the current min
            if tuples[col] != None and tuples[col] < minimum:
                all_values_none = False
                # The new minimum is the value of the column
                minimum = tuples[col]
                # Creates and adds name and min value to tuple
                new_tuple = (cities[count], round(minimum,2))
        count+=1
        if all_values_none == False:
            return_list.append(new_tuple)
    return return_list     
def get_max(col, data, cities): 
    ''' Using the col as an index, get_min loops
    through the data and finds the maximum value
    of the column for each city.'''
    return_list = []
    # Used to track index of city namesv
    count = 0
    # While working on the main I got errors that occured when 
    # all the values were None, because the new_tuple var 
    # wouldn't be initialized if that was the case. To 
    # circumvent this I made this boolean that would only
    # add the tuple to the return list if there were some
    # values that weren't None
    all_values_none = True
    # For each tuple in each cities list of tuples
    for list_of_tuples in data:
        maximum = 0
        # For each tuple in each cities list of tuples
        for tuples in list_of_tuples:
            # As long as the value at the index of the column isn't None
            # and if the value is larger than the current max
            if tuples[col] != None and tuples[col] > maximum:
                all_values_none = False
                # The new maximum is the value of the column
                maximum = tuples[col]
                # Creates and adds name and max value to tuple
                new_tuple = (cities[count], round(maximum,2))
        count+=1
        if all_values_none == False:
            return_list.append(new_tuple)
    return return_list
def get_average(col, data, cities): 
    ''' Docstring'''
    return_list = []
    # Used to track index of city namesv
    count = 0
    # For each tuple in each cities list of tuples
    for list_of_tuples in data:
        sum_of_col = 0.0
        # For each tuple in each cities list of tuples
        counter = 0
        for tuples in list_of_tuples:
            # As long as the value at the index of the column isn't None
            # and if the value is larger than the current max
            if tuples[col] != None:
                counter+=1
                # The new maximum is the value of the column
                sum_of_col += float(tuples[col])
            if sum_of_col != 0:
                avg = sum_of_col/counter
                avg = round(avg,2)
            else:
                avg = 0.0
            # Creates and adds name and max value to tuple
            new_tuple = (cities[count], avg)
        count+=1
        return_list.append(new_tuple)
    return return_list
def get_modes(col, data, cities):
    '''get_modes finds streaks within the defined column
    of the data. The function loops through and tracks how 
    many values are within a certain range of eachother 
    in a row, and returns any values with streaks over one.'''
    return_list = []
    # Will hold the values of the specified column
    col_list = []
    # Used as an index for city names
    city_count = 0
    
    # list_o_tupples is the data for each city within the master list
    for list_of_tuples in data:
        # Each tuple corresponds to a date and the related temperature info
        for tuples in list_of_tuples:
            # Ensures the item to be appended is not None (meaning it has to be a float)
            if tuples[col] != None:
                col_list.append(tuples[col])
            # Puts list in ascending order 
            col_list = sorted(col_list,reverse = False)
        # The return list that will contain tuples of streaks
        list_of_streaks = []
        # Appends a very large number that will not ever be counted as
        # a streak later. This is necessary to avoid an inxed out of bounds error
        col_list.append(10000000000000000000)        
        streak = 0
        # Used to track column index
        index = 0
        # Used to keep track of while loop
        count = 0
        # Will be used to put the column values in a list
        index_list = []
        is_streak = False
        # This will help me catch the case in which there are no streaks over 1
        streak_count = 0
        while count < len(col_list):
            try:
                # This starts a new streak and creates a variable that stores 
                # the "representative of the streak"
                if is_streak == False:
                    initial_index = col_list[index]  
                    streak+=1  
                # First part of if statement ensures that no float div by zero errors occur.
                # Second part calculates the condition and compares it to the tolerance
                if initial_index != 0 and abs((initial_index-col_list[index+1])/initial_index) <= TOL:
                    is_streak = True
                    streak +=1
                else:
                    # We don't want streaks of one or else every value would be considered a streak
                    if streak >  1:
                        tuple_streak = (initial_index,streak)
                        list_of_streaks.append(tuple_streak)
                        streak_count+=1
                    # Reset streak
                    streak = 0
                    is_streak = False
                index+=1 
            except:
                pass    
            count+=1
        # If there are no modes then the list of modes for that city is empty and the streak is 1
        if streak_count == 0:
            city = cities[city_count]
            empty_list = []
            # Appends the city name, [the repeated value], and the streak number
            return_list.append((city,empty_list,streak))
        else:
            list_of_reps = []
            max_streak = max(list_of_streaks,key = itemgetter(1))
            for tuples in list_of_streaks:
                if tuples[1] == max_streak[1]:
                    list_of_reps.append(tuples[0])
            return_list.append((cities[city_count],list_of_reps,max_streak[1]))
        # Moves city list index along
        city_count+=1
        # Clears all the data for the current city after it has all been looped through
        col_list.clear()
    return return_list        
def high_low_averages(data, cities, categories):
    ''' Loops through data for cities in multiple categories
    and returns the highest and lowest average in each category.'''
    # Tracks position in the list of cities
    city_index = 0
    column_indexes = []
    # Will be an unfilterd list of all averages
    list_of_averages = []
    # Will be the filtered and returned list of averages
    high_low_list = []
    # For each category in the list of categories
    for category in categories:
        # If that catoegory is in the list of column names
        if category.lower() in COLUMNS:
            category = category.lower()
            # Append the index of the column in the COLUMNS list
            column_indexes.append(COLUMNS.index(category))
        # If the category isnt in the list then append None
        else:
            column_indexes.append(None)
    # For each column we are interested in
    for indexes in column_indexes:
        # If it is none then append none to the list of averages
        if indexes == None:
            list_of_averages.append(None)
        # If not then call list of averages using the colums number at the current index
        else:
            list_of_averages.append(get_average(indexes,data,cities))
    # Since there are lists for each city we need to loop 
    # through each list for each city
    for individual_list in list_of_averages:
        # If the list isn't none
        if individual_list != None:
            maximum = 0
            minimum = 1000
            # Checking if the first index of item (the average)
            # is a min or max by comparing it to previous mins
            # and maxs
            for item in individual_list:
                if item[1] > maximum:
                    maximum = item[1]
                    max_tuple = item
                if item[1] < minimum:
                    minimum = item[1]
                    min_tuple = item
            # Appends a list containing the min and max
            high_low_list.append([min_tuple,max_tuple])
        # If the value of the list at the index was None then append None
        else:
            high_low_list.append(None)
    return high_low_list
def display_statistics(col,data, cities):
    ''' Gets values form calling all needed functions.'''
    min_return_values = get_min(col,data, cities)
    max_return_values = get_max(col,data, cities)
    avg_return_values = get_average(col,data, cities)
    mode_return_values = get_modes(col,data,cities)
    count = 0
    # For each city
    for city in cities:
        print("\t{}: ".format(city))
        # Gets value fo indexes based off counts
        print("\tMin: {:.2f} Max: {:.2f} Avg: {:.2f}".format(min_return_values[count][1],max_return_values[count][1],avg_return_values[count][1]))
        str_value = ""
        # Changes list values to strings
        for value in mode_return_values[count][1]:
            str_value += str(value)
        # If the streak isn't over one it prints No modes, if not it prints all modes info
        if mode_return_values[count][2] != 1:
            print("\tMost common repeated values ({:d} occurrences): {:s}\n".format(mode_return_values[count][2],str_value))
        else:
            print("\tNo modes.")
        count+=1
             
def main():
    print(BANNER)
    files = open_files()
    master_list = read_files(files[1])
    user_input = int(input(MENU))
    valid_input = False
    while user_input != 7:
        start_date = input("\nEnter a starting date (in mm/dd/yyyy format): ")
        end_date = input("\nEnter an ending date (in mm/dd/yyyy format): ")
        data = get_data_in_range(master_list, start_date, end_date)
        column_index = []   
        if user_input in range(1,7) and user_input != 6:
            valid_input = False
            while valid_input == False:
                desired_category = input("\nEnter desired category: ")
                desired_category = desired_category.lower()
                if desired_category in COLUMNS:
                    # Append the index of the column in the COLUMNS list
                    column_index.append(COLUMNS.index(desired_category))
                    valid_input = True
                else:
                    print("\n\t{} category is not found.".format(desired_category))
            print("\n\t{}: ".format(desired_category))
        cities = files[0]
        if user_input == 1:
            for value in column_index:
                print_values = get_max(value,data,cities)
                for tuples in print_values:
                    print("\tMax for {:s}: {:.2f}".format(tuples[0],tuples[1]))
            user_input = int(input(MENU))
        elif user_input == 2:
            for value in column_index:
                print_values = get_min(value,data,cities)
                for tuples in print_values:
                    print("\tMin for {:s}: {:.2f}".format(tuples[0],tuples[1]))
            user_input = int(input(MENU))   
        elif user_input == 3:
            for value in column_index:
                print_values = get_average(value,data,cities)
                for tuples in print_values:
                    print("\tAverage for {:s}: {:.2f}".format(tuples[0],tuples[1]))
            user_input = int(input(MENU))  
        elif user_input == 4:
            value = column_index[0]
            largest_streak_tuple = (get_modes(value,data,cities))
            for tuples in largest_streak_tuple:
                str_value = ""
                for value in tuples[1]:
                    str_value += str(value)
                print("\tMost common repeated values for {:s} ({:d} occurrences): {:s}\n".format(tuples[0],tuples[2],str_value))
            
            user_input = int(input(MENU)) 
        elif user_input == 5:
            display_statistics(column_index[0],data,cities)
            user_input = int(input(MENU)) 
        elif user_input == 6:
            categories = input("\nEnter desired categories seperated by comma: ")
            category_list = categories.split(",")
            print("\nHigh and low averages for each category across all data.")
            high_low_average_values = high_low_averages(data,cities,category_list)
            count = 0
            for value in high_low_average_values:
                if value is None:
                     print("\n\t{} category is not found.".format(category_list[count].lower()))
                else:
                    print("\n\t{}: ".format(category_list[count].lower()))
                    print("\tLowest Average: {:s} = {:.2f} Highest Average: {:s} = {:.2f}".format(value[0][0],value[0][1],value[1][0],value[1][1]))
                count+=1
            user_input = int(input(MENU))    

    else:
        print("\nThank you using this program!")


    

#DO NOT CHANGE THE FOLLOWING TWO LINES OR ADD TO THEM
#ALL USER INTERACTIONS SHOULD BE IMPLEMENTED IN THE MAIN FUNCTION
if __name__ == "__main__":
    main()
                                           
