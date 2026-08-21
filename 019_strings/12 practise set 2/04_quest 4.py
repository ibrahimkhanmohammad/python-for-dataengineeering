#    Take a sentence as input. Print each word's length next to it. Example: Python (6) is (2) great (5)

def word_len(sentence:str):
    word_lst = sentence.split()
    for word in word_lst:
        print(word, len(word))

sentence = 'python is a great programming language'
word_len(sentence)
