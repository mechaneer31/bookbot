from stats import get_num_words, revamp_dictionary



def main():
    #book_num_words, book_char_dict = get_num_words("/home/chris/workspace/github.com/mechaneer31/bookbot/books/frankenstein.txt")

    book_num_words, book_char_dict = get_num_words("/home/chris/workspace/github.com/mechaneer31/bookbot/books/test_book.txt")


    print(f"Found {book_num_words} total words")
    print(book_char_dict)
    
    data_report = revamp_dictionary(book_char_dict)

main()