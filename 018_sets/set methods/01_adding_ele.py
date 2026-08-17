#   there are 3 methods in which we can add elements in sets, add(), update(), using add() with duplicate values

fruits = {'apple', 'banana', 'cherry', 'kiwi'}

#   add() - it only adds single element
fruits.add('guava')
print(fruits)

#   update() - it adds multiple elements at a once from any iterable
fruits.update(['strawberry', 'watermelon'])
print(fruits)

#   adding element which is already present
fruits.add('watermelon')
print(fruits)