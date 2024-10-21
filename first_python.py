# arithmetic operator 
name="faisal"
age=99
price=3
price2=2
divide=price/price2
modulo=price%price2
print(divide)
print(modulo)
print(price**price2)
print(type(name))
print(type(age))
print(type(price))
# relational operator
a=39
b=40
print(a==b)
print(a!=b)
print(a>=b)
print(a<=b)
print(a>b)
print(a<b)
# assignment operator
a=10
a=a+10
print(a),
a-=10
print(a),
a*=10
print(a),
a/=10
print(a),
a%=10
print(a),
a**=10
# logical operators
c=10
d=15
print(not(c==d))
print(c==d and c>d)
print(c==d or c<d)
# TYpeCasting
p=3
x="5"
y=3.33
print(int(x)+y) #manual type casting
print(x+str(y))
print(p+y)#automatic type casting
# INput in Python
name=input("Entered your name : " )#string by default
age=int(input("Entered your age : " ))
Marks=float(input("Entered your marks : " ))
print("your good name is : ", name)
print("your age is : ", age)
print("your marks : ", Marks)

