#   Read a sentence from the user. Count and print the total number of vowels (a, e, i, o, u, case-insensitive) present in it, using a for loop

def count_vowels(naam):
    count = 0
    vowels = 'aeiouAEIOU'
    for char in naam:
        if char in vowels:
            count += 1
    return count

sentence = input('sentence: ')
print(count_vowels(sentence))