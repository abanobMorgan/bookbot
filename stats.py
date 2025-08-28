from collections import defaultdict
def count_book_words(data:str) -> int: 
    num_words = len(data.split())
    return num_words


def count_book_chars(data:str) -> int: 
    data = data.lower()
    characters = defaultdict(int)
    for char in data: 
        characters[char] += 1
    return characters

def sort_on(items):
    sorted_items = sorted(items.items(), key=lambda x: x[1], reverse=True)
    
    return dict(sorted_items)