# The MRO is the order in which python searches classes when looking up a method,

class A:

    def hello(self):
        print("A")


class B(A):

    def hello(self):
        print("B")


class C(A):

    def hello(self):
        print("C")


class D(B, C):
    pass


d = D()
d.hello()  # B
print(D.mro())

# because hello method doe not there in D class, so that it goes to parent class and such that the priority will be given to B and if it does not contain hello method ten go to C and if it too does not have then goes to A
# always, use:  print(class_name.mro()) just like in this case: print(D.mro())
