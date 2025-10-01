from stats import get_num_words, get_instances_of_chars, get_sorted_list_of_dict

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()


def main():
    filepath = "books/frankenstein.txt"
    book_text = get_book_text(filepath)
    num_words = get_num_words(book_text)
    instances_of_chars = get_instances_of_chars(book_text)
    print("============ BOOKBOT ============")
    print(f"Analyzing books found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    sorted_list_of_dict = get_sorted_list_of_dict(instances_of_chars)
    for dict in sorted_list_of_dict:
        if dict['char'].isalpha():
            print(f"{dict['char']}: {dict['num']}")

    print("============= END ===============")


main()


