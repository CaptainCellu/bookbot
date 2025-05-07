from stats import *

#sort_num_char
def main():
    path = "books/frankenstein.txt"
    sorted_list_of_num_char = sort_num_char(get_num_char(get_book_text(path)))

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(get_book_text(path))} total words")
    print("--------- Character Count -------")

    for element in sorted_list_of_num_char:
        if element["char"].isalpha():
            print(f"{element["char"]}: {element["num"]}")

    print("============= END ===============")

    return

main()
