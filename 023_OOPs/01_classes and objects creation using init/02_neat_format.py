# class
class Student:
    # attributes
    roll_no = 0
    name = ''
    age = 0
    gender = ''

    # method 1
    def set_details(self, roll_no: int, name: str, age: int, gender: str) -> None:
        self.roll_no = roll_no
        self.name = name
        self.age = age
        self.gender = gender

    # method 2
    def display_details(self):
        print(f'Roll no: {self.roll_no}')
        print(f'Name: {self.name}')
        print(f'Ae: {self.age}')
        print(f'Gender: {self.gender}')


# object / Instance
student1 = Student()
print(student1)  # it prints the address of the student1 which is an object
student1.set_details(1, 'Ibrahim', 20, 'Male')
student1.display_details()

student2 = Student()
print(student2)
print(student2.display_details())
