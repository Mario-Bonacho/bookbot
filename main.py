from stats import words_counter
from stats import letters_counter
from stats import sort_on
from stats import print_it
import sys


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]  # use the book path provided by the user

    text = get_book_text(book_path)
    # print(text)
    num_words = words_counter(text)
    letters_count = letters_counter(text)
    letters_count_list = [{"char": k, "num": v} for k, v in letters_count.items()]
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    # print(f"{letters_count}\n")
    letters_count_list.sort(reverse=True, key=sort_on)
    print_it(letters_count_list)
    print("============= END ===============")


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()
