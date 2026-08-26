# Encapsulation:
# Keeping data and the methods that work on that data
# together inside a class.

class Bank:

    # __init__ is a constructor.
    # It runs automatically when we create an object.
    def __init__(self, name: str, balance: int) -> None:

        # PUBLIC VARIABLE
        # No underscore before the variable name.
        # It can be accessed directly from outside the class.
        self.name: str = name

        # PRIVATE VARIABLE
        # Double underscore (__) is used.
        # Python performs NAME MANGLING on this variable.
        #
        # __balance is internally changed approximately to:
        # _Bank__balance
        #
        # It is intended to be accessed only through the class's methods.
        self.__balance: int = balance

    # PUBLIC METHOD
    # This method can be called from outside the class.
    def deposit(self, amount: int):

        # Validation:
        # We don't allow a negative deposit.
        if amount < 0:
            print("Invalid Amount")

        else:
            # We are modifying the PRIVATE variable
            # through a public method.
            #
            # __balance is automatically treated as:
            # _Bank__balance
            self.__balance += amount


# OBJECT CREATION
# b1 is an object (instance) of the Bank class.
b1 = Bank("Ibrahim", 20000)


# PUBLIC VARIABLE
# name is public, so we can access it directly.
print(b1.name)


# NAME MANGLING
#
# We normally cannot do:
# print(b1.__balance)       # ❌ AttributeError
#
# Python changes:
#
#     __balance
#          ↓
#     _Bank__balance
#
# Therefore, we can technically access it using
# the mangled name.
print(b1._Bank__balance)


# Calling the PUBLIC METHOD
#
# deposit() modifies the private __balance variable.
b1.deposit(2000)


# After depositing 2000:
#
# Previous balance = 20000
# Deposit          = 2000
# New balance      = 22000
#
# Accessing the name-mangled variable:
print(b1._Bank__balance)