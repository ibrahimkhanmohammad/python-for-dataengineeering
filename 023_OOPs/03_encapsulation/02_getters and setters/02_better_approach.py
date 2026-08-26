class Student:

    def __init__(self, name: str) -> None:
        # PRIVATE VARIABLE
        # __name is name-mangled internally to:
        # _Student__name
        self.__name = name

    # PROPERTY / GETTER
    #
    # @property allows us to access the method
    # like a normal variable:
    #
    # s1.name
    #
    # instead of:
    # s1.get_name()
    @property
    def name(self):
        return self.__name

    # SETTER
    #
    # @name.setter allows us to change the
    # private variable using:
    #
    # s1.name = "Firdous"
    #
    # instead of:
    # s1.set_name("Firdous")
    @name.setter
    def name(self, new_name: str):

        # Validation
        if new_name.strip() == "":
            print("Name cannot be empty")
        else:
            self.__name = new_name


# OBJECT CREATION
s1 = Student("Ibrahim")


# GET / READ
# Python automatically calls the @property method.
print(s1.name)


# SET / MODIFY
# Python automatically calls the @name.setter method.
s1.name = "Firdous"


# GET / READ again
print(s1.name)