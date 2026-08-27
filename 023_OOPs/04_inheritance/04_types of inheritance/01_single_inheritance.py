# single inheritance means that there is only one parent class with one child class


class Animal:

    def speak(self):
        print("Animal is making some sound")


class Cat(Animal):

    def meow(self):
        print("Cat is making sound meow")


c = Cat()
c.speak()
c.meow()
