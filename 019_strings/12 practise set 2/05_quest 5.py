#    Take a sentence as input. Reverse the order of words (not the characters in each word). Example: "Python is fun" - "fun is Python"

def reverse_sentence(sentence:str):
    word_lst = sentence.split()
    word_lst = word_lst[::-1]
    return ' '.join(word_lst)

sentence = 'Python is fun'
print(reverse_sentence(sentence))