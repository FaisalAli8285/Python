inputName=input("enter your full name : ")
# a) The total number of characters in the string 
print(len(inputName))
# b) The string repeated 10 times 
repeatedString=(inputName + "\n") *10
print(repeatedString )
# c) The first character of the string 
print(f"first character of string : {inputName[0:1]}")
# d) The first three characters of the string 
print(f"first three character of string : {inputName[0:3]}")
# e) The last three characters of the string 
print(f"last three character of string : {inputName[-3:]}")
# (f) The string backwards 
print(f"reversed string : {inputName[::-1]}")#start:stop:step
# (g) The seventh character of the string  
print(f"seventh character of string : {inputName[6:7]}")
# (h) The string with its first and last characters removed
print(f"string without first and last character of string : {inputName[1:len(inputName)-1]}")
# i) The string in all uppercase 
print(f"string in upper case : {inputName.upper()}")
# The string with every “a” replaced with an “e” 
print(f"string with every a replaced with an e : {inputName.replace('a','e')}")
# The string with every letter replaced by a “space”
# Question 03: Write a program that asks the user for their name and how many times to print it. The program 
# should print out the user’s name the specified number of times. 
print("hi")
myName=input("enter how many times you want to print your name :")
number=int(input("enter how many times you want to print your name"))
repition=((yourname + "\n")*number)
print(f"your repeated name : {repeated}")