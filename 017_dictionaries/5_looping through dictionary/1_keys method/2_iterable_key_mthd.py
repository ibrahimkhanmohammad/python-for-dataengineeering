#   we can iterate by using for loop so that we get keys, and also values
marks = {
    'science': 40,
    'maths': 80,
    'physics': 65,
    'chemistry': 50
}

for sub in marks.keys():
    print(sub)

print()

#   also to print both va;ues alongside values then
for sub in marks.keys():
    print(sub, marks[sub])