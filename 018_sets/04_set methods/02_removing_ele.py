#   there are 4 methods in which we can remove elements in sets, remove(), discard(), pop(), clear()

fruits = {'apple', 'banana', 'cherry', 'kiwi', 'watermelon'}

#   remove() - it removes an item from the set and also it results key error if item does not exist
fruits.remove('banana')
# fruits.remove('papaya')   - returns key error as item papaya does not exist
print(fruits)

#   discard() - it discard an item from the set if exists, else nothing happen
fruits.discard('cherry')
fruits.discard('papaya')
print(fruits)

#   pop() - it randomly removes an item and it returns that item which was removed
removed_fruit = fruits.pop()
print(removed_fruit)
print(fruits)

#   clear() - it clears everything in the set and make it empty
fruits. clear()
print(fruits)