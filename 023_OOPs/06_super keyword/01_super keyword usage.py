# The super() keyword allows a child class to call a method from its parent class. It is useful when we want to extend the parent's behavior instead of completely replacing it


class Animal:

    def eat(self):
        print("Animal is eating")

    def sleep(self):
        print("Animal is sleeping")


class Cat(Animal):

    # Override the eat() method from the parent class
    def eat(self):
        print("Cat is eating")

        # Call the parent's version of the eat() method
        super().eat()


# Create an object of the Animal class and call eat()
a = Animal()
a.eat()

# Create an object of the Cat class and call eat()
c = Cat()
c.eat()
