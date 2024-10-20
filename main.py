import os

def main():
    book_path = "books/frankenstein.txt"
        # is used for testing if path exists
        # print(os.path.exists(book_path))
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    print_report(chars_dict, num_words)

def get_book_text(path):
    with open(path, 'r') as f:
        return f.read()
    
def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def get_num_words(text):
    words = text.split()
    return len(words)

def print_report(chars_dict, num):
    print("\n--- Begin report of books/frankenstein.txt ---\n", num, "words found in the document\n")
    for key in chars_dict:
        print("The '" + key + "' character was found", chars_dict[key], "times\n")

main()
