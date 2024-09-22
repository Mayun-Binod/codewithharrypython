# # Write a function that takes two numbers as arguments and returns their sum.
# def sum_numbers(num1,num2):
#     sumResult=num1+num2
#     return sumResult
# res=sum_numbers(44,33)
# print(res)

# # Write a function to check if a given number is even or odd.
# def check_odd_even(number):
#     remainder=number%2
#     if remainder==0:
#         return("i am even number")
#     else:
#         return("i am odd number")
# res1=check_odd_even(5)
# print(res)
# # by user input

# def user_even_odd():
#     number=int(input("enter the number:"))
#     remainder=number%2
#     if remainder==0:
#         return("even")
#     else:
#         return("odd")
# res2=user_even_odd()
# print(res2)

# # Factorial: Write a function to calculate the factorial of a given number.
# def getfactorial():
#     number=int(input("enter the factorial number:"))
#     factorial=1
#     for storeValue in range(1,number+1):
#         factorial=factorial*storeValue
#     return factorial
# res3=getfactorial()
# print(res3)

# # Write a function to calculate the multiplication of a given number.
# def getMultiplication():
#     number4=int(input("enter the number:"))
#     print(f"multipliaction of {number4} is:")
#     for i in range(1,11):
#         multiple=number4*i
#         print(f"{number4}X{i}={multiple}")
# getMultiplication() 

# Write a function that checks if a given number is prime or not.

def getPrime():
    prime=int(input("enter any number:"))
    if prime < 2:
        print("not a prime")
        return
    for i in range(2,int(prime**0.5)+1):
        if prime%i==0:
            print("not a prime")
            return
        else:
            print("prime number")
getPrime()
