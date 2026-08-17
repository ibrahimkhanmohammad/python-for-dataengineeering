#   printing only unique words from a sentence

sentence = 'python is powerful and python is beautiful'
words = set(sentence.split())
#   the split() is a method in strings as we are discussing later, but it split the sentence or string contents, such that we are using set() constructor in order to convert string into a set

for word in words:
    print(word)     #   order may vary(set is unordered)