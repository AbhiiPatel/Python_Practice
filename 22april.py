a=[1,2,3,4]
b=a
c=a.copy()

'''
print(a is b)              #Identitiy Operators  1)is  2)not is
print(a == b)
print(a is c)
print(a == c)
print(a is not c)
'''


'''
print(6 in a)             #Membership Operator   1)in  2)not in
print(7 not in a)
print(3 in a)
'''

'''
myString="my name is abhi"

print("t" in myString)
print('t' in myString)
print("a" in myString)
print("my " in myString)
print("my" in myString)
print("my  " in myString)
'''


# Decision Making: if-else

'''
num=int(input("Enter a number:"))

if num>0:
    print(f"{num} is positive")

elif num==0:
    print("It is zero")    

else:
    print(f"{num} is negative")

print("Thanks!!")
'''

#shorthand if
'''
a=int(input("Enter a number:"))
if a>0:print(f"{a} is positive")
'''


#shorthand if-else
'''
a=int(input("Enter a number"))
print("positive") if a>0 else print("negative")
'''


# write a Python code to print multiplicative table of a given number.
'''
a=int(input("Enter a number:"))
i=1
while i<=10:
    print(f"{a} x {i} = {a*i}")
    i+=1
'''



#calculator

'''
a=int(input("Enter two number:"))
b=int(input())
while True:
    print("'+'  for addition")
    print("'-'  for subtraction")
    print("'*'  for multiplication")
    print("'/'  for division")
    print("'q' foe exist")
    choice=input("Enter your choice:").lower()
    if choice == '+':
        print(f"{a}+{b}={a+b}")
    elif choice =='-':
        print(f"{a}-{b}={a-b}")
    elif choice =='*':
        print(f"{a}*{b}={a*b}")
    elif choice =='/':
        print(f"{a}/{b}={a/b}")
    elif choice =='q':
        break
    else:
        print("Invalid choice")
'''


"""
False for Python:
False, 0, 0.0, "", [], (), set(), {}
"""




'''
string="poojara"
ch='o'
list=[]
i=0
while i<len(string):
#for i in range(len(string)):
    if(string[i]==ch):
        list.append(i)
    i+=1    

print(list)        

'''

#a=int(input("Enter 10 numbers:"))
'''
b=[]

i=1
while i<=10:
    a=int(input("Enter 10 numbers:"))
    b.append(a)
    i+=1
    
print(b)
b.reverse()
c=b.copy()
print(c)

'''





