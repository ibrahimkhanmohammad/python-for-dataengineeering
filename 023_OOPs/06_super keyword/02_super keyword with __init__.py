# super().__init__() is basically saying:
#     “Call the __init__ method of my parent class.”


class Person:

    def __init__(self, name: str):
        self.name = name


class Student(Person):

    def __init__(self, name: str, age: int):
        super().__init__(name)
        self.age = age


s = Student("Mohammad", 63)
print(s.age) # 63
print(s.name) # Mohammad

# flow
'''
1. Create Student object
        ↓
2. Student.__init__ starts
        ↓
3. super().__init__(name)
        ↓
4. Go to Person.__init__
        ↓
5. Person sets self.name = "Mohammad"
        ↓
6. Come back to Student
        ↓
7. Student sets self.age = 63
        ↓
8. Done
'''