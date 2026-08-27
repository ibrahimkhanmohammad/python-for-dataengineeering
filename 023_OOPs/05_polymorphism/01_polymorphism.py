# Polymorphism is the ability of one method or interface to have different forms or behaviours. In Python, method overriding is one way to achieve polymorphism


class Animal:

    def sound(self):
        print("Animal makes a sound")


class Dog(Animal):

    def sound(self):
        print("Dog barks")


class Cat(Animal):

    def sound(self):
        print("Cat meows")


dog = Dog()
cat = Cat()

dog.sound()
cat.sound()
