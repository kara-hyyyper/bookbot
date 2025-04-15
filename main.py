# -- IMPORT ---------------------------------

from stats import get_word_count
from stats import get_char_count
from stats import get_char_count_sorted
import re
import sys

# -- VARIABLES ------------------------------

if (len(sys.argv)>1):
    BOOKS_PATH = sys.argv[1]
else:
     print("Usage: python3 main.py <path_to_book>")
     sys.exit(1)

# -- FUNCTIONS ------------------------------

def get_book_text():
    try:
        with open(BOOKS_PATH) as book:
            return book.read()
    except:
            print("Book does not exist.")

# -- MAIN -----------------------------------

def main():
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {BOOKS_PATH}...")
    print("----------- Word Count ----------")
    word_count = get_word_count(get_book_text())
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    dict_of_chars = get_char_count_sorted(get_char_count(get_book_text()))
    for key, value in dict_of_chars.items():
         if (re.match(r'[^[\W_]+$', key)):
              print(f"{key}: {value}")
    print("============= END ===============")

# -- EXECUTE --------------------------------

main()
