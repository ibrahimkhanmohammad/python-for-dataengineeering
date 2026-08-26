class Student:

    def __init__(self, name: str) -> None:
        self.__name = name

    # getter - traditional way
    def get_name(self):
        return self.__name

    # setter - traditional way
    def set_name(self, new_name: str):
        self.__name = new_name


s1 = Student("Ibrahim")
print(s1.get_name())
s1.set_name("Firdous")
print(s1.get_name())
