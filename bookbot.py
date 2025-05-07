#!/usr/bin/python3

import sys
from stats import *

def main():
    print(sys.argv)
    path = sys.argv[1]
    sorted_list_of_num_char = sort_num_char(get_num_char(get_book_text(path)))

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(get_book_text(path))} total words")
    print("--------- Character Count -------")

    for element in sorted_list_of_num_char:
        if element["char"].isalpha():
            char = element["char"]
            num = element["num"]
            print(f"{char}: {num}")

    print("============= END ===============")

    return

if len(sys.argv) == 2:
    main()
else:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
