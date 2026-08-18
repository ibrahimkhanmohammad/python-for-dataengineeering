#   Take a name as input from the user. Print its first character, its last character, and the total length of the name.

def name_stud(naam):
    print(naam[0])
    print(naam[-1])
    print(len(naam))

name = input('username: ')
name_stud(name)
