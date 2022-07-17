
fruits = ["banana", "apple", "mango", "orange", "grapes", "kiwi", "guava", "sapota"]
#print(fruits)

'''                           #using while loop
i=0
while i<len(fruits):
    print(fruits[i])
    i+=1
'''


'''                          #using for loop
for i in fruits:
    print(i)
'''

'''                           #break
for i in fruits:
    if i=="orange":
        break
        
    print(i)
'''


'''
for i in fruits:              #continue
    if i=="orange":
        continue
        
    print(i)
'''


'''
for fruit in fruits:
    if fruit=="orange":
        pass

    print(fruit)
print("Thanks!")    
'''


#The pass statement is used as a placeholder for future code. 
'''
choice=int(input("Enter your choice:"))

if choice==1:
    print("Your balance")
elif choice==2:
    print("Your due")
elif choice==3:
    print("Loan emi")
elif choice==4:
    pass    
elif choice==5:
    pass    
elif choice==6:
    pass    
elif choice==7:
    pass    
elif choice==8:
    pass    
elif choice==9:
    print("Your call is being diverted to customer care executive.")
else:
    print("Invalid choice") 
'''
    

#tuple using for loop
'''
India = ("New Delhi", "Mumbai", "Chennai", "Kolkata", "Bangluru", "Ahmedabad")

for city in India:
    print(city)
'''

#set  using for loop
'''
India = {"New Delhi", "Mumbai", "Chennai", "Kolkata", "Bangluru", "Ahmedabad"}

for city in India:
    print(city)
'''


'''
myName="Python Rossum"

for character in myName:
    print(character)
'''



'''
for i in range(10):
    print(i)
'''

'''
for i in range(5,15):
    print(fruits[i])
'''


'''
for i in range(5,15,2):
    print(fruits[i])
'''




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


"""
list=[]
print("Enter the element:")

while True:
    quit=input("press 'q' for exit,'enter ' for the enter number:").lower()
    if quit=='q':
        break
    number=input()
    list.append(number)
print(list)    
"""


'''
number=int(input("Enter a number:"))
digit=len(str(number))
print(digit)
'''


'''
list=[]
for i in range(1,101):
    list.append(i)
print(list)
'''

#List comprehension:

'''
list=[i for i in range(1,101)]
print(list)
'''


#prime number

'''
number=int(input("Enter a number:"))
count=0

for i in range(1,number+1):
    if number%i == 0:
        count+=1
if count==2:
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")    
'''



n = int(input("Enter n: "))
flag = 1
for i in range(2, n):
    if n % i == 0:
        flag = 0
        print("Not Prime.")
        break
if flag == 1:
    print("Prime.")




# break - else
'''
n = int(input("Enter n: "))
for i in range(2, n):
    if n % i == 0:
        print("Not Prime.")
        break
else:
    print("Prime.")
'''







