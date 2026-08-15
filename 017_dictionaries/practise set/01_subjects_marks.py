#   Create a dictionary of 6 subjects and their respective marks. Print the subject with the highest marks and the one with the lowest, using max() and min() functions alongside a lambda expression.


marks = {'mat': 90, 'sci': 88, 'soc': 75, 'eng': 80, 'urdu': 86, 'chem': 68}
highest = max(marks, key=lambda sub: marks[sub])
lowest = min(marks, key=lambda sub: marks[sub])

print(f'Highest marks are: {highest, marks[highest]}')
print(f'Lowest marks are: {lowest, marks[lowest]}')