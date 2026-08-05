#   tuple is an ordered data type stores duplicate values and also store values of different data types , but it is immutable which wee cannot change or add, remove elements once it is created, unlike list

#   creation of a tuple
empty = ()
print(type(empty))

#   creation of a tuple
details = (101, 'Asta', 5.4, True)

#   creation of a single element tuple

#   here we have to use a trailing comma, when we have only one element in a tuple, such that it can be a tuple
#   wrong way
name = ('Asta')
print(type(name))   #   type is str

#   correct way
name = ('Yuno', )
print(type(name))   #   type is tuple

#   note: as we cannot update in tuples unlike lists, but we can override in tuples and in everywhere, like

marks = (10, 20, 30, 40, 50)
print(marks)
print(type(marks))

marks = marks[::-1]
print(marks)    # here it is not updating but simply override itself

#   we can also override tuple into boolean, list, int, str; same happens with lists too

names = ('asta', 'yuno', 'julius', 'yami')
print(names)
print(type(names))

names = 10
print(names)    #   it overrides the tuple into an int
print(type(names))