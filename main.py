def main():
    book_path = "books/frankenstein.txt"
    total_words = count_words(get_text(book_path))
    # print(f"{total_words} words found in the document")
    total_characters = count_char(get_text(book_path))
    report(book_path, total_words, total_characters)

def get_text(path):
    with open (path) as f:
        book_content = f.read()
    return book_content

def count_words(text):
    return len(text.split())

def count_char(text):
    chars = {}
    list_book = list(text.lower())
    for char in list_book:
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1
    return chars

def report(book_path, total_words, total_characters):
    print(f"""--- Report of {book_path} ---\n{total_words} was the total of words in the document \n""")
    
    characters = []

    for k, v in total_characters.items():
        if k.isalpha():
            characters.append({"char":k, "count":v})
    
    characters.sort(reverse=True, key=sort_dict)
    
    for dict in characters:
        print(f"The '{dict["char"]}' character was found {dict["count"]} times")

    print("--- End of report ---")

def sort_dict(dict):
    return dict["count"]

if __name__ == '__main__':
    main()