class Animal:

    def __init__(self, name: str) -> None:
        self.name: str = name

    def eat(self) -> None:
        print(f"{self.name} is eating!")

    def sleep(self) -> None:
        print(f"{self.name} is sleeping!")


class Cat(Animal):

    def meow(self) -> None:
        print(f"{self.name} is meowing!")


c = Cat("Mainecoon")
c.eat()
c.sleep()
c.meow()
