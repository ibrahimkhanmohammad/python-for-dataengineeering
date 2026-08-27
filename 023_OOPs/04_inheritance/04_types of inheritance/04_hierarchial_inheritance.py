# hierarchial inheritance means, one sinle parent class and there are several multiple child classes


class Animal:

    def __init__(self, name: str):
        self.name = name

    def breathe(self):
        print(f"{self.name} is breathing")


class Dog(Animal):

    def bark(self):
        print("woof")


class Cat(Animal):

    def meow(self):
        print("Meow")


class Cow(Animal):

    def moo(self):
        print("Moo")


d = Dog("German Shepard")
c = Cat("Mainecoon")
cow = Cow("Jersey")

# all inherit breathe() from Animal, so:

d.breathe()
c.breathe()
cow.breathe()
