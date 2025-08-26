from stats import  get_num_of_words ,  get_num_of_characters, chars_dict_to_sorted_list
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>") 
        sys.exit(1)
    else:
        file_path =sys.argv[1]
    book_content =  get_book_test(file_path)
    num_of_words = get_num_of_words(book_content)
    count_dict = get_num_of_characters(book_content)
    sorted_count_list = chars_dict_to_sorted_list(count_dict)
    print_report(file_path, num_of_words,sorted_count_list)


def get_book_test(path):
    with open(path) as f:
        return f.read()


def print_report(book_path, num_words, chars_sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")


    
main()
    