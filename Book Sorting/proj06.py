 ###########################################################

    #  Computer Project #6

    #

    #  Algorithm

    #    Prompted for file name until valid file name is provided

    #    Shown message and menu and promped for input   
    #    This will continue as long as user inputs does not input 4

    #    If user selects 1 they can sort by book name.
    #    User keyword is as a criterion while looping through all titles.
    #    All books with titles matching the keyword are returned
    
    #    If user selects 2 they can sort by 4 differernt criterion.
    #    If valid criterion input is prodived then user is prompted for a value
    #    All books with criterion matching the value are returned

    #    If the user selects 3 books are reccomende using criteria they input
    
    #    If the user selects 4 the program ends

 ###########################################################

import csv
from operator import itemgetter

TITLE = 1
CATEGORY = 3
YEAR = 5
RATING = 6
PAGES = 7

MENU = "\nWelcome to the Book Recommendation Engine\n\
        Choose one of below options:\n\
        1. Find a book with a title\n\
        2. Filter books by a certain criteria\n\
        3. Recommend a book \n\
        4. Quit the program\n\
        Enter option: "

CRITERIA_INPUT = "\nChoose the following criteria\n\
                 (3) Category\n\
                 (5) Year Published\n\
                 (6) Average Rating (or higher) \n\
                 (7) Page Number (within 50 pages) \n\
                 Enter criteria number: "

TITLE_FORMAT = "{:15s} {:35s} {:35s} {:6s} {:8s} {:15s} {:15s}"
TABLE_FORMAT = "{:15s} {:35s} {:35s} {:6s} {:<8.2f} {:<15d} {:<15d}"

def open_file():
    """Prompts for user input and attemps to open
    a file with the same name. Prompts until successful
    and returns the file pointer."""
    count = 0
    file_name = input("Enter file name: ")
    # Ensures the function stops after it opens a file
    while count < 1:
        # If it opens then end the loop
        try:
            csv_file = open(file_name, "r", encoding="utf-8")
            count+=1
        # If it doesn't work the prompt for new input
        except:
            print("\nError opening file. Please try again.")
            file_name = input("Enter file name: ")
    return csv_file

def read_file(fp):
    """Takes each book and categorizes all
    the different aspects of the book into a tuple
    so that each tuple holds all the information about
     a book. That tuple is added to a list of similar 
     tuples and returned."""
    list_of_tuples = []
    for book in csv.reader(fp):
        # Initializes a new empty tuple to hold
        # all the book info every time a new book is
        # iterated(?) on 
        book_tuple = ()
        given_category = (book[5]).lower()
        try: 
            # Tries to add each different peiece of info to the specified slot in the 
            # tuple. If it fails it skips the list entry
            # I used .split() to make the catorgory into a list as per the instructions
            book_tuple = (book[0],book[2],book[4],given_category.split(",")\
            , book[7], book[8],float(book[9]), int(book[10]), int(book[11]))
            list_of_tuples.append(book_tuple) 
        except:
            pass    
    
    return list_of_tuples
    

        

def get_books_by_criterion(list_of_tuples, criterion, value):
    """After user provides an int criterion, this function loops
    through that index of the list_of_tuples and returns any 
    book that matches the user provided value."""
    # Criterion is the index of the book tuple being searched
    # Value is the user input for keyword
    # List of tuples is all the books and their categories of information
    count = 0
    list_of_tuples_return = []
    valid_keyword = False
    # Book is each individual tuple within the list
    for book in list_of_tuples:
        # Checks whch criterion was given
        if criterion == 0 or criterion == 2:
            # This allows for all cases to pass
            value = value.lower()
            # Variable is set to the index of the tuple
            # using the criterion as an inxed. The count
            # accounts for which row it is on or which book tuple
            category = (list_of_tuples[count][criterion]).lower()
            # Checks if the keyword is part of the selected index
            if value in category:
                # Adds the whole book to the list of tuples
                list_of_tuples_return.append(book)
        if criterion == 1:
            value = value.lower()
            title = (list_of_tuples[count][1]).lower()
            # Ensures the user typed in the title perfetly
            # excluding capitalization
            if value == title:
                return book
        if criterion == 3:
            value = value.lower()
            category = (list_of_tuples[count][criterion])
            if value in category:
                list_of_tuples_return.append(book) 
        if criterion == 5:
            category = (list_of_tuples[count][criterion])
            if value in category:
                list_of_tuples_return.append(book) 
        if criterion == 6:
            rating = (list_of_tuples[count][criterion])
            if value <= rating:
                list_of_tuples_return.append(book) 
        if criterion == 7:
            page_count = (list_of_tuples[count][criterion])
            # Gets a min an max based on the given value
            max_count = value + 50
            min_count = value - 50
            # I tried to use if page count in range(min,max) 
            # but it didn't work so this is how I made sure 
            # the value was within the correct range
            if min_count <= page_count <= max_count:
                list_of_tuples_return.append(book)
        if criterion == 8:
            ratings_count = (list_of_tuples[count][criterion])
            if value == ratings_count:
                list_of_tuples_return.append(book)
        count+=1
    return list_of_tuples_return



