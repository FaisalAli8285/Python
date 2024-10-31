# escape sequence character use for formatting purpose
str1="This is python lecture2\nand in this lecture we gonna learn about coonditional statements"
print(str1)
firstName="Faisal"
lastName="ali"
fullName=firstName+lastName
print(f"your full name is{fullName.upper()}      ")
lenFullName=len(fullName)
print(lenFullName)
# get string characters modification of string is not allowed
getNameFirstVariable=firstName[0]
print(getNameFirstVariable)
# slicing concept is very important especially when we are dealing with big data in ML it helps us to
#  access specific part of string
nameSlicing=fullName[6:len(fullName)]
print(nameSlicing)
gettingFirstnameThroughSlicing=fullName[:6]#0:6
print(gettingFirstnameThroughSlicing)
#slicing through negative indexing
nameSlicingThroughNegativeIndxing=fullName[-9:]
print("negative slicing "+nameSlicingThroughNegativeIndxing)
print(fullName.endswith("Ali"))
print(fullName.startswith("Fai"))
#capitalize the first word of string
print(lastName.capitalize())
print(lastName.replace("ali","Inayat"))
#finding index of particular characters
print(fullName.find("ali")),
#counting number of repitition of particular word
print(fullName.count("a"))
yourName=input("Enter Your Name : ")
print(len(yourName))
# Conditional Statements 
# conditional statement follow indentation means proper spacing
light=input("Enter the color of traffic light : ").lower()
if(light=="green"):
    print("move")
elif(light=="red"):
    print("stop")
elif(light=="yellow"):
    print("look")
else:
    print("Light is broken")
print("End of condition................")
percentage=float(input("Enter Your Percentage : "))
print(type(percentage))
if(percentage>=80):
    print("A+")
elif(percentage>=70 and percentage < 80):
    print("A")
elif(percentage>=60 and percentage  <70):
    print("B")
elif(percentage>=50 and percentage <60):
    print("C")
elif(percentage>=40 and percentage  <50):
    print("D")
else:
    print("fail")
driverAge=int(input("enter your age : "))
if(driverAge>=18):
    if(driverAge>80):
        print("you can't drive")
    else:
        print("cannot drive")
else:
    print("can't drive")