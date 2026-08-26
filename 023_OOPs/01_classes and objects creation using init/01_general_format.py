# A class is a blueprint for creating things
# An object is specific instance created from that blue print

# class
class Student:
    # attributes
    roll_no = 0
    name = ''
    age = 0
    gender = ''


# object / Instance
student1 = Student()
print(student1)  # it prints the address of the student1 which is an object

# changing details of student1
student1.name = 'xyz'
student1.age = 20
student1.gender = 'male'
student1.roll_no = 5

# so to print details of student1
print(student1.roll_no)
print(student1.name)
print(student1.age)
print(student1.gender)

# since object 1 is independent of object 2, changes applied in obj1 does not affect in obj2
student2 = Student()
print(student2)
print(student2.roll_no)
print(student2.name)
print(student2.age)
print(student2.gender)
