# l=[]
# for store in range(1,101):
#     l.append(store)
#     print(l)
# print(l)

# n=[m for m in range(1,101)]
# print(n)

# n=[m for m in range(1,101) if m%2==0]
# print(n)

# s="Binod"
# d=[g for g in s]
# print(d)

# without list comprehension
# list33=[]
# for f in range(6):
#     list33.append(f)
# print(list33)
# list comprehension
# l2=[f for f in range(6) if f%2==0]
# print(l2)

# list44=[]
# for i in range(11):
#     if (i%2==0):
#         if (i%3==0):
#            list44.append(i)
# print(list44)
# l3=[i for i in range(11) if i%2==0 if i%3==0]
# print(l3)


# list2=[0,1,2,3,4,5,6,7,8,9,10]
# list22=[]
# for i in list2:
#     list22.append(i+1)
#     # print(list22)
# print(list22)

# with list comprehension
# l1=[i+1 for i in range(11)]
# print(l1)

# # without list comprehension
list55=[]
for store in range(11):
    if (store%2==0):
        list55.append(store)
    else:
        list55.append("invalid")
print(list55)

# list comprehension
list555 = [store1 if store1 % 2 == 0 else "invalid" for store1 in range(11)]
print(list555)
