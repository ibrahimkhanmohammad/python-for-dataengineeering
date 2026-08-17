#   to count total vowels in a string
sentence = 'welcome to python programming'
count = 0
vowels = 'aeiouAEIOU'
for char in sentence:
    if char in vowels:
        count += 1
print(f'Total vowels: {count}')