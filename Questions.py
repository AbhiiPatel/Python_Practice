
#Home Work

'''
#1
a=input("First Name:")
b=input("Middle Name:")
c=input("Surname:")
print(f"{a[0]}.{b[0]}.{c}")
'''

'''
#2
a="happy birthday"
print(a.replace("h","H",1))
'''


'''
#3
a="color"
b="full"
print(a.replace(a[0:3],b[0:3]))
print(b.replace(b[0:3],a[0:3]))
'''

'''
#4
a="superstar"
b="rocking"
print(a.replace(a[0:3],b[-3: ]))
print(b.replace(b[-3: ],a[0:3]))
'''


'''
#5
a="Keep yourself mute while not speaking."
b=a.replace(" ","_",1)
c=b[::-1]
d=c.replace(" ","#",1)
e=d[::-1]
print(e)
'''


'''
#6
a=input("Enter a String:")
temp=a.lower()
vowels=temp.count("a")+temp.count("e")+temp.count("i")+temp.count("o")+temp.count("u")
space=temp.count(" ")
others=len(a)-vowels-space
print(f"Vowels:{vowels}\nWhite spaces:{space}\nOther character:{others}")
'''

'''
#7
a="This is the lion in the cage."
print(a.replace("the",""))
'''


#date=22/04/22

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


#if-else examples: 


'''
a=int(input("Enter the percentage:"))

if a<35:
    print("F")
elif a>=35 and a<=44:
    print("E")
elif a>=45 and a<=54:
    print("D")
elif a>=55 and a<=64:
    print("C")    
elif a>=65 and a<=74:
    print("B")    
else:
    print("A")    

'''


'''
year=int(input("Enter a year:"))    

if (year%4==0) and  (year%400==0 or year%100!=0):
    print(f"{year} is leap year")
else:
    print(f"{year} is not leap year")

'''


'''
print("Enter three number:")
a=int(input())
b=int(input())
c=int(input())

if a>b:
    if a>c:
        print(f"{a} is the largest number.")
    else:
        print(f"{c} is the largest number.")

else:
    if b>c:
        print(f"{b} is the largest number.")
    else:
        print(f"{c} is the largest number.")    

'''


'''
print("Enter X coordinate:")
x=int(input())
print("Enter Y coordinate:")
y=int(input())

if x>0 and y>0:
    print(f"First Quadrant")
elif x<0 and y>0:
    print(f"Seconf Quadrant")
elif x<0 and y<0:
    print("Third Quadrant") 
else:
    print("Fourth Quadrant")    
'''


'''
maths=int(input("Enter Maths mark:"))
phy=int(input("Enter physics mark:"))
chem=int(input("Enter chemistry mark:"))


total=maths+phy+chem
total1=maths+phy


if (maths>=65) and (phy>=55) and (chem>=50) and ((total>=190) or (total1>=140)):
    print("The candidate is  eligible.")
else:
    print("The candidate is  not eligible.")    
'''


#Loop examples

'''
n=int(input("Enter integer:"))
count=0

while(n!=0):
    n=n//10
    count +=1

print(count)
'''


'''

list=[]

n=int(input("Enter number of elements to store in list:"))
print("Enter the element:")

i=0
while i<n:
    ele=int(input())
    list.append(ele)
    i+=1
print(list)    
'''


'''
a=[45,67,43,22,78]
i=0
while i<len(a):
    print(a[i])
   # print("\n")
    i+=1
'''


'''
no1=int(input("Enter number 1:"))
no2=int(input("Enter number 2:"))

print("Before swapping:",no1,no2)
no1=no1 ^ no2
no2=no1 ^ no2
no1=no1 ^ no2

print("After swapping:",no1,no2)
'''
 
'''
l=input("Enter 10 number:").split(" ")
index= input("enter the number:")
#l.pop(index)           #for index 
l.remove(index)         #for element
print(l)
'''


#for loop

'''

list=[]
size=int(input("Enter the size of elements to store in the list:"))
print("Enter the element")

for i in range(0,size):
    ele=input()
    list.append(ele)
print("The list is:")
print(list)
'''


'''
list=[]
print("Enter the element:")

while True:
    quit=input("press 'q' for exit,'enter ' for the enter number:").lower()
    if quit=='q':
        break
    number=input()
    list.append(number)
print(list)    
'''


'''
number=int(input("Enter a number:"))
digit=len(str(number))
print(digit)
'''
