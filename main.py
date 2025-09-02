from stats import words_counter
from stats import letters_counter

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    #print(text)
    num_words = words_counter(text)
    letters_count = letters_counter(text)
    print(f"{num_words} words found in the document")
    print(letters_count)

def get_book_text(path):
    with open(path) as f:
        return f.read()


main()
