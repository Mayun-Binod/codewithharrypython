# write a program to add two numbers
firstNumber=401
secondNumber=66
resultNumber=firstNumber+secondNumber
resultNumber1=firstNumber-secondNumber
resultNumber2=firstNumber*secondNumber
resultNumber3=firstNumber/secondNumber
resultNumber4=firstNumber**secondNumber
resultNumber5=firstNumber//secondNumber
print(resultNumber)
print(resultNumber1)
print(f"the number is {resultNumber3:.2f}")
print(round(resultNumber3,1))
print(resultNumber3)
print(resultNumber4)
print(resultNumber5)

# write a program  to find remainder when a number is divided by 2
number=44
if number%2==0:
    print("it is even")
else:
    print("it is odd")
# or another method
numbs=44
numbs1=numbs%2==1
print(numbs1)
# check the type of variable assigned using input() function
number1=input("enter the string:")
print(type(number1))
number2=int(input("i am integer:"))
print(type(number2))
number3=float(input("this is float number:"))
print(type(number3))

# use comparison operator to find out whether a given variable is greater than "b" or not. take a=34 and b=80

a=34
b=80
a>b
print(" a variable is greater than b",a)
a<b
print(" a is less than b")


# write a program to find an average of two numbers entered by the user.
avgNum1=float(input("enter first number:"))
avgNum2=float(input("enter the second number:"))
finalAverage=(avgNum1+avgNum2)/2
print("average ouput is",finalAverage)


# write a program  to calculate the square of a number  entered by the user
numb1=int(input("enter the square number:"))
sqNumber=numb1**3
print(sqNumber)



# write a program  to find remainder when a number is divided by Z

number=44
z=3
final=number%2/z
print(final)

