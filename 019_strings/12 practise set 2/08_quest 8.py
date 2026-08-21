'''Write a function `most_common_word(text)` that returns the most frequently occurring word in a given paragraph.

**Requirements:**

* Ignore case while counting words.
* If multiple words have the same highest frequency, return any one of them.
'''

def most_common_word(text:str):
    word_lst = text.lower().split()

    max_count = 0
    common_word = ""

    for word in word_lst:
        count = word_lst.count(word)

        if count > max_count:
            max_count = count
            common_word = word

    return common_word

text  = 'python is great and python is beauty'
print(most_common_word(text))