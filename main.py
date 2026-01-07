from stats import get_num_words, revamp_dictionary
import sys






def main():

    #print("Usage: python3 main.py <path_to_book>")
    #input("Choose book to open: ")
    
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
        
    book_file_path = sys.argv[1]

    book_num_words, book_char_dict = get_num_words(book_file_path)
    #book_num_words, book_char_dict = get_num_words("/home/chris/workspace/github.com/mechaneer31/bookbot/books/test_book.txt")

    char_list = revamp_dictionary(book_char_dict)

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