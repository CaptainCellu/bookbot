from stats import *

def main():
    print(f"{get_num_words(get_book_text("books/frankenstein.txt"))} words found in the document")

    num_char_dict = get_num_char(get_book_text("books/frankenstein.txt"))
    print(f"Number of occurrences of each character: \n{num_char_dict}")
    
    return

main()
