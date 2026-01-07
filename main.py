from stats import get_num_words, revamp_dictionary







def main():
    book_num_words, book_char_dict = get_num_words("/home/chris/workspace/github.com/mechaneer31/bookbot/books/frankenstein.txt")
    #book_num_words, book_char_dict = get_num_words("/home/chris/workspace/github.com/mechaneer31/bookbot/books/test_book.txt")
    
    char_list = revamp_dictionary(book_char_dict)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
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