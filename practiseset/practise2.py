# write a program to display a user entered name followed by good afternoon using input()function.
name=input("enter name :")
print(f"good afternoon  my name is  {name}") #f means format strings
print("good afternoon my name is " +name+" Shrestha") # concatenation strings


# write a program to fill in a letter template given below with name and date

letter='''
Dear <|Name|>,
You are selected !
<|Date|>
'''
print(letter.replace("<|Name|>","Binod").replace("<|Date|>","2080/06/04"))

# write a program to detect double space in string
spaceDetech="My name is Binod  shrestha  hello everyone."
print(spaceDetech.find("")) # return 0 index if there is no space
print(spaceDetech.find(" ")) # return index if there is one space 
print(spaceDetech.find("  ")) #return -1 index which have double space
print(spaceDetech.find("  ")) #return index if there is double space given

# Replace the double space from with single space

space="hello i am replacing the  double  spacing with with single space"
print(space)
print(space.replace("  "," "))


# write a program to format the following  letter using escape sequence characters.
letters="Dear Binod,this python course is nice. Thanks!"
print("Dear Binod,\n\tThis python course is nice.\nThanks")
print("Dear Binod \"hello saroj\" i am shrestha")