def get_books_by_criteria(list_of_tuples, category, rating, page_number):
    """Uses user provided search criteria to filter the list of tuples
    and add books that meet the specifications to a list of tuples which
    is returned."""
    # Runs the initial list of tuples through get books by criteria to 
    # get a list that meets the category searched for
    category_list = get_books_by_criterion(list_of_tuples, 3, category)
    # Runs the category list of tuples through get books by criteria to 
    # get a list that meets the rating and category searched for
    rating_and_category_list = get_books_by_criterion(category_list, 6, rating)
    # Runs the rating and category list of tuples through get books by criteria to 
    # get a list that meets the rating, category, and page count searched for
    final_list = get_books_by_criterion(rating_and_category_list, 7, page_number)

    return final_list

def get_books_by_keyword(list_of_tuples, keywords):
    """Loops through the descriptions from the list of
    tuples, and returns all books that have descriptions
    containing the user provided keyword."""
    # List that will be returned
    list_of_books =  []
    # Loop though books first so they get added to 
    # he returned list in the correct order
    for book in list_of_tuples:
        # Solves case issues
        description = book[4].lower()
        # Checks each word in the list of keywords
        for word in keywords:
            # Solves case issues
            word = word.lower()
            # Adds book to the returned list if the keyword
            # is in the description anywhere
            if word in description and book not in list_of_books:
                list_of_books.append(book)

    return list_of_books

def sort_authors(list_of_tuples, a_z = True):
    """Sorts the list of tuples alphabetically
    either in asscending or descending order based on 
    the a_z parameter"""
    # Sorts from A-> Z since the default value is True
    return_list = sorted( list_of_tuples, key=itemgetter(2) ) 
    # If the value isn't the same as the default value
    if a_z == False:
        # The list is sorted in reverse, form Z-> A
        return_list = sorted( list_of_tuples, key=itemgetter(2), reverse = True ) 
    return return_list
        
def recommend_books(list_of_tuples, keywords, category, rating, page_number,  a_z):
    """Returns a list of reccomended books by passing the inital list of tuples
    through three functions which filter out all books that do not match the criteria given."""
    # Uses get_books_by_criteria to filter by category, rating, and page number
    filtered_by_criteria = get_books_by_criteria(list_of_tuples,category,rating,page_number)
    # Calls get_books_by_keyword on the filtered_by_criteria var to filter by
    # keywords found in the description
    matching_all_criteria = get_books_by_keyword(filtered_by_criteria,keywords)
    # Puts the list in aplhabetically ascending or decensding order based on user preference
    final_list = sort_authors(matching_all_criteria, a_z)

    return final_list

def display_books(list_of_tuples):
    """Prints the book info formatted based on the 
    inputs of funcions that the user called. If no
    results were found in earlier functions, then a 
    print statement lets the user know."""
    # Makes sure that there is a list of values
    print("\nBook Details:")
    if len(list_of_tuples) > 0:
        # Header
        print("{:15s} {:35s} {:35s} {:6s} {:8s} {:15s} {:15s}".format("ISBN-13","Title","Authors",\
         "Year", "Rating", "Number Pages", "Number Ratings"))
        count = 0
        # For every tuple in the list
        for book in list_of_tuples:
            # As long as the length of the title and the author are less than 35
            if len(book[1]) <= 35 and len(book[2]) <= 35:
                # Print the values formatted
                rating = str(book[6])
                if len(rating) < 4:
                    rating += "0"
                print("{:15s} {:35s} {:35s} {:6s} {:8s} {:15s} {:15s}".format(book[0],book[1], book[2],\
                 str(book[5]), rating, str(book[7]), str(book[8])))
                count+=1
    else:
        print("Nothing to print.")


