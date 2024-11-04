def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_character = get_character_counts(text)
    print(f"{num_words} words found in the document")
    for k, v in num_character.items():
        print(f"'{k}' character was found {v} times")


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()


def get_character_counts(text):
    words = {}
    text_lowercase = text.lower()
    for string in text_lowercase:
        if string in words:
            words[string] += 1
        else:
            words[string] = 1

    return words


main()
