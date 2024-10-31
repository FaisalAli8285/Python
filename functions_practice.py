#  Write a function called cube() with one number parameter and returns the value of that number raised 
# to the third power. Test the
# function by displaying the result of calling your cube() function on
# a few different numbers
cubicNumber=int(input("enter a number to find cube : "))
def cube(number):
    result=(f"your cube is {cubicNumber**3}")
    return result
print(cube(
    cubicNumber
))
#  Write a function called greet() that takes one string parameter
# called name and displays the text "Hello <name>!", where <name> is
# replaced with the value of the name parameter.
name=input("your good name? : ")
def greet(name):
    yourName=print(f"Hello {name}")
    return name
greet(
    name
)
# Calculate Area of Circle
radius=int(input("enter a radius of circle : "))
def area(radius):
        result=print(f"area of circle is {3.14*radius**2}")
        return result
#function calling 
area(
    radius
)

tempInC=float(input("Enter temp in Celcius : "))
#construction
def temConversion(t):
    tempInkelvin=t+273.15
    result=print(f"{t} celcius is equals to {tempInkelvin} kelvin")
    return result
    #calling
temConversion(tempInC)
tempInK=float(input("Enter temp in Kelvin : "))
def temConversion(t):
    tempInCelcius=t-273.15
    result=print(f"{t} Kelvin is equals to {tempInCelcius} celcius")
    return result
    #calling
temConversion(tempInK)