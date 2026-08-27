# in multiple inheritance there are two parent classes with one child class, so:


class Flyer:

    def fly(self):
        print("Flyer is flying")


class Swimmer:

    def swim(self):
        print("Swimmer is swimming")


class Duck(Flyer, Swimmer):

    def both(self):
        print("Duck can swim and fly")


d = Duck()
d.fly()
d.swim()
d.both()
