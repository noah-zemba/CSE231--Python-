 ###########################################################

    #  Computer Project #4

    #

    #  Algorithm

    #    Banner is displayed along with menu, user is promted for input 

    #    Input provided triggers one of 7 options or returns an error if
    #    input wasn't recognized
    
    #    This will continue as long as user doesn't input x whenever prompted

    #    If user selects A prompt for numtobase() paramaters and return result
        # numtobase() changes decimal numbers to numbers in a given base
    
    #    If user selects B prompt for basetonum() paramaters and return result
        # basetonum() changes numbers in a given string from a given base
        # to a different also user specified base
    
    #    If user selects C prompt for basetobase() paramaters and return result
        # basetobase() chenges a number from one base to a decimal number
        # and then into a differnet specified base
    
    #    If user selects E prompt for encode_image() paramaters and return result
        # encode_image() turns a given message into binary and then splices is into 
        # the slot of the least significant bit in a given image to produce a encoded image
    
    #    If user selects D prompt for decode_image() paramaters and return result
        # decode_image() takes an encoded string and removes the original binary string
        # and translates it into ASCII
    
    #    If user selects M show the menu and prompt again

    #    If user selects X print message and end program 

 ###########################################################

MENU = '''\nPlease choose one of the options below:
             A. Convert a decimal number to another base system         
             B. Convert decimal number from another base.
             C. Convert from one representation system to another.
             E. Encode an image with a text.
             D. Decode an image.
             M. Display the menu of options.
             X. Exit from the program.'''


def numtobase( N, B ):
    '''Function takes a user inputted number and
       converts it to a base of the user's choice.'''
    # Will end up representing the "translated" and returned number
    binary_num = ""
    # Probably doesn't need to be so big but go big or go home
    # I wasn't sure how to loop through while quotient != 0 
    # because my quotient variable isnt defined yet
    count = 10000000
    
    # Accounts for case in which no number is provided and returns
    # an empty string per the instrutions
    if N == 0:
        binary_num = ""
    # The case in which a number was provided
    else:
        while count > 0:       
            # Accounts for the first time the loop runs, to set a value for quotient
            # in a way that allows it to update later
            if len(binary_num) == 0:
                remainder = N%B
                # Adding the remainder to the front now prevents me from having
                # to flip the string later
                binary_num = str(remainder) + binary_num
                # Sets an initial value for quotient
                quotient = N//B
            # This case will run every time but the first time
            else:
                new_remainder = quotient%B
                quotient = quotient//B
                binary_num = str(new_remainder) + binary_num
            # This means there is nothing left to be divided so the number
            # has been fully translated to binary
            if quotient == 0:
                break
    # If the length of the string isn't a multiple of 8
    # In hindsight this if may be redundant        
    if len(binary_num) % 8 != 0:
        # While the length of the string isn't a multiple of 8
        while len(binary_num) % 8 != 0:
            binary_num = str(binary_num) 
            # Add a 0 to the string
            binary_num = "0" + binary_num
            
    return binary_num

def basetonum( S, B ):
    '''Function takes user inputted string and converts it to
       a decimal number using the base provided as a conversion 
       factor.'''
    # This will be the decimal number being returned
    normal_int = 0
    placeCount = 0
    S = str(S)  
    # If the length of S isn't 8, add 0's until it is
    if len(S) < 8:
        while len(S)<8:
            S = "0" + S
    count = len(S)-1
    while count >= 0:
        # Transform num = current digit of S x Base^index
        transform_num = (int(S[placeCount])) * (B**count)
        normal_int = normal_int + transform_num
        placeCount+=1
        count-=1
    return normal_int

def basetobase(B1,B2,s_in_B1):
    '''Function takes user input string (s_in_B1) and, considering the base (B1)
       provided, converts it to a new number of base B2.'''
    # Translates all variables from the paramaters to work within
    # the functions being called, not sure if this is necessary but 
    # I did it throughout my whole project
    S = s_in_B1
    B = B1
    # Converts from base provided to decimal
    B1_s_to_normal_num = basetonum(S, B)
    N = int(B1_s_to_normal_num)
    B = B2
    # Converts decimal to new base
    normal_num_to_B2 = numtobase(N, B)
    return normal_num_to_B2

