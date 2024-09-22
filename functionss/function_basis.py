def parameter(num):
    print(num)
parameter(44)

def print1(call):
    print(f"i am function1 {call}")
    print(f"i am function 2 {call}")
    print(f"i can all function {call}")
print1("number1")
print1("number 2")
print1("number 3")


def welcome_message():
    pass
welcome_message()


def product(num1,num2,num3):
    result=num1*num2*num3
    print(f"result:{result}")
    return result
res=product(33,44,55)
print(res)

def return1(sum1,sum2):
    result=sum1+sum2
    result1=sum1-sum2
    return result,result1
res,res1=return1(44,22)
print(res,res1)
# another return in tuple
ress=return1(44,55)
print(ress)

def api_call():
    binod="hello handsome"
    return binod

if api_call()==None:
    print("does not return anything"  )
else:
    print("return value ")  
    