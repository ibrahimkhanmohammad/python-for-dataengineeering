# Class variable → belongs to the class, and normally has the same value shared by all objects
# Instance variable → belongs to an individual object, so each object can have its own value


class Student:

    college = "SRKR engineering college"  # class variable

    def __init__(self, name: str, age: int) -> None:
        self.name: str = name
        self.age: int = age


s1 = Student("Ibrahim", 20)
s2 = Student("Mohammad", 19)

print(s1.name)  # instance variables
print(s2.name)  # instance variables

print(Student.college)  # class variable
print(s1.college)  # accessing class variable through instance
print(s2.college)  # accessing class variable through instance

# way to change class variables
Student.college = "Tirumala junior college"