def encode_image(image,text,N):  
    '''Function takes provided text and converts it to 
       binary by calling the numtobase() function and using 
       a combination of user provided and set values as paramaters.
       After being converted, the string of binary is spliced into
       the original provided image string at every Nth (user provided)
       index. The resulting encoded string is returned.'''
    # I was concerned that if I didn't essentially save a state of N
    # as a new variable that I would mess up the value later
    every_N = N
    every_N = int(every_N)
    # If no image is provided then return an empty string
    if image == "":
        return ""
    # If no text is provided then return the image
    if text == "":
        return image
    # Will eventually be the message converted to binary
    in_binary = ""
    # FOr each letter in the provided message 
    for letter in text:
        # Base will always be 2 since we are converting to binary
        B = 2
        # Converts the letter to its numerical ASCII value
        N = ord(letter)
        # Adds each converted letter to the in_binary string
        in_binary += (numtobase(N, B))
    # Convert in_binary into a string for the fun of it, pretty sure 
    # this is redundant
    in_binary = str(in_binary)
    count = 1
    # Tracks the index of the image
    image_count = 0
    # Tracks the index of the message input
    text_index = 0
    # Will actually be the encoded string that is returned believe it or not
    encoded_string = ""
    # I multiplied the length of in_binary by every_N because the amount of times 
    # it needs to run is every_N (N) times more that the length of in_binary
    if len(in_binary)*every_N <= len(image):
        # Prevents index is out of bounds errors and continues the loop
        # until the binary string is fully spliced in
        while count <= len(in_binary)*every_N and image_count< len(image):
            # Accounts for the first run of the loop
            if count == 0:
                encoded_string+=image[image_count]
            # If the count isn't 0 and the count is a multiple of the every_N (N) provided
            # then splice in one digit of the secret binary the user wants encoded
            elif count % every_N == 0 and count != 0:
                # This variable is useless and I could combine these two lines
                insert_letter = in_binary[text_index]
                encoded_string+= insert_letter
                text_index+=1
            
            # When the count isn't a multiple of every_N, we want the image to be spliced in
            elif count % every_N != 0:
                encoded_string+=image[image_count]
            # Image count always has to go up even when a digit from image
            # isn't printed so that the resulting string looks spliced
            image_count+=1
            count+=1  
        # Adds the remainder of the image string to the encoded string
        encoded_string+= image[image_count:]
        return encoded_string   
    else:
        return 


