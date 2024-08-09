 ###########################################################

    #  Computer Project #10

    #

    #  Algorithm

    #    Shown rules and menu  
    #    This will continue as long as user inputs does not input Q

    #    Initial tableau, stock and foundation are shown
    #    User prompted for an option (DFTRHQ)

    #    If user selects D, then cards are dealt from tableau, deal_to_tableau 
    #    is called and the game is displayed again along with a prompt for input
    
    #    If user inputs F and a number 1-4 (checked for errors) then the card is moved
    #    to the foundation if it is a valid move by the rules of the game. validate_move_to_foundation
    #    and move_to_foundation are utilized and the game is displayed again along with a 
    #    prompt for input

    #    If user inputs T and two numbers 1-4 (checked for errors) then the card is moved
    #    from one column to an empty column, using the validate_move_within_tableau and
    #    move_within_tableau functions to do so and the game is displayed again along with a
    #    prompt for input

    #    If the user inputs R a message is shown and the game resets
    
    #    If the user inputs H the menu of options is shown again

    #    If the user inputs Q then the game is quit and a message is shown.
    #    The game also ends if the game is won (the stock is empty and only aces 
    #    are in the tableau)

 ###########################################################

# I changed the imports due to errors I was getting
from cards import Deck# required !!!
from cards import Card
RULES = '''
Aces High Card Game:
     Tableau columns are numbered 1,2,3,4.
     Only the card at the bottom of a Tableau column can be moved.
     A card can be moved to the Foundation only if a higher ranked card 
     of the same suit is at the bottom of another Tableau column.
     To win, all cards except aces must be in the Foundation.'''

MENU = '''     
Input options:
    D: Deal to the Tableau (one card on each column).
    F x: Move card from Tableau column x to the Foundation.
    T x y: Move card from Tableau column x to empty Tableau column y.
    R: Restart the game (after shuffling)
    H: Display the menu of choices
    Q: Quit the game        
'''

def init_game():
    ''''Sets an empty foundation, instansiates and shuffles 
    a new deck, and deals 4 cards from the deck to the tableau.'''
    # Foundation is alwasy empty when the game starts
    foundation = []
    # Initilize, then shuffle a new deck
    deck_of_fifty_two = Deck()
    deck_of_fifty_two.shuffle()
    tableau = []
    count = 0
    # Creates 4 new lists and adds one card to each of them
    while count < 4:
        new_list = []
        new_list.append(deck_of_fifty_two.deal())
        tableau.append(new_list)
        count +=1
    return deck_of_fifty_two, tableau, foundation

def deal_to_tableau( tableau, stock):
    '''Adds one card to each of the columns (lists) 
    of the tableau.'''
    for column in tableau:
        column.append(stock.deal())

           
def validate_move_to_foundation( tableau, from_col ):
    '''Makes sure that moving card the user wants to
    move to the foundation is a legal move by the rules.'''
    # Count tracks the current col being iterated over
    count = 0
    # List of cards on the bottom of each column of the tableau
    bottom_card_list = []
    # Placeholder var
    chosen_card = ""

    for column in tableau:
        # I use a try except because if the column is empty then
        # there is no [-1] index
        try:
            # Gets the last card in each column
            playable_card = column[-1]
            # When the column we are iterating over is the same as the 
            # one we want to get the card from (from_col)
            if count == from_col:
                chosen_card = playable_card
            # If it isn't the card from the column we want then add it to the
            # list of other cards to later be compared against
            else:
                bottom_card_list.append(playable_card)
        except:
            pass
        count+=1
    # If the chosen card is a card
    if chosen_card != "":
        # If it is an ace then you cannot move it to the foundation
        if chosen_card.value() == 1:
            print("\nError, cannot move {}.".format(chosen_card))
            return False
        else:
            valid_move = False
            for bottom_card in bottom_card_list:
                # If the suits are the same and the card its being compared to is an ace
                # then, since aces are high, it is a valid move
                if chosen_card.suit() == bottom_card.suit() and bottom_card.value() == 1:
                    valid_move = True
                # If the other cards rank is higher and the cards are of the same suit then it is a legal move
                elif chosen_card.rank() < bottom_card.rank() and chosen_card.suit() == bottom_card.suit():
                    valid_move = True
            if valid_move == False:
                print("\nError, cannot move {}.".format(chosen_card))
    # If chosen_card == "" then they tried to move a card from a column with no cards in it
    else:
        print("\nError, empty column:")
        return False
    return valid_move

    
def move_to_foundation( tableau, foundation, from_col ):
    '''After ensuring the desired move is legal, the card is removed
    from the tableau and placed in the foundation pile.'''
    valid_move = validate_move_to_foundation( tableau, from_col )
    # Count workds the same as in the previous function
    # a tracker of column index
    count = 0
    if valid_move == True:
        card = tableau[from_col][-1]
        # Remove the bottom card from the specified column
        for column in tableau:
            if count == from_col:
                column.remove(column[-1])
            count+=1
        # Add the card to the foundation
        foundation.append(card)

def validate_move_within_tableau( tableau, from_col, to_col ):
    '''Checks if it is legal to move a card from one column to another.'''
    valid_move_within = False
    # If the column you want to move to is empty and the column 
    # you are moving the card form isn't empty
    if len(tableau[to_col]) == 0 and len(tableau[from_col]) != 0:
        valid_move_within = True
    # If there are cards in the column you want to move your card to isn't empty
    elif len(tableau[to_col]) != 0:
        print("\nError, target column is not empty: {}".format(to_col+1))
    # If there are no cards in the column you want to move your card from
    elif len(tableau[from_col]) == 0:
        print("\nError, no card in column: {}".format(from_col+1))
    return valid_move_within


