from stats import get_word_count, get_char_count
import sys

def get_book_text(file_path):
    with open(file_path) as f:
        contents = f.read()
    return contents


def main(file):
    if len(sys.argv) < 2:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)
    
    book_text = get_book_text(sys.argv[1])
    print("============ BOOKBOT ============")
    print(f'analyzing book found at {file}')
    print('----------- Word Count ----------')
    print(f'Found {get_word_count(book_text)} total words')
    print('--------- Character Count -------')
    get_char_count(book_text)
    print('============= END ===============')


main(sys.argv)