def get_option():
    """Displays a menu of options and prompts
    for an input. It will return the input 
    as long as the input is a number between 1 and 4.
    If that isn't the case it will print an error."""
    user_input = int(input(MENU))
    # Makes sure the input is in the desired range
    if 1 <= user_input <=4:
        return user_input
    else:
        print("\nInvalid option")
        return None

def main():
    returned_file_name = open_file()
    list_of_tuples = read_file(returned_file_name)
    user_input = get_option()
    # Makes sure program stops if user inputs 4
    while user_input != 4:
        if user_input == 1:
            book_list = []
            value = input("\nInput a book title: ")
            # Adds the book(s) with matching title to the list that is printed
            book_list.append((get_books_by_criterion(list_of_tuples,1,value)))
            # Calls function on the list to print it
            display_books(book_list)
            # Prompts for user input
            user_input = get_option()
        elif user_input == 2:
            # Makes sure the user puts in an int
            try:
                criterion = int(input(CRITERIA_INPUT)) 
            except:
                print("\nInvalid input")
                criterion = int(input(CRITERIA_INPUT))
            count = 0
            # Makes sure the user stops being asked for 
            # input after they put a matching number
            while count < 1:
                if criterion == 3 or criterion == 5 or criterion == 6 or criterion == 7:
                    count+=1
                else:
                    print("\nInvalid input")
                    try:
                        criterion = int(input(CRITERIA_INPUT)) 
                    except:
                        print("\nInvalid input")
                        criterion = int(input(CRITERIA_INPUT))
            value = input("\nEnter value: ")
            # Makes the value a float if they choose to sort by rating
            if criterion == 6:
                try:
                    value = float(value)
                except:
                    print("\nInvalid input")
                    value = float(input("\nEnter value: "))
            # Makes the value a int if user chooses to sort by page number
            if criterion == 7:
                try:
                    value = int(value)
                except:
                    print("\nInvalid input")
                    value = int(input("\nEnter value: "))
            # List of organized tuples contains a list that has been 
            # sorted alphabetically and filtered by criteria 
            list_of_organized_tuples = (get_books_by_criterion(sort_authors((list_of_tuples)\
            ,a_z=True), criterion, value))

            list_tuples_to_print = []
            count = 0
            # Prints all books that met the criterion
            for book in list_of_organized_tuples:
                # Makes sure only 30 books will be printed
                if count < 30:
                    # Adds the book to the list that will be printed
                    list_tuples_to_print.append(book)
                # Tracks number of books in list
                count+=1
            # Calls funciton to print the 30 filtered and organized books
            display_books(list_tuples_to_print)
            # Prompts for input
            user_input = get_option()
        elif user_input == 3:
            category = input("\nEnter the desired category: ")
            try:
                rating = float(input("\nEnter the desired rating: "))
            except:
                rating = float(input("\nEnter the desired rating: "))
            try:
                page_number = int(input("\nEnter the desired page number: "))
            except:
                page_number = int(input("\nEnter the desired page number: "))

            a_z_input = int(input("\nEnter 1 for A-Z sorting, and 2 for Z-A sorting: "))

            keywords = input("\nEnter keywords (space separated): ")
            # Turns the string into a list of keywords
            keywords_list = keywords.split()
            # Sorts in ascending or decending aplhabetical order by user preference
            if a_z_input == 1:
                display_books( recommend_books(list_of_tuples, keywords_list, category, rating,\
                 page_number,  True) )
            else:
                display_books( recommend_books(list_of_tuples, keywords_list, category, rating,\
                 page_number, False) )
            user_input = int(input(MENU))
        else:
            user_input = get_option()
    else:
        print()



# DO NOT CHANGE THESE TWO LINES
# These two lines allow this program to be imported into other code
# such as our function_test code allowing other functions to be run
# and tested without 'main' running.  However, when this program is
# run alone, 'main' will execute.
if __name__ == "__main__":
    main()
