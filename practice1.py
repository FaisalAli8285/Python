#print sum of two number
a=int(input("Enter your first number :"))
b=int(input("Enter your second number :"))
print(f"Sum of {a} and {b} is ",a+b)#f string method allow you to directly insert variable inside the traingle
print("Sum of {} and {} is {} ".format(a,b,a+b))#format string allow you to directly insert variable inside the traingle
print("Sum of " + str(a) + "and" + str(b)+  "is" + str(a+b)) #You can concatenate strings and convert the integers to strings:
#wap input sides of square and prints its area
side=int(input("Enter first side of square :"))

print(f"Area of square is ",side**2)#f string method allow you to directly insert variable inside the traingle
# WAP to input two floating number and print their average
number1=int(input("Enter your first number :"))
number2=int(input("Enter your second number :"))
average=(float(number1)+float(number2))/2#type casting
print("average of two float number is", average)