###########################################################

    #  Computer Project #9

    #

    #  Algorithm

    #    Prompted for file name until valid file name is provided

    #    All words in file are added to a set after clearing punctutaion.
    #    Words with apostraphes or hyphens are not included in the set.
    
    #   Dictionary is made with key being (index, character) and value
    #   being a set of words that have the character at the index
    
    #   User is promted for prefix and as long as they do not type in #,
    #   words with that prefix are returened and user is promted for another prefix

 ###########################################################
'''
Main data structure is a dictionary
   word_dic[(i,ch)] = set of words with ch at index i
'''
import string

def open_file():
    ''' Prompts for vocabulary file and returns 
    the file pointer, prompts until valid file is given.''' 
    valid_input = False
    while valid_input == False: 
        try:
            file_name = input("\nInput a file name: ")
            fp = open(file_name, encoding='UTF-8')
            return fp
        except:
            print("\n[Error]: no such file")

def read_file(fp):
    ''' Takes fp provided by open_file() and adds words 
    with a length over 1 and no inner punctuation to a set after
    removing all punctuation from around the word. (removes commas before and 
    after word but won't include a word with a - or ' in it.'''
    set_of_words = set()
    for line in fp:
        # Creates a list of every word in the line
        word_list = line.split()
        for word in word_list:
            # Strips word of outside punctiation
            stripped_word = word.strip(string.punctuation)
            # Only adds words that have only letters in them that are longer than 1 character
            if stripped_word.isalpha() == True and len(stripped_word) > 1:
                set_of_words.add(stripped_word.lower())
    return set_of_words

def fill_completions(words):
    ''' Creates a list of keys that are tuples in the form of (index, character)
    then loops through the list of words, adding words that have the character at the 
    index specified by the tuple to a set. Each set is paired with a key tuple in the
    dictionary that is returned. '''
    # Holds a list of tuples that will be the keys for the final dict
    # in the form (index,character)
    list_keys = []
    # For each word in the set, if the index and character pairing
    # isn't yet in the list then add it
    for word in words:
        for i,ch in enumerate(word):
            if (i,ch) not in list_keys:
                list_keys.append((i,ch))
    # Dict to be returned
    final_dict = {}
    # For each (index, character) in the list of keys
    for each_tuple in list_keys:
        # Creates a new set of words that will hold words that
        # match a certain criteria
        set_words_by_key = set()
        # For each word in the word list
        for word in words:
            # To bypass index errors
            try:
                # If the letter in the word at the index (gotten by the first index of the current tuple)
                # is the same as the letter in the second index of the tuple
                if word[each_tuple[0]] == each_tuple[1]:
                    # Add it to the set of words
                    set_words_by_key.add(word)
            # Just pass since the word isn't the one we are looking for if the try fails
            except:
                pass
        final_dict[each_tuple] = set_words_by_key
    return final_dict

def find_completions(prefix,word_dic):
    '''Loops through all words in the word_dic and 
    adds word with the desired prefix to the set that is returned.'''
    set_of_completions = set()
    # If the prefix isn't blank
    if prefix != "":
        for each_set in word_dic.values():
            for word in each_set:
                # If the prefix is in the word and the prefix is in the word at the start
                if prefix in word and word[0:len(prefix)] == prefix:
                    set_of_completions.add(word)
    return set_of_completions
def main():       
    set_of_words = read_file(open_file())
    word_dic = fill_completions(set_of_words)
    prefix = "go"
    while prefix != "#":
        prefix = input("\nEnter a prefix (# to quit): ")
        if prefix != "#":
            set_of_completions = find_completions(prefix,word_dic)
            # If there are words with the prefix
            if len(set_of_completions) > 0:
                string_of_words = ""
                list_of_words = []
                # Put all the words in a list so I can sort them
                for word in set_of_completions:
                    list_of_words.append(word)
                list_of_words = sorted(list_of_words, reverse = False)
                # Now that the words are sorted add them to the string that will be printed
                for word in list_of_words:
                    string_of_words += word + ", "
                # Get rid of the last comma and space
                string_of_words = string_of_words[0:-2]
                print("\nThe words that completes {} are: {}".format(prefix,string_of_words))
            else:
                print("\nThere are no completions.")
    else:
        print("\nBye")
    
if __name__ == '__main__':
    main()
