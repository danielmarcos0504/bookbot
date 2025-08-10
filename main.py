import sys
from stats import get_num_words, get_chars_dict, sort_characters

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    count_char = get_chars_dict(text)

    sorted_chars = sort_characters(count_char)
    print(f"""============ BOOKBOT ============
Analyzing book found at {book_path}...
----------- Word Count ----------
Found {num_words} total words""")
    print("--------- Character Count -------")

    for chars in sorted_chars:
        print(f"{chars['char']}: {chars['num']}")
    print("============= END ===============")


def get_book_text(path):
    # Your code for reading the file contents goes here
    # Example:
    with open(path) as f:
        return f.read()


main()

