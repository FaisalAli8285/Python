
# // Write a for loop that prints out the integers 2 through 10, each on
#  a new line, by using the range() function.
for n in range(2, 11):
    print(n)
# Use a while loop that prints out the integers 2 through 10 (Hint:
# You’ll need to create a new integer first.)
new=1
while new<10:
    new=new+1
    print(new)
# Write a function called doubles() that takes one number as its input
# and doubles that number. Then use the doubles() function in a
# loop to double the number 2 three times, displaying each result on
# a separate line. Here is some sample output:
userNumber=int(input("Enter a number to double it :"))
def doubles(num):
   doub=num*2
   print(f"double of {num} is {doub}")
   return doub
# doubles(userNumber)
for n in range(3):
    userNumber=doubles(userNumber)
# An initial deposit, called the principal amount, is made. Each year,
# the amount increases by a fixed percentage, called the annual rate of
# return.
# For example, a principal amount of $100 with an annual rate of return
# of 5% increases the first year by $5. The second year, the increase is
# 5% of the new amount $105, which is $5.25.
# Write a function called invest with three parameters: the principal
# amount, the annual rate of return, and the number of years to calculate. 
# The function signature might look something like this:
principal=float(input("Enter a principal amount :"))
annualrate=float(input("Enter a annual rate :"))
years=int(input("Enter a number of years :"))
def invest(principalAmount,annualrate,years):
    for m in range (1,years+1):
        principalAmount=principalAmount+principalAmount*(annualrate/100)
        print(f"Year {m}: ${principalAmount:.2f}")
invest(principal,annualrate,years)



    








