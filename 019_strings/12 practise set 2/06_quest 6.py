#   Take a sentence as input. Capitalize only the first letter of each word that has more than 3 characters. Keep the rest as it is

def capitalize_sentence(sentence: str):
    word_lst = sentence.split()
    result = []

    for word in word_lst:
        if len(word) > 3:
            result.append(word.capitalize())
        else:
            result.append(word)

    return ' '.join(result)


sentence = 'python is a great programming language'
print(capitalize_sentence(sentence))
