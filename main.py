from stats import get_num_words, revamp_dictionary
import sys






def main():

    #file path to book required to run code.  If user tries to just run main.py this will instruct them that they need to add a book file path
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    #book file path gets pulled from sys.arg and put in program to be run    
    book_file_path = sys.argv[1]
    #running function get_num_words form stats.py
    book_num_words, book_char_dict = get_num_words(book_file_path)
    #running function revamp_dictionary form stats.py
    char_list = revamp_dictionary(book_char_dict)

    #create an ouput format showing number of words in book and all alphabetical characters sorted from most to least
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {book_num_words} total words")
    print("--------- Character Count -------")
    
    #create loop counter i
    i = 0

    for list_item in char_list:
        print(f"{char_list[i]["char"]}: {char_list[i]["num"]}")
        i += 1
    
    print("============= END ===============")

    

main()