def decode_image(sego,N):
    '''Function loops through user provided encoded image (sego)
       and takes every Nth (user provided) digit and adds it to 
       a string (S) that is cut off every 8 indexes and converted 
       to decimal numbers using the basetonum() function and then 
       into ASCII characters using the built-in chr() function.'''
    # Will hold the message in binary and then will be converted to ASCII letters
    decoded_message_in_binary = ""
    # I added the dash before the string so that the count and index would match up
    sego = "-"+sego
    count = 0
    trimmed_msg = ""
    for index, value in enumerate(sego):
        # If the index is a multiple of the N amount of bits provided
        # and it is not the first time through the loop
        if index % N == 0 and index != 0:
            # Add the character at the current index to the decoded message
            decoded_message_in_binary += sego[count]
        count+=1
    length = len(decoded_message_in_binary)
    # Finds the nearest mutiple of 8 to the length of the decoded message
    # in binary
    closest_multiple = (length // 8)*8
    # Originally was meant to see if the length wasn't a multiple of 8
    # and make it so it was, but it cut too much off and caused errors
    if length >= closest_multiple:
        # Originally was trimmed_msg = decoded_message_in_binary[difference:]
        # but was throwing errors in test 5
        trimmed_msg = decoded_message_in_binary[:]
    length = len(trimmed_msg)

    S = ""
    full_string = ""
    index = 0
    counter = 1
    # This condition causes the code to run as many times as there
    # are groups of 8 binary numbers
    while counter <= length//8:
        # From the current starting index through the next 8
        for i in range(index, index+8):
            # Add 8 digits from the trimmed_msg
            S+=trimmed_msg[index]
            # And then turn them into decimal numbers
            snippet = basetonum(S, 2)
            index+=1
        # This updates the variable I believe, that was the hope at least
        index = index
        # This resets S back to nothing every time because it was sending the 
        # first 8 binary characters the first time through the loop, then
        # the first 16 the second time, then the first 32 the third time etc.
        S = ""
        # Adds the snippet to the string that will be returned
        full_string+=chr(snippet)
        counter+=1
 
    return full_string


def main():
    BANNER = '''
               A long time ago in a galaxy far, far away...   
              A terrible civil war burns throughout the galaxy.      
  ~~ Your mission: Tatooine planet is under attack from stormtroopers,
                   and there is only one line of defense remaining        
                   It is up to you to stop the invasion and save the planet~~
    '''

    print(BANNER)   
    print(MENU)
    user_input = input("\n\tEnter option: ")
    user_input = user_input.lower()
    # Ensures the user didn't put x
    while user_input != "x":
        if user_input == "a":    
            # This counter will stop the loop if the conditions of a valid
            # input given by the instructions are met
            valid_count = 0
            while valid_count == 0:
                N_str = (input("\n\tEnter N: "))
                # Checks if N is a digit
                if N_str.isdigit() == False:
                    # If it isnt, it is not a valid input
                    print("\n\tError: " + N_str +" was not a valid non-negative integer.")
                if N_str.isdigit():
                    # Since we know the N is a digit we can safley turn it into an int
                    N = int(N_str)
                    # Checks if N is positive
                    if N<0:
                        # If it isnt, it is not a valid input
                        print("\n\tError: " + N_str +" was not a valid non-negative integer.")
                    elif N>=0:
                        # Essentially stops the loop
                        valid_count+=1
            # This counter will stop the loop if the conditions of a valid
            # input given by the instructions are met
            valid_count_B = 0
            while valid_count_B == 0:
                B_str = (input("\n\tEnter Base: "))
                # If B isn't a digit it isn't a valid input
                if B_str.isdigit() == False:
                    print("\n\tError: " +B_str + " was not a valid integer between 2 and 10 inclusive.")
                # Makes sure B is a digit
                if B_str.isdigit()==True:
                    B = int(B_str)
                    # Ensures B is in the valid range of bases
                    if 2<=B<=10:
                        # Essentially ends the loop
                        valid_count_B+=1
                    # If B is a number but not between 2 and 10 inclusive
                    # it isn't valid
                    else:
                        print("\n\tError: " +B_str + " was not a valid integer between 2 and 10 inclusive.")
            # Calls the function and assigns the return value to a variable        
            print_variable = numtobase(N, B)
            print(("\n\t {} in base {}: {}").format(N, B, print_variable))
            user_input = input("\n\tEnter option: ")

        elif user_input == "b":
            S = input("\n\tEnter string number S: ")
            # This counter will stop the loop if the conditions of a valid
            # input given by the instructions are met
            valid_count_B = 0
            while valid_count_B == 0:
                B_str = (input("\n\tEnter Base: "))
                # If B isn't a digit it isn't a valid input
                if B_str.isdigit() == False:
                    print("\n\tError: " +B_str + " was not a valid integer between 2 and 10 inclusive.")
                # Makes sure B is a digit
                if B_str.isdigit()==True:
                    B = int(B_str)
                    # Ensures B is in the valid range of bases
                    if 2<=B<=10:
                        # Essentially grinds the loop to a halt
                        valid_count_B+=1
                    # If B is a number but not between 2 and 10 inclusive
                    # it isn't valid
                    else:
                        print("\n\tError: " +B_str + " was not a valid integer between 2 and 10 inclusive.")
            # Calls the function and assigns the return value to a variable
            print_variable = basetonum(S, B)
            print("\n\t " + S + " in base " + str(B) + ": " + str(print_variable))
            user_input = input("\n\tEnter option: ")

        elif user_input == "c":
            # Same as above 
            # While the condition of a valid input isn't met, user is prompted
            # for base inputs that is an integer between 2 and 10
            valid_count_B1 = 0
            while valid_count_B1 == 0:
                B1_str = (input("\n\tEnter base B1: "))
                if B1_str.isdigit() == False:
                    print("\n\tError: " +B1_str + " was not a valid integer between 2 and 10 inclusive.")
                if B1_str.isdigit()==True:
                    B1 = int(B1_str)
                    if 2<=B1<=10:
                        valid_count_B1+=1
                    else:
                        print("\n\tError: " +B1_str + " was not a valid integer between 2 and 10 inclusive.")
            # While the condition of a valid input isn't met, user is prompted
            # for base inputs that is an integer between 2 and 10
            valid_count_B2 = 0
            while valid_count_B2 == 0:
                B2_str = (input("\n\tEnter base B2: "))
                if B2_str.isdigit() == False:
                    print("\n\tError: " +B2_str + " was not a valid integer between 2 and 10 inclusive.")
                if B2_str.isdigit()==True:
                    B2 = int(B2_str)
                    if 2<=B2<=10:
                        valid_count_B2+=1
                    else:
                        print("\n\tError: " +B2_str + " was not a valid integer between 2 and 10 inclusive.")
            # Sets paramater so function can run when called
            s_in_B1 = input("\n\tEnter string number: ")
            # Calls the function and assigns the return value to a variable
            print_variable = basetobase(B1, B2, s_in_B1)
            print("\n\t " + s_in_B1 + " in base " + str(B1) + " is " + str(print_variable) + " in base " + str(B2) + "...")
            user_input = input("\n\tEnter option: ")
        
        elif user_input == "e":
            # Sets all paramaters of function that I will call to the inputs
            image = input("\n\tEnter a binary string of an image: ")
            N = int(input("\n\tEnter number of bits used for pixels: "))
            text = input("\n\tEnter a text to hide in the image: ")
            # Calls the function and assigns the return value to a variable
            print_variable = encode_image(image, text, N)
            # If the funciton returns none, then that means that the image wasn't large 
            # enough to hold the message
            if str(print_variable) == "None":
                print("\n\tImage not big enough to hold all the text to steganography")
            # If the image doesn't exist then it certainly isn't big enough to 
            # encode the message
            elif len(image) == 0:
                print("\n\tImage not big enough to hold all the text to steganography")
            # Cases in which a string is returned
            else:
                print("\n\t Original image: "+ image)
                print("\n\t Encoded image: " + str(print_variable))
            user_input = input("\n\tEnter option: ")
        
        elif user_input == "d":
            # Sets the paramaters equal to the inputs
            sego = input("\n\tEnter an encoded string of an image: ")
            N = int(input("\n\tEnter number of bits used for pixels: "))
            # Calls the function and assigns the return value to a variable
            print_variable = decode_image(sego, N)     
            print("\n\t Original text: " + print_variable)
            user_input = input("\n\tEnter option: ")
            
        # The user wants the menu, we give them the menu
        elif user_input == "m":
            print(MENU)
            user_input = input("\n\tEnter option: ")
        else:
            # Since I set the input to lowercase earlier I have to change it back
            # for printing 
            option_selected = user_input.upper()
            print("\nError:  unrecognized option " + "[" + option_selected +"]")
            # Starts loop again
            print(MENU)
            user_input = input("\n\tEnter option: ")
        user_input = user_input.lower()  
    # If the user inputs X or x when prompted the program ends and this is printed
    else:
        print('\nMay the force be with you.')

# These two lines allow this program to be imported into other code
# such as our function tests code allowing other functions to be run
# and tested without 'main' running.  However, when this program is
# run alone, 'main' will execute.
#DO NOT CHANGE THESE 2 lines  
if __name__ == '__main__': 
    main()
