def main():
    frankenstein = "books/frankenstein.txt"
    frankenstein_contant = get_book_text(frankenstein)
    frankenstein_words = count_words(frankenstein_contant)
    character_int_dict = count_characters(frankenstein_contant)
    print_reprot(frankenstein, frankenstein_words, character_int_dict)
    
def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def count_words(contant):
    split_contant = contant.split()
    return len(split_contant)

def count_characters(contant):
    contant = contant.lower()
    characters_dict = {}
    for c in contant:
        if c.isalpha():
            if c not in characters_dict:
                characters_dict[c] = 1
            else:
                characters_dict[c] += 1
    return characters_dict

def convert_dict_to_list(character_int_dict):
    dict_to_list = []
    for i in character_int_dict:
        dict_to_list.append({"char": i, "count": character_int_dict[i]})
    return dict_to_list
    
def sort_on(dict):
    return dict["count"]

def print_reprot(book_path, book_counted_words, character_int_dict):
    print(f"--- Begin report of {book_path} ---")
    print(f"{book_counted_words} words found in the document\n")
    converted_list = convert_dict_to_list(character_int_dict)
    converted_list.sort(reverse=True, key=sort_on)
    for i in converted_list:
        print(f"The '{i["char"]}' character was found {i["count"]} times")
    print("--- End report ---")

main()
