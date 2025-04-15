# -- IMPORT ---------------------------------

from stats import get_word_count
from stats import get_char_count
from stats import get_char_count_sorted
import re

# -- VARIABLES ------------------------------

BOOKS_PATH = "./books/"

# -- FUNCTIONS ------------------------------

def get_book_text(book_name):
    try:
        with open(BOOKS_PATH + book_name + ".txt") as book:
            return book.read()
    except:
            print("Book does not exist.")

# -- MAIN -----------------------------------

def main():
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    word_count = get_word_count(get_book_text("frankenstein"))
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    dict_of_chars = get_char_count_sorted(get_char_count(get_book_text("frankenstein")))
    for key, value in dict_of_chars.items():
         if (re.match(r'[^[\W_]+$', key)):
              print(f"{key}: {value}")
    print("============= END ===============")

# -- EXECUTE --------------------------------

main()
