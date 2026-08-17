sentence = 'welcome to python programming'

#   first way
for char in sentence:
    print(char)

#   second way
n = len(sentence)
for char in range(0, n):
    print(sentence[char])

#   to count total no.of capital and small o's we can use:
count  = 0
for i in sentence:
    if i == 'o' or i == 'O':
        count   += 1
print(count)