def move_within_tableau( tableau, from_col, to_col ):
    '''If the move within tableau is legal, then the card is moved to the empty slot'''
    valid_move_within = validate_move_within_tableau( tableau, from_col, to_col )   
    # Count works the same as in previous functions
    # a tracker of column index
    count = 0
    if valid_move_within == True:
        card = tableau[from_col][-1]
        # Remove card from the from_col column
        for column in tableau:
            if count == from_col:
                column.remove(column[-1])
            count+=1
        # Add card to the to_col column
        tableau[to_col].append(card) 
               
def check_for_win( tableau, stock ):
    '''Checks if the user won, by ensuring the
    stock is empty and the only cards left are aces'''
    only_aces = False
    if stock.is_empty() == True:
        for column in tableau:
            for card in column:
                # Means that the card is an ace
                if card.value() == 1:
                    only_aces = True
                else:
                    return False
    return only_aces
def display( stock, tableau, foundation ):
    '''Provided: Display the stock, tableau, and foundation.'''

    print("\n{:<8s}{:^13s}{:s}".format( "stock", "tableau", "  foundation"))
    maxm = 0
    for col in tableau:
        if len(col) > maxm:
            maxm = len(col)
    
    assert maxm > 0   # maxm == 0 should not happen in this game?
        
    for i in range(maxm):
        if i == 0:
            if stock.is_empty():
                print("{:<8s}".format(""),end='')
            else:
                print("{:<8s}".format(" XX"),end='')
        else:
            print("{:<8s}".format(""),end='')        
        
        #prior_ten = False  # indicate if prior card was a ten
        for col in tableau:
            if len(col) <= i:
                print("{:4s}".format(''), end='')
            else:
                print( "{:4s}".format( str(col[i]) ), end='' )

        if i == 0:
            if len(foundation) != 0:
                print("    {}".format(foundation[-1]), end='')
                
        print()


def get_option():
    '''Prompts for options (based on menu) and checks that it 
    is a valid input. If it is valid, then the option is returned in a list
    but if not, an error is printed and an empty list is returned.'''
    return_list =[]
    user_input = input("\nInput an option (DFTRHQ): ")
    list_of_valid_options = ["D","F","T","R","H","Q"]
    user_input_list = user_input.split()
    letter = user_input_list[0].upper()
    if letter in list_of_valid_options:
        if letter == "F":
            # Makes sure that the user only typed F and x (an int) by 
            # seeing if the number of items in the list after the .split() is two
            if len(user_input_list) == 2:
                try:
                    # Change the second value in the list to an int and -1 to
                    # account for index numbers vs column numbers
                    x = int(user_input_list[1]) -1
                    if x not in range(0,4):
                        print("\nError in option:" , user_input)
                        return []
                    choice = user_input_list[0].upper()
                    # List of choice (F) and the column index is returned
                    return_list = [choice, x]
                    return return_list
                except:
                    # If the user provides F and a letter instead of an x
                    # then an error is shown and an empty list is returned
                    print("\nError in option:" , user_input)
                    return []
            else:
                # If the user provides F and too many numbers
                print("\nError in option:" , user_input)
                return []
        elif letter == "T":
            # Makes sure that the user only typed F and x (an int) and y (an int) by 
            # seeing if the number of items in the list after the .split() is three
            if len(user_input_list) == 3:
                try:
                    # Change the 2nd and 3rd value in the list to an int and -1 to
                    # account for index numbers vs column numbers
                    x = int(user_input_list[1]) -1
                    y = int(user_input_list[2]) -1
                    # Makes sure both numbers are in range
                    if x not in range(0,4) or y not in range(0,4):
                        print("\nError in option:" , user_input)
                        return []
                    choice = user_input_list[0].upper()
                    # Returns letter (T) and both column numbers
                    return_list = [choice,x,y]
                    return return_list
                except:
                    # If the user provides T and letters instead of an int x
                    # or y then an error is shown and an empty list is returned
                    print("\nError in option:" , user_input)
                    return []
            else:
                # If the user provides T and too many numbers
                print("\nError in option:" , user_input)
                return []
        else:
            # Makes sure the user only input one letter
            # Ex.) D instead of D 1 2 3
            if len(user_input_list) == 1:
                return_list.append(letter)
            else:
                print("\nError in option:" , user_input)
            return return_list 
    # If the inputted letter isn't one of the options listed
    else:
        print("\nError in option:" , user_input)
        return []
def main():
    print(RULES)
    print(MENU)
    game= init_game()
    # display(stock,tableau, foundation)
    display(game[0],game[1],game[2])
    valid_input = False
    option = ""
    # Makes sure that an empty list isn't returned
    # to prevent errors in while loop
    while valid_input == False:
        if len(option) < 1:
            option = get_option()
        else:
            valid_input = True
    while "Q" not in option:
        try:
            # Deals cards if the user requests
            if option[0] == "D":
                deal_to_tableau(game[1],game[0])
            # Moves card to foundation on user request if the move is legal
            elif option[0] == "F":
                move_to_foundation( game[1], game[2], option[1] )
            # Moves card from column to column on user request if legal
            elif option[0] == "T":
                move_within_tableau( game[1], option[1], option[2] )
            # Prints messages and resets game
            elif option[0] == "R":
                print("\n=========== Restarting: new game ============")
                print(RULES)
                print(MENU)
                game = init_game()
            # Prints menu of options on user request
            elif option[0] == "H":
                print(MENU)
            win = check_for_win(game[1],game[0])
            # Breaks loop if the game has been won
            if win == True:
                print("\nYou won!")
                break
            display(game[0],game[1],game[2])
            option = get_option()
        except:
            option = get_option()
    else:
        print("\nYou have chosen to quit.")
if __name__ == '__main__':
     main()
