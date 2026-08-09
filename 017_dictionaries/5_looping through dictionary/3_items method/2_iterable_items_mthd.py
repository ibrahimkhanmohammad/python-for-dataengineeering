#   we can iterate by using for loop so that we get both keys and values, such that
marks = {
    'science': 40,
    'maths': 80,
    'physics': 65,
    'chemistry': 50
}

for sub, mark in marks.items():
    print(sub, mark)