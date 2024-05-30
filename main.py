def get_book(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def count_words(book):
    words = book.split()
    return len(words)

def main():
    book = get_book("books/frankenstein.txt")
    word_count = count_words(book)
    print(book)
    print(word_count)
    
main()