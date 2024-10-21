#WAP to take name as input from user and print name's length
yourName=input("Enter Your Name : ")
print(len(yourName))
#write a program to count repition of $ in a string
price="$50$"
print(price.count("$"))
# WAP to check the number enter by user is even or odd
num=int(input("Enter a number : "))
if(num%2==0):
    print(f"{num} is even number")
else:
    print(f"{num} is odd number")
# WAP to find greatest of 3 entered by user
num1=int(input("Enter a number1 : "))
num2=int(input("Enter a number2 : "))
num3=int(input("Enter a number3: "))
if(num1>num2 and num1>num3):
    print(f"{num1} is greatest among 3")
elif(num2>num1 and num2>num3):   
    print(f"{num2} is greatest among 3")
else:
    print(f"{num3} is greatest among 3")
# WAP to check if a number is multiple of 7 or not
num4=int(input("Enter a number: "))
if(num4%7==0):
    print(f"{num4} is multiple of 7")
else:
    print(f"{num4} is not a multiple of 7")
# WAP to find greatest of 3 entered by user
a=int(input("enter a num1 : "))
b=int(input("enter a num2 : "))
c=int(input("enter a num3 : "))
d=int(input("enter a num4 : "))
if(a>b and a>c and a>d):
    print(f"( {a} is greater")
elif(b>c and b>d):
    print(f"( {b} is greater")
elif(c>d):
    print(f"{c} is greater")
else:
    print(f"( {d} is greater")