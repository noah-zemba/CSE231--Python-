###########################################################

    #  Computer Project #5

    #

    #  Algorithm

    #    Banner is displayed along with menu, user is promted for input 

    #    Input provided triggers one of 3 options and prompts until valid
    #    input is given
    
    #    This will continue as long as user doesn't input 3 whenever prompted

    #    If user selects 1 prompt, run open file and prompt for filename and
    #    prompt until valid filename is given
    
    #    Use run_file to loop through file and find min, max, calculate the
    #    average score, and find the show with the most episodes and return them

    #    If the user selects 2 prompt, prompt for the file they want to open with
    #    open_file and prompt for a keyword to search for and then run the search_anime
    #    function

    #    Use search_anime to loop through the selected file and return all 
    #    the titles that include the inputted keyword and the number of shows returned
    
    #    If the user selects 3 print thank you message and end prgram 

 ###########################################################
def open_file():
    '''This function takes a user input and tries to 
       open the corresponding text file, prompting for
       new input until one is given that opens a file.'''
    count = 0
    file_name = input("\nEnter filename: ")
    # Ensures the function will end after a satasfactory input is given
    while count<1:
        try:
            text = open(file_name,'r', encoding="utf-8")
            count+=1
        except:
            print("\nFile not found!")
            file_name = input("\nEnter filename: ")
    return text
    
def find_max(num, name, max_num, max_name):
    '''Compares the given show and rating to 
        another show and rating to see which has
        the highest rating.'''
    if num < max_num:
        # Returns the max_num and the name assiciated with
        # it if num is smaller
        return max_num,max_name
    elif num > max_num:
        # Sets the largest number to the 
        # number it is being compared to
        # (updates max_num variable)
        max_num = num
        return max_num, "\n\t{}" .format(name)
    else:
        # Returns the number and both of the names
        # if the number of score or episode count are equal
        return num, "{}\n\t{}".format(max_name,name)

    
    
def find_min(num, name, min_num, min_name):
    '''Compares the given show and rating to 
        another show and rating to see which has
        the lowest rating.'''
    if num > min_num:
        # Returns the min_num and the name assiciated with
        # it if num is bigger
        return min_num,min_name
    elif num < min_num:
        # Sets the smallest number to the 
        # number it is being compared to
        # (updates min_num variable)
        min_num = num
        return num, "\n\t{}" .format(name)
    else:
        # Returns the number and both of the names
        # if the number of scores are equal
        return num, "{}\n\t{}".format(min_name,name)

def read_file(data_fp):
    '''Loops though the file provided while calling
       max and min funcitons to output the max episode
       count and rating along with their names, and the show 
       with the lowest rating. While looping through, read_file
       also calculates the average ratings of all the shows.'''
    sum_score = 0
    highest_score = 0
    highest_score_name = ""
    lowest_score = 100
    lowest_score_name = ""
    highest_episode = 0
    highest_episode_name = ""
    count = 0
    # Loops through the file
    for line in data_fp:
        # Stores and strips the names of anime
        show_name = (line[0:100]).strip()
        # Makes sure that the score is not "N/A"
        if line[100:105].strip() != "N/A":
            # Since the score isn't N/A I can make the score a float
            # without worrying about data type errors
            score = float(line[100:105])
            # Calls the max funciton using score values 
            find_max_return_values = find_max(score, show_name, highest_score, highest_score_name)
            # Sets the high score and the name of that show so it 
            # can be used the next time through the loop
            highest_score = find_max_return_values[0]
            highest_score_name = find_max_return_values[1]

            # Calls the min funciton using score values 
            find_min_return_values = find_min(score, show_name, lowest_score, lowest_score_name)
            # Sets the lowest score and the name of that show so it 
            # can be used the next time through the loop
            lowest_score = find_min_return_values[0]
            lowest_score_name = find_min_return_values[1]
            count+=1
            sum_score+= score
        # Makes sure that the episode count is not "N/A"
        if line[105:110].strip() != "N/A":
            # Since the episode count isn't N/A I can make the score a float
            episodes = float(line[105:110])
            # Calls the max funciton using episode values 
            find_max_episode_return_values = find_max(episodes, show_name, highest_episode, highest_episode_name)
            # Sets the highest episode and the name of that show so it 
            # can be used the next time through the loop
            highest_episode = find_max_episode_return_values[0]
            highest_episode_name = find_max_episode_return_values[1]
    # Calculates average and rounds it
    score_average = sum_score/count
    score_average = round(score_average,2)

    return highest_score, highest_score_name, highest_episode,highest_episode_name, lowest_score,lowest_score_name, score_average
    

     

    
        
def search_anime(data_fp, anime_name): 
    '''Loops through given data set and returns
       using ankeyword provided by the user and
       returns the number of shows with the 
       keyword in the title and the titles of the shows'''
    anime_shows = ""
    num_shows = 0
    # Loops through data
    for line in data_fp:
        title = line[0:100]
        release_season = line[110:122]
        # If the given keyword is in the title
        # add one to the count and add the formatted 
        # show to the list of shows returned 
        if anime_name in title:
            num_shows+=1
            anime_shows += ("\n\t{}{}".format(title,release_season))
    # If there are no shows with the keyword in the title
    if num_shows == 0:
        # Return the keyword and the number of shows (0)
        return num_shows, anime_name
    # If results were found 
    else:
        # Return the number of shows and all the shows with 
        # the keywoprd in the title
        return num_shows, anime_shows

def main():
    
    BANNER = "\nAnime-Planet.com Records" \
             "\nAnime data gathered in 2022"
    
    MENU ="Options" + \
          "\n\t1) Get max/min stats" + \
          "\n\t2) Search for an anime" + \
          "\n\t3) Stop the program!" + \
          "\n\tEnter option: "
    
    print(BANNER)
    user_input = input(MENU)
    user_input = user_input.lower()
    # Ensures user doessn't want to exit the prgram
    while user_input != "3":
        if user_input == "1":
            # Sets a varaible to the file the user opened
            data_fp = open_file()
            # Variables stores all the returned values from
            # read_file function
            variables = read_file(data_fp)
            # Highest episode is the 2nd index of the returned values
            # I didn't know you could use this index strategy until
            # I tried and it's pretty cool
            highest_episode = int(variables[2])
            # Adds a comma after the first number if the number of 
            # episodes are over 1000, I probably could have made some kind
            # of if else logic mixed with a while loop to account for 
            # numbers over 10000, but it wasn't necessary for the porject
            if highest_episode > 999:
                highest_episode = str(highest_episode)
                highest_episode = highest_episode[0] + "," + highest_episode[1:]
            # Prints the all the values returned by read_file() formatted
            print("\n\nAnime with the highest score of {}:".format(variables[0]))
            print("{}" .format(variables[1]))
            print("\n\nAnime with the highest episode count of {}:".format(highest_episode))
            print("{}" .format(variables[3]))
            print("\n\nAnime with the lowest score of {:.2f}:".format(variables[4]))
            print("{}" .format(variables[5]))
            print("\n\nAverage score for animes in file is {}".format(variables[6]))
            # Prints the menu and prompts for input to see if loop is continued
            user_input = input(MENU)
        elif user_input == "2":
            # Sets a varaible to the file the user opened
            anime = open_file()
            # Sets a varaible to the keyword the user input
            anime_name = input("\nEnter anime name: ")
            # Variables holds all the returned values 
            # from search_anime() function
            variables = (search_anime(anime,anime_name))
            # If no shows were returned using the keyword
            if variables[0] == 0:
                # variables[1] is the returned keyword
                print("\nNo anime with '{}' was found!".format(variables[1]))
            else:
                # Print var is the list of shows (not actually a list structure thing)
                print_var = variables[1]
                # Adds the header to the list before it is printed
                print_var = "\nThere are {} anime titles with '{}'\n".format(variables[0],anime_name) + print_var
                print(print_var)
            # Prints the menu and prompts for input to see if loop is continued
            user_input = input(MENU)
        # If user doesn't input 1, 2, or 3 print error
        else:
            print("\nInvalid menu option!!! Please try again!")
            # Prints the menu and prompts for input to see if loop is continued
            user_input = input(MENU)
            
    # If user inputs 3 print thank you message and end program   
    else:
        print("\nThank you using this program!")
# These two lines allow this program to be imported into other code
# such as our function tests code allowing other functions to be run
# and tested without 'main' running.  However, when this program is
# run alone, 'main' will execute.
#DO NOT CHANGE THESE 2 lines  
if __name__ == "__main__":
    main()