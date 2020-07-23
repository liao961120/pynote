# Classes

## Class, Object, Instance/Static Variables

class Date():
    pass

# Declare object `d` with class `Date`
d = Date()
# Add attibutes (instance variables) to object `b`
d.year = 2019
d.month = 5
d.day = 7

print(d)  # No print method defined for class `Date`
print(d.day)

## A Better Way to Define a Class

- Class
    - Static Variables
    - Static Functions (`@staticmethod`)
    - Constructor (Special Function): `__init__()`
    - Print Method (Special Function): `__str__()`
    - Object
        - Instance Variables
        - Instance Functions

class Date():
    ############ Static (Belong to Class) ############
    # Static variable
    doubleDigit = True
    
    @staticmethod
    def setDoubleDigit(isDouble=True):
        Date.doubleDigit = isDouble
    
    # Constructor
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
    
    # Print method
    def __str__(self):
        if Date.doubleDigit == False:
            return str(self.year) + "/" + str(self.month) + "/" + str(self.day)
        else:
            dateStr = str(self.year) + "/"
            dateStr += "0" + str(self.month) if self.month < 10 else str(self.month)
            dateStr += "/"
            dateStr += "0" + str(self.day) if self.day < 10 else str(self.day)
            return dateStr

    ############ Instances (Belong to Objects) ############
    def isLeap(self):
        if(self.year % 400 == 0):
            return True
        elif((self.year % 4 == 0) and (self.year % 100 != 0)):
            return True
        else:
            return False
    
    def isValidDate(self): # the invoker is a Date object
        if((1 <= self.year <= 3000) and (1 <= self.month <= 12)):
            daysInMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if(self.isLeap() == True):
            daysInMonth[1] = 29
        if(1 <= self.day <= daysInMonth[self.month - 1]):
            return True
        return False

d = Date(2019, 5, 7)
print(d)
Date.setDoubleDigit(False)
print(d)
print(d.isLeap(), d.isValidDate())

d2 = Date(2019, 5, 33)
print(d2.isValidDate())

## Advanced Topics

### Magic Methods

- `__init__`, `__str__`, `__eq__`, `__lt__`, `__gt__`, `__add__`

### Protected Attributes, getter & setters

<https://medium.com/bryanyang0528/python-setter-和-getter-6c08a9d37d46>