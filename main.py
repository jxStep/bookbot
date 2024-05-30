def get_book(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def count_words(book):
    words = book.split()
    return len(words)

def count_chars(book):

    book     = book.lower()
    alphabet = {
        'a': 0,
        'b': 0,
        'c': 0,
        'd': 0,
        'e': 0,
        'f': 0,
        'g': 0,
        'h': 0,
        'i': 0,
        'j': 0,
        'k': 0,
        'l': 0,
        'm': 0,
        'n': 0,
        'o': 0,
        'p': 0,
        'q': 0,
        'r': 0,
        's': 0,
        't': 0,
        'u': 0,
        'v': 0,
        'w': 0,
        'x': 0,
        'y': 0,
        'z': 0
    }
    
    for char in book:
        if char in alphabet:
            alphabet[char] = alphabet[char] + 1
    
    return alphabet

def print_dict(my_dict):
    sorted_dict = {k: v for k, v in sorted(my_dict.items(), key=lambda item: item[1], reverse=True)}
    for key, value in sorted_dict.items():
        print(f"The '{key}' character was found '{value}' times")

def main():

    book       = get_book("books/frankenstein.txt")
    word_count = count_words(book)
    char_count = count_chars(book)

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document\n")
    print_dict(char_count)
    print("--- End report ---")

    
main()