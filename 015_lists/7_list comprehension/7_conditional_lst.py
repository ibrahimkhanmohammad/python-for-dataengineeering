#   Given a list of marks, use list comprehension to create a new list that contains only the marks that are above 75.
def grades(lst):
    return [el for el in lst if el > 75]

marks = [14, 76, 75, 100, 12, 35, 96, 24, 20, 13, 21]
print(grades(marks))