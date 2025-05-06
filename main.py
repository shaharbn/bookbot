from stats import get_num_words, get_num_characters, sort_dict
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file_path = sys.argv[1]
    text = get_book_text(file_path)
    num_words = get_num_words(text)
    dict_ch = get_num_characters(text)
    sorted_dict = sort_dict(dict_ch)
    print_report(file_path, num_words, sorted_dict)


def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
    
def print_report(file_path, num_words, dict_num_ch):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for d in dict_num_ch:
        if d["name"].isalpha():
            print(f"{d["name"]}: {d["num"]}")
    print("============= END ===============")
    
main()