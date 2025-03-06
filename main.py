from stats import word_counter
from stats import char_counter
from stats import sort_dict
import sys


def get_book_text(filepath):
    with open(filepath) as f:
        book_text = f.read()
    return book_text


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    book_words = word_counter(book_text)
    book_chars = char_counter(book_text)
    sorted_chars = sort_dict(book_chars)
    formatted_sorted_chars = "\n".join(
        f"{char['char']}: {char['count']}" for char in sorted_chars if char["char"].isalpha()
    )

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {book_words} total words")
    print("--------- Character Count -------")
    print(formatted_sorted_chars)
    print("============= END ===============")
main()