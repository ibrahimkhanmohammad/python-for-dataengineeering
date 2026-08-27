# Python does support Method Overloading but doe snot support Method Overriding

# Metjod Overriding: Child classes does override (replaces) the methods of parent's class with their own version


class Animal:

    def eat(self) -> None:
        print("Animal is eating!")


class Cat(Animal):

    def eat(self) -> None:
        print("Cat is eating!")


class Dog(Animal):

    def eat(self) -> None:
        print("Dog is eating!")


a = Animal().eat()
c = Cat().eat()
d = Dog().eat()
