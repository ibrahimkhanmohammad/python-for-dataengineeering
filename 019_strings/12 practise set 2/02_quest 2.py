#    Take a paragraph as input. Print the count of unique words in it (case insensitive).

def count_unique(paragraph:str):
    word_lst = paragraph.lower().split()
    # used set() constructor bcoz it gives unique items
    unique_words = set(word_lst)
    return len(unique_words)

paragraph = 'Python is crazy and python is a beautiful programming language'
print(count_unique(paragraph))