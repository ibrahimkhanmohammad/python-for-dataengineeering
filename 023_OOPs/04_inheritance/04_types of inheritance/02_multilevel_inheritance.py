# in multilevel inheritance there are grandparent with parent and a child class


class Animal:

    def speak(self):
        print("Animal is making some sound")


class Cat(Animal):

    def meow(self):
        print("Cat is making sound meow")


class Kitten(Cat):

    def feed(self):
        print("Mother cat is feeding it's child kitten")


k = Kitten()
k.speak()
k.meow()
k.feed()
