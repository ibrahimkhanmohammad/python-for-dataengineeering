#   You are given two separate lists: one containing subject names and another containing the corresponding marks obtained by a student. Using dictionary comprehension, create a new dictionary that maps each subject name to its respective mark

def marks_dct(lst1, lst2):
    return{sub: mark for sub, mark in zip(lst1, lst2)}

subjects = ['mat', 'sci', 'soc', 'chem']
marks = [84, 76, 66, 38]
print(marks_dct(subjects, marks))