students = {
"anirudh": {"math": 87, "science": 92, "english": 74},
"priya": {"math": 65, "science": 78, "english": 90},
"rahul": {"math": 55, "science": 60, "english": 48},
"sneha": {"math": 95, "science": 88, "english": 82},
"karan": {"math": 70, "science": 45, "english": 63}
}

#   prints based on the name of students in alphabetical order
print(dict(sorted(students.items(),key=lambda x:x[0])))

#   sorts based on the 1st index of math
print(dict(sorted(students.items(),key=lambda x:x[1]['math'])))

#   to get sum of every mark of each student then
print(sorted(students.items(),key=lambda x: sum(x[1].values())))
#   in desc order
print(sorted(students.items(),key=lambda x: sum(x[1].values()),reverse=True))
