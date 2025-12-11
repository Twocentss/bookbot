from stats import get_word_count, get_character_dict, char_dict_to_sorted_list
import sys

if len(sys.argv) != 2:
     print("Usage: python3 main.py <path_to_book>")
     sys.exit(1)


    
def main():
    path_to_book = sys.argv[1]
    book_contents = get_book_text(path_to_book)
    word_counter = get_word_count(book_contents)
    character_dict = get_character_dict(book_contents)
    sorted_characters = char_dict_to_sorted_list(character_dict)
    report = print_report(path_to_book, word_counter, sorted_characters)
    


def get_book_text(path_to_book):
    with open(path_to_book, "r") as book:
        book_contents = book.read()
        return book_contents

def print_report(path_to_book, word_counter, sorted_characters):
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {path_to_book}")
        print("----------- Word Count ----------")
        print(f"Found {word_counter} total words")
        print("--------- Character Count -------")
        for entry in sorted_characters:
             if not entry["char"].isalpha():
                  continue
             print(f"{entry["char"]}: {entry["num"]}")                  
             
main()


