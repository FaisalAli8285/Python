# Write a script that creates the two variables, num1 and num2. Both
# num1 and num2 should be assigned the integer literal 25,000,000,
# one written with underscored and one without. Print num1 and num2
# on two separate lines.
num1=25000000
num2=25_000_000
print(num1),
print(num2)
#  Write a script that assigns the floating-point literal 175000.0 to the
# variable num using exponential notation, and then prints num in the
# interactive window.
num3=175e3
print(num3)
# In IDLE’s interactive window, try and find the smallest exponent N
# so that 2e<N>, where <N> is replaced with your number, returns inf
num4=-2e400
print(num4)
# Challange 5.3
# Write a script called exponent.py that receives two numbers from the
# user and displays the first number raised to the power of the second
# number
num5=int(input("enter a base : "))
num6=int(input("enter the exponent : "))
powerNumber=num5**num6
print((f"the power of number {num5}^{num6} is  {powerNumber}"  ))
print(f"sum of {0.1} and {0.2} is 0.1+0.2")
# .Write a script that asks the user to input a number and then displays that number rounded to two 
# decimal places. When run, your
# program should look like this:
roundNumber =float(input("Enter a floating number : "))
print(f"number {roundNumber} is rounded up to two decimal point {round(roundNumber,2 )} ")
# Write a script that asks the user to input a number and then displays the absolute value of that 
# number. 
absoluteNum=int (input("Enter a negative number :"))
print(f"absolute value of {absoluteNum} is {abs(absoluteNum)} ")
# Write a script that asks the user to input two numbers by using the
# input() function twice, then display whether or not the difference
# between those two number is an integer.
isInt1 =float(input("Enter a first floating number : "))
isInt2 =float(input("Enter a 2nd  floating number : "))
intCheck=isInt1-isInt2
print(f"The diff of {isInt1} and {isInt2} is integer {intCheck.is_integer()} ")
# Print the result of the calculation 3 ** .125 as a fixed-point number
# with three decimal places.
base3=3
exponentOfBase3=0.125
fixedNumber=base3**exponentOfBase3
print(f"number with three three decimal places is {fixedNumber:.3f}")
# Print the number 150000 as currency, with the thousands grouped
# with commas. Currency should be displayed with two decimal
# places.
numCurrency=150000
print(f"Here is the currency grouped with , and fixed upto two decimal places is {numCurrency:,.2f}")
ratio=0.77
print(f"here's representain of {ratio} in percentage is {ratio:.1%}")

