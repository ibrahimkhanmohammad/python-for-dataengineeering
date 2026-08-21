#   Vowel-Starting Words Take a sentence as input. Split it into words and print how many words start with a vowel.

def vowel_count(sentence:str):
    words_list = sentence.split()
    count = 0 
    vowels = 'aeiouAEIOU'
    for word in words_list:
        if word[0] in vowels:
            count += 1
    return count

sentence = 'python is a great language and it is an exciting language'
print(vowel_count(sentence))