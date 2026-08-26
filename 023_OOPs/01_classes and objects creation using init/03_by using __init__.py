'''
The init method in Python allows for the initialization of an object's attributes at the time of its creation, ensuring that each instance starts with the necessary values and properties. This helps keep code organized and scalable by allowing customization of object attributes right from the start
'''

class Student:

    def __init__(self, roll_no: int, name: str, age: int, gender: str) -> None:
        self.roll_no = roll_no
        self.name = name
        self.age = age
        self.gender = gender

    def display_details(self) -> None:
        print(f'Roll no: {self.roll_no}')
        print(f'Name: {self.name}')
        print(f'Ae: {self.age}')
        print(f'Gender: {self.gender}')


student1 = Student(1, 'Ibrahim', 20, 'Male')
student1.display_details()
print(student1)  # it prints the address of the student1 which is an object
