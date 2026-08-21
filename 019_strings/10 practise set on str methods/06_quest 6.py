# Take a sentence as input. Print the longest word in that sentence

def longest_substr(sentence:str):
    word_lst = sentence.split()
    return max(word_lst, key = lambda x: len(x))

sentence = 'Python is a great programming language'
print(longest_substr(sentence))