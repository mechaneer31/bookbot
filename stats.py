def get_num_words(path_to_file):
    
    #get the book text
    with open(path_to_file) as f:
        #print(f"debugging: path_to_file is: {path_to_file}")

        #file_contents has all the words of text
        file_contents = f.read()
        #print(f"debugging: file_contents: {file_contents}")

        #split book into individual words
        individual_words = file_contents.split()
        #print(f"debugging: all words should be split: {individual_words}")


        #get the word count
        total_words = len(individual_words)


        #create empty list to store lowercase words
        all_lowercase_words = []

        #make all words lowercase
        for word in individual_words:
            lowercase_word = word.lower()
            all_lowercase_words.append(lowercase_word)
            all_lowercase_words_count = len(all_lowercase_words)
            #print(f"debugging: all_lowercase_words count: {all_lowercase_words_count}")
            
        #print(f"debugging: all words should be lowercase. {all_lowercase_words}")


        #Set new empty list to break words into characters
        separate_characters = []

        for word in all_lowercase_words:
            #print(f"debugging: checking lowercase words count. {word} {len(all_lowercase_words)}")
            split_characters = list(word)
            #print(f"debugging: split characters is: {split_characters}")
            separate_characters = separate_characters + split_characters
            #print(f"debugging: separate_characters is: {separate_characters}")
        
        
        
        character_count_dict = {}


        for character_list_item in separate_characters:
            if character_list_item in character_count_dict:
                character_count_dict[character_list_item] += 1
                #print(f"debugging: character {char} exists in dictionary, char value should increase by 1: {character_count_dict}")
            
            else:
                character_count_dict[character_list_item] = 1

        #print(f"debugging: character count dict is: {character_count_dict}")
                       

        return total_words, character_count_dict



def revamp_dictionary(char_count_dict):
    
    dict_revamp_list = []

    for char_count_key in char_count_dict:
       
       #remove any non-alphanumeric pairs
       if char_count_key.isalpha():
        print(f"debugging: char_count_pair is: {char_count_key}")

        #initialize temp list to append dict_revamp_list
        temp_list = []
        
        #place updated key/value pairs in temp list
        temp_list.append("char")
        temp_list.append(char_count_key)
        temp_list.append("num")
        temp_list.append(char_count_dict[char_count_key])

        print(f"debugging: temp list is: {temp_list}")

        #add the temp list to dict_revamp_list 
        dict_revamp_list.append(temp_list)
        print(f"debugging: dict_revamp_list is: {dict_revamp_list}")


    #create empty new dictionary for new key/value pairs
    #dict_revamp_dict = {}

    revamp_dict_list = []

    #loop through dict_revamp_list to add new key/value pairs to dictionary
    for list in dict_revamp_list:
        
        #create temp_dict for loop to add to list
        temp_dict = {}

        print(f"debugging: list is: {list}")
        temp_dict[list[0]] = list[1]
        temp_dict[list[2]] = list[3]

        print(f"debugging: dict_revamp_dict is: {temp_dict}")

        revamp_dict_list.append(temp_dict)

    print(revamp_dict_list)


    
    
    


