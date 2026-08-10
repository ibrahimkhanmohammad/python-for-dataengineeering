marks = {
"akshy": [43, 12, 98, 10, 22],
"priya": [76, 55, 34, 89],
"rahul": [20, 45, 67, 30, 88],
"sneha": [91, 73],
"karan": [38, 82, 47, 95, 29]
}

#   it sorts based on alphabetical order of names of students
print(dict(sorted(marks.items(), key=lambda x:x[0])))
#   sorts based on the last subject marks of each student
print(dict(sorted(marks.items(), key=lambda x:x[1][-1])))

#   as x[1] is list so for finding sum we can use built-in sum function
print(dict(sorted(marks.items(), key=lambda x:sum(x[1]))))
#   in desc order
print(dict(sorted(marks.items(), key=lambda x:sum(x[1]),reverse=True)))




