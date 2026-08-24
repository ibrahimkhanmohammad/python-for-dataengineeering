class Student:

    def __init__(self, name: str, age: int, marks: list[int]) -> None:
        self.name: str = name
        self.age: int = age
        self.marks: list[int] = marks

    def total(self) -> int:
        return sum(self.marks)

    def average(self) -> float:
        return sum(self.marks) / len(self.marks)

    def grade(self) -> None:
        # avg = sum(self.marks)/len(self.marks) since in oops we do not usually duplicate the data again and again
        avg = self.average()
        if avg >= 80:
            print('A')
        elif avg >= 65:
            print('B')
        elif avg >= 45:
            print('C')
        elif avg >= 35:
            print('D')
        else:
            print('F')


student1 = Student('Ibrahim', 20, [95, 85, 90])
total = student1.total()
average = student1.average()

print(total)
print(average)
student1.grade()
