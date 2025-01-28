def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_of_words = count_words(text)
    num_of_characters = count_characters(text)
    print_report(num_of_characters, num_of_words)
    # print(text)


def get_book_text(path):
    with open(path) as f:
        return f.read()


def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    lower_text = text.lower()
    ch = {}
    for i in lower_text:
        if i in ch:
            ch[i] += 1
        else:
            ch[i] = 1
    return ch

def print_report(characters_dict, num_of_words):
    def sort_on(dict):
        return dict["num"]

    dict_to_list = []
    for i in characters_dict:
        if i.isalpha():
            dict_to_list.append({"character":i, "num":characters_dict[i]})

    dict_to_list.sort(reverse=True, key=sort_on)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_of_words} words found in the document\n")
    for i in dict_to_list:
        print(f"The '{i["character"]}' character was found {i["num"]} times")
    print("--- End report ---")




main()