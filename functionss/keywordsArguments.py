def example_func(*args):
    print(args[0])
    print(args[2])
    sum=0
    for storeValue in args:
        sum=sum+storeValue
    return sum
print(example_func(1,2,3,4,56,77))

# keywords arguments

def kwargs_example(**kwargs):
    print(kwargs['num1'])
    print(kwargs['num2'])
    print(kwargs['num3'])
    print(kwargs.get('num1'))
    for key,value in kwargs.items():
        print(key,value)
print(kwargs_example(num1=22,num2=33,num3=44))


# all mixed arguments
def all_mix_args(num1,num2,*args,**kwargs):
    print(num1)
    print(num2)
    print(args)
    print(kwargs)
res11=all_mix_args(22,33,44,55,66,a=2,b=3,c=88)
print(res11)

# default arguments
def default(a=1):
    print(a)
print(default(4))
     