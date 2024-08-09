import csv
from operator import itemgetter


MENU = '''\nSelect from the option: 
        1.Games in a certain year 
        2. Games by a Developer 
        3. Games of a Genre 
        4. Games by a developer in a year 
        5. Games of a Genre with no discount 
        6. Games by a developer with discount 
        7. Exit 
        Option: '''
        
      
        
def open_file(s):
    ''' Depending on paramater, either prompts for game file
    name or discount file name and returns the file pointer, 
    prompts until valid file is given.''' 
    valid_input = False
    while valid_input == False: 
        try:
            file_name = input('\nEnter {} file: '.format(s))
            fp = open(file_name, encoding='UTF-8')
            return fp
        except:
            print('\nNo Such file')
        

def read_file(fp_games):
    ''' Read file organizes the data in the given FP
    in a dictionary after converting data types and price.'''
    # Dictionary to be returned
    dict_o_games = {}
    fp_games.readline()
    for game in csv.reader(fp_games):
        list_of_genres = game[3].split(";")
        list_of_devs = game[2].split(";")
        player_mode = game[4].split(";")[0]
        # Defaults player mode to 1 unless its a multiplayer game
        player_mode_int = 1
        if player_mode[0:5].lower() == "multi":
            player_mode_int = 0
        # Tries to convert price to a float after removing commas
        # and sets price to 0.0 if the game is "Free to Play"
        try:
            price = float(game[5].replace(",",""))
            price = price * 0.012
        except:
            price = 0.0
        # Adds support for platform to list if the .csv
        # value of the column is  "1"
        supported_platform_list = []
        if game[9] == "1":
            supported_platform_list.append("win_support")
        if game[10] == "1":
            supported_platform_list.append("mac_support")
        if game[11] == "1":
            supported_platform_list.append("lin_support")
        # Adds the new game (key) to the dictionary with all info in a list (value)
        dict_o_games[game[0]] = [game[1],list_of_devs,list_of_genres,player_mode_int,price,\
        game[6],int(game[7]),int(game[8].replace("%","")),supported_platform_list]

    return dict_o_games


def read_discount(fp_discount):
    ''' Read discount organizes the data in the given FP
    in a dictionary after converting and rounding price.'''
    # Dictionary to be returned
    discount_dictionary = {}
    fp_discount.readline()
    for discount in csv.reader(fp_discount):
        # Adds the game (key) and the covnerted to float and 
        # rounded discount (value) to the dictionary
        discount_dictionary[discount[0]] = round(float(discount[1]),2)
    return discount_dictionary


def in_year(master_D,year):
    '''Given a dictionary of games, in_year returns
    all games that were published within a specified year
    in an alphabetically sorted list.'''
    # List to be returned
    games_in_range = []
    for key,value in master_D.items():
        # value[0] is a string containing the date
        # so check if the year (as a string) is in the MM/DD/YYY
        if str(year) in value[0]:
            # If it is append it to the list
            games_in_range.append(key)
    # Sort the list alphabetically
    games_in_range = sorted(games_in_range,reverse = False)

    return games_in_range


def by_genre(master_D,genre): 
    ''' Sorts games of a certain genre in order of parcentage 
    of positive ratings.'''
    # Final list of games in order that will be returned
    ordered_games_in_genre = []
    # List of games in the specified genre
    games_in_genre = []
    # Stores all positive ratings
    list_of_values = []
    # For each value attached to each game key
    for key,value in master_D.items():
        # Append the % positive ratings
        list_of_values.append((key,value[7]))
    # Sorts the list of ratings in descending order
    sorted_by_percent = sorted(list_of_values,key = itemgetter(1),reverse = True)
    # Will hold all game names (keys) in order of % positive ratings

    # Checks if the desired genre is in the list of genres for each game
    # and adds the key to the games_in_genre list if it is of the correct genre
    for key,value in master_D.items():
        for word in value[2]:
            if word == genre:
                games_in_genre.append(key)
    
    # Loops through the ordered list of keys
    for game in sorted_by_percent:
        # And appends the games from games_in_genre in the order of
        # % pos rating descending
        for genre_game in games_in_genre:
            if genre_game == game[0]:
                ordered_games_in_genre.append(genre_game)
    return ordered_games_in_genre


