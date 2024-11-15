def main():
    frankenstein = "books/frankenstein.txt"
    frankenstein_contant = get_book_text(frankenstein)
    frankenstein_words = count_words(frankenstein_contant)
    
def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def count_words(contant):
    split_contant = contant.split()
    return len(split_contant)

main()
