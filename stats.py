#function that gets the number of words from a book and creates a dictionary with all characters found in book paired to number of ocurrences
def get_num_words(path_to_file):
    
    #get the book text
    with open(path_to_file) as f:
        
        #file_contents has all the words of text
        file_contents = f.read()
        
        #split book into individual words
        individual_words = file_contents.split()

        #get the word count
        total_words = len(individual_words)
    
        #initialize empty list to store lowercase words
        all_lowercase_words = []

        #convert all letters in words to lowercase if they are not already
        for word in individual_words:
            lowercase_word = word.lower()
            all_lowercase_words.append(lowercase_word)
         
        #initialize empty list to break words into characters
        separate_characters = []

        #loop through each word to split the words into their individual characters
        for word in all_lowercase_words:            
            split_characters = list(word)            
            separate_characters = separate_characters + split_characters        
        
        #initalize empty character count dictionary
        character_count_dict = {}

        #loop through the separate characters list; if character already added to dictionary then just add an occurence, otherwise add character and set to value 1
        for character_list_item in separate_characters:
            if character_list_item in character_count_dict:
                character_count_dict[character_list_item] += 1                
            
            else:
                character_count_dict[character_list_item] = 1                       

        return total_words, character_count_dict
    


#helper function for sorting in revamp_dictionary function
def sort_on(items):
    return items["num"]



#function to revamp the dictionary to only return alphabetical characters and create a list of dictionaries of format {"char": "", "num", num}
def revamp_dictionary(char_count_dict):
    #initalize empty list to store dictionaries in
    dict_revamp_list = []

    #loop through dictionary data called into function
    for char_count_key in char_count_dict:
       
       #remove any non-alphanumeric pairs
       if char_count_key.isalpha():        

        #initialize temp list to append dict_revamp_list
        temp_list = []
        
        #place updated key/value pairs in temp list
        temp_list.append("char")
        temp_list.append(char_count_key)
        temp_list.append("num")
        temp_list.append(char_count_dict[char_count_key])        

        #add the temp list to dict_revamp_list 
        dict_revamp_list.append(temp_list)    

    #initialize empty list to place new revamped dictionaries into
    revamp_dict_list = []

    #loop through dict_revamp_list to add new key/value pairs to dictionary
    for list in dict_revamp_list:
        
        #initialize temp_dict for loop to add to list
        temp_dict = {}
        
        #get values to place into temp dictionary for each loop iteration to be stored in the list of dictionaries
        temp_dict[list[0]] = list[1]
        temp_dict[list[2]] = list[3]        

        #add the temporary dictionary created to the list of dictionaries
        revamp_dict_list.append(temp_dict)

    #sort the revamped list of dictionaries to sort based on character count values from largest to smallest
    revamp_dict_list.sort(reverse = True, key=sort_on)    

    return revamp_dict_list

    

    