def by_dev(master_D,developer): 
    ''' Returns a list of games made by a specified developer,
    ordered by date released descending.'''
    # Holds a sorted list years (int) in descending order
    dates_descending = []
    # Holds all games made by specified developer
    games_by_dev = []
    # Holds all game titles in order of year descending
    games_by_year = []
    # Holds all games made by the specified developer in order of dates descending
    ordered_games_by_dev = []
    # Adds all the years converted to int to a list
    for key,value in master_D.items():        
        dates_descending.append((key,int(value[0][-4:])))
    # Sorts years from most recent to oldest
    dates_descending = sorted(dates_descending, key = itemgetter(1),reverse  = True)

    # From the master list, add all games made by a certain developer to a new list
    for key,value in master_D.items():
        if value[1][0] == developer:
            games_by_dev.append(key)
    # Loop through the list of all games in year descending and the games we are interested in 
    # (games made by certain developer) and add them to the new ordered list if the titles match
    for game in dates_descending:
        for dev_game in games_by_dev:
            if dev_game == game[0]:
                ordered_games_by_dev.append(dev_game)
    return ordered_games_by_dev


def per_discount(master_D,games,discount_D): 
    ''' Checks if desired games have a discount, if a game has a discount it 
    is applied to the price and added to the final list, and if not the original price 
    is appended to the final list.'''
    # Final list to be returned
    adjusted_price_list = []
    # List of tuples holding (game, original price)
    list_game_price = []
    # List of tuples holding (game name, discount)
    discount_list = []
    # A list to ensure games are only put in final lsit once
    games_with_discount = []
    # Loops through the list of given games and master dict, adding each desired game 
    # and its price (converted to float) to a tuple and adds that tuple to the list of game prices
    for desired_game in games:
        for game,info in master_D.items():
            if desired_game == game:
                list_game_price.append((game,float(info[4])))
    # Loops through desired games and discount dict, adding only each desired game and its discount 
    # (converted to float) to a tuple and adds that tuple to the list of discounts
    for desired_game in games:
        for game,discount in discount_D.items():
            if desired_game == game:
                discount_list.append((game,float(discount)))
                # This holds the names of the games in another seperate list
                games_with_discount.append(game)
    # Loops through the list of tuples of original prices and applies its discount if it has one
    # or adds the original price to the adjusted prices list
    for undiscounted_games in list_game_price:
        if len(discount_list) > 0:
            for discount_games in discount_list:
                # Making sure that the game titles are the same to ensure the right discount is being
                # applied and then rounded to 6 decimal places
                if undiscounted_games[0] == discount_games[0]:
                    discounted_price = (1-(discount_games[1]/100))*undiscounted_games[1]
                    adjusted_price_list.append(round(discounted_price,6))
                else:
                    # Since every game in discount list is being looped over multiple times it is necessary to 
                    # make sure that no games will be double added to the final list. The first half of the if statement makes sure that
                    # only games that don't have discounts are being added while undiscounted
                    if undiscounted_games[0] not in games_with_discount and undiscounted_games[1] not in adjusted_price_list:
                        adjusted_price_list.append(undiscounted_games[1])
        else:
            adjusted_price_list.append(undiscounted_games[1])
    return adjusted_price_list


def by_dev_year(master_D,discount_D,developer,year):
    ''' Filters out games made by a specified dev in a specified year and returns 
    them in order of discounted (if applicable) price ascending'''
    # Will hold the games that meet the dev and year criteria and their discounted prices
    list_o_tuples_price_game = []
    # Will hold the games that meet the dev and year criteria
    list_dev_and_year = []
    # Will hold the list of games that meet the criteria in order of discounted price ascending
    return_list = []
    # Holds all games that are made in the desired year
    list_games_in_year = in_year(master_D,year)
    # Holds all games that are made by the desired dev
    list_games_by_dev = by_dev(master_D,developer)
    # Loops thorugh both lists and adds titles that appear on both to a new list
    # (the list will hold games that are made by the specified dev in the specified year)
    for game_year in list_games_in_year:
        for game_dev in list_games_by_dev:
            if game_dev == game_year:
                list_dev_and_year.append(game_year)
    discount_list = per_discount(master_D,list_dev_and_year,discount_D)
    # Used as an index for list_dev_and_year
    count = 0
    for price in discount_list:
        # Appends a tuple (discounted price,game title)
        list_o_tuples_price_game.append((price,list_dev_and_year[count]))
        count+=1
    # Sorts by discounted price ascending
    sorted_by_price = sorted(list_o_tuples_price_game, key = itemgetter(0))
    # Appends the titles (now in order of price) to the final list
    for tuuple in sorted_by_price:
        return_list.append(tuuple[1])
    return return_list
   
          
def by_genre_no_disc(master_D,discount_D,genre):
    ''' Filters out games of a specified genre which do not have discounts.
    In the case in which multiple games have the same price, they are returned
    in order of percentage of positive ratings high -> low.'''
    # Holds list of games in desired genre
    list_games_in_genre = by_genre(master_D,genre)
    # Holds list of tuples of all games in genre and their original price (title, original price)
    list_tuple_game_original_price = []
    # Makes tuples of games in genre alog with their original price
    for title,info in master_D.items():
        for game in list_games_in_genre:
            if title == game:
                list_tuple_game_original_price.append((title,float(info[4])))
    # Holds prices of the games in genre after applying any existing discounts
    list_of_discounts = per_discount(master_D,list_games_in_genre,discount_D)
    # Holds list of tuples contaning games and their prices only if prices don't change after checking for discounts
    undiscounted_games = []
    for price in list_of_discounts:
        for tuuples in list_tuple_game_original_price:
            # If the old price (tuuples[1]) is the same as the discounted price (price)
            if tuuples[1] == price and tuuples[0] not in undiscounted_games:
                # Append the game and its price
                undiscounted_games.append((tuuples[0],price))
    list_of_percent_pos = []
    for game,info in master_D.items():
        # Append the % positive ratings
        list_of_percent_pos.append((game,info[7]))
    # Sorts the list of ratings in descending order
    sorted_by_percent = sorted(list_of_percent_pos,key = itemgetter(1), reverse = True)
    # Holds a tuple of the game and its price, after being sorted by percent positive rating descending
    desired_games_by_percent_pos = []
    # Creates a list of games with discounts
    discounted_games = []
    for game,info in discount_D.items():
        discounted_games.append(game)
    # Loops through sorted percentages and appends game tuples to new list in order of percent positive rating descending
    for percentage in sorted_by_percent:
        for game in undiscounted_games:
            # IF the titles are the same,and the game isn't already in the list, and the game isn't in 
            #the list of discounted games then add to the new list
            if game[0] == percentage[0] and game not in desired_games_by_percent_pos and game[0] not in discounted_games:
                desired_games_by_percent_pos.append(game)
    # The list is now sorted by percent pos rating, and needs to be sorted by price
    # I sorted by percent pos rating first so that when there are ties in price, the higher rated game will come first
    sorted_by_percent_price = sorted(desired_games_by_percent_pos,key = itemgetter(1))
    # Will hold only the titles, not the price
    return_list = []
    # Loops though the list of tuples of games in order of percent pos raiting and price,
    # adds the title only to the list to be returned
    for item in sorted_by_percent_price:
        return_list.append(item[0])
    return return_list
def by_dev_with_disc(master_D,discount_D,developer):
    ''' Filters games within a certain genre that have a discount 
    and returns them in order of price, if there is a tie then 
    the order will be based on percentage positive ratings descending.'''
    games_by_dev = by_dev(master_D,developer)
    # List of tuples that hold the title, year released, and price
    list_tuple_game_original_price = []
    # Adds title, year released, and price to list if it is within the correct genre
    for title,info in master_D.items():
        for game in games_by_dev:
            if title == game:
                list_tuple_game_original_price.append((title,int(info[0][-4:]),float(info[4])))
    # Holds the games sorted by release year descneing (recent -> old)
    list_tuple_game_original_price_by_year = sorted(list_tuple_game_original_price,key = itemgetter(1), reverse = True)
    # Sorts the sorted list to be sorted by price
    list_tuple_game_original_price_by_year_price = sorted(list_tuple_game_original_price_by_year,key = itemgetter(2), reverse = False)
    discounted_games = []
    # If the game from the sorted list is in the discount list, append it to the final list
    for game in list_tuple_game_original_price_by_year_price:
        for title, info in discount_D.items():
            if game[0] == title:
                discounted_games.append(title)
    
    return discounted_games
def main():
    game_fp = open_file("games")
    discount_fp = open_file("discount")
    games_dictionary = read_file(game_fp)
    discount_dictionary = read_discount(discount_fp)
    user_input = 1
    while user_input != 7:
        try:
            user_input = int(input(MENU))
        except:
            print("\nInvalid option")
        # Solves a int being out of range
        if user_input in range (1,8):
            if user_input == 1:
                valid_input = False
                while valid_input == False:
                    try:
                        # Tries to convert to year and prompts until an int is input
                        year = int(input('\nWhich year: '))
                        valid_input = True
                        games_in_year = in_year(games_dictionary,year)
                        print_str = ""
                        if len(games_in_year) > 0:
                            for game in games_in_year:
                                print_str += game + ", "
                            # Gets rid of final comma and space
                            print_str = print_str[:-2]
                            print("\nGames released in {}:".format(str(year)))
                            print(print_str)
                        else:
                            print("\nNothing to print")
                    except:
                        print("\nPlease enter a valid year")
                    
            elif user_input == 2:
                dev = input('\nWhich developer: ')
                games_by_dev = by_dev(games_dictionary,dev)
                print_str = ""
                if len(games_by_dev) > 0:
                    for game in games_by_dev:
                        print_str += game + ", "
                    print_str = print_str[:-2]
                    print("\nGames made by {}:".format(dev))
                    print(print_str)
                else:
                    print("\nNothing to print")
            elif user_input == 3:
                genre = input('\nWhich genre: '   )
                games_by_genre = by_genre(games_dictionary,genre)
                print_str = ""
                if len(games_by_genre) > 0:
                    for game in games_by_genre:
                        print_str += game + ", "
                    print_str = print_str[:-2]
                    print("\nGames with {} genre:".format(genre))
                    print(print_str)
                else:
                    print("\nNothing to print")
            elif user_input == 4:
                dev = input('\nWhich developer: ')
                valid_input = False
                while valid_input == False:
                    try:
                        year = int(input('\nWhich year: '))
                        valid_input = True
                        games_dev_year = by_dev_year(games_dictionary,discount_dictionary,dev,year)
                        print_str = ""
                        if len(games_dev_year) > 0:
                            for game in games_dev_year:
                                print_str += game + ", "
                            print_str = print_str[:-2]
                            print("\nGames made by {} and released in {}:".format(dev,str(year)))
                            print(print_str)
                        else:
                            print("\nNothing to print") 
                    except:
                        print("\nPlease enter a valid year")
            elif user_input == 5:
                genre = input('\nWhich genre: '   )
                games_genre_no_disc = by_genre_no_disc(games_dictionary,discount_dictionary,genre)
                print_str = ""
                if len(games_genre_no_disc) > 0:
                    for game in games_genre_no_disc:
                        print_str += game + ", "
                    print_str = print_str[:-2]
                    print("\nGames with {} genre and without a discount:".format(genre))
                    print(print_str)
                else:
                    print("\nNothing to print") 
            elif user_input == 6:
                dev = input('\nWhich developer: ')
                games_genre_no_disc = by_dev_with_disc(games_dictionary,discount_dictionary,dev)
                print_str = ""
                if len(games_genre_no_disc) > 0:
                    for game in games_genre_no_disc:
                        print_str += game + ", "
                    print_str = print_str[:-2]
                    print("\nGames made by {} which offer discount:".format(dev))
                    print(print_str)
                else:
                    print("\nNothing to print") 
                    
        else:
            print("\nInvalid option")
    else:
        print("\nThank you.")

if __name__ == "__main__":
    main()