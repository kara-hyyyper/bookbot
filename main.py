# -- IMPORT ---------------------------------

from stats import get_word_count
from stats import get_char_count
from stats import get_char_count_sorted

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
    word_count = get_word_count(get_book_text("frankenstein"))
    print(f"{word_count} words found in the document")
    print(get_char_count_sorted(get_char_count(get_book_text("frankenstein"))))

# -- EXECUTE --------------------------------

main()
