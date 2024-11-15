def main():
    frankenstein = "books/frankenstein.txt"
    frankenstein_contant = get_book_text(frankenstein)
    frankenstein_words = count_words(frankenstein_contant)
    print(count_characters(frankenstein_contant))
    
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
        if c not in characters_dict:
            characters_dict[c] = 1
        else:
            characters_dict[c] += 1
    return characters_dict

main()
