# Type annotations in Python are used to tell developers what type of data a variable, function parameter, or return value is expected to have

'''
Important point
Type annotations do not normally affect Python's execution. Python does not automatically enforce them.

They mainly help with:

Readability — developers can easily understand the expected data type.
Code sharing — other developers can understand and work with your code more easily.
Developer tools — IDEs and type checkers can detect possible type-related mistakes.
'''

# without type annotation:
'''
def calculate(a, b):
    return a + b
print(calculate('5', 5)) # TypeError: can only concatenate str (not "int") to str
'''


# with type annotation:
def calculate(a: int, b: int) -> int:
    return a + b


print(calculate('5', 5))  # it'll tell the user that it is only int type
