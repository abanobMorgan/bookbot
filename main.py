import sys

from stats import (
    count_book_words,
    count_book_chars, 
    sort_on, 
)

def get_book_text(file_path:str) -> str:
    """Reads the contents of a text file and returns it as a string.
    
    Args:
        file_path (str): The path to the text file.
        
    Returns:
        str: The contents of the text file.
    """
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents



if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    num_words = count_book_words(book_text)
    characters = count_book_chars(book_text)
    chars = sort_on(characters)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char, count in chars.items():
        if char.isalpha():
            print(f"{char}: {count}")
    print("============= END ===============")


