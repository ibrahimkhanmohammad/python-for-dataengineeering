class Vehicle:

    def __init__(self, brand: str) -> None:
        self.brand: str = brand

    def start(self) -> None:
        print(f"{self.brand} is starting!")


class Car(Vehicle):

    def launch(self) -> None:
        print(f"{self.brand} is just launched today!")


"""
v = Vehicle("Volkswagen")
v.start()
# v.launch() # we get here attribute error because parent class have no attribute called launch
"""

# so we use;
v = Car("Virtus")
v.start()
v.launch()

# we can access both attributes with start attribute too as the child class is automatically reusing the parent class
