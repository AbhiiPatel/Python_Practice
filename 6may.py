#Perfect number
'''
n=int(input("Enter a number:"))
sum=0

for i in range(1,n):
    if n%i==0:
       sum+=i
if sum==n:
    print("perfect number.")
else:
    print("not perfect number.") 
'''

'''
n=int(input("Enter a number:"))
list=[]
for i in range(1,n):
    if n%i==0:
        list.append(i)
if sum(list)==n:
    print("perfect number.")
else:
    print("not perfect number.") 
'''


'''
n=int(input("Enter a number:"))
list=[i for i in range(1,n) if n%i==0]
print("perfect") if sum(list)==n else print("not perfect")
'''


'''
n=int(input("Enter a number:"))
print("perfect") if sum([i for i in range(1,n) if n%i==0])==n else print("not perfect")
'''


'''
result=[
    [56,78],
    [46,89],
    [32,95]

]
i=1
for x,y in result:
    print(f"student-{i} got {x} marks in c and {y} marks in python.")
    i+=1
'''


#Armstrong number

'''
n=int(input("Enter a positive number:"))
temp=n
power=0

while n>0:
    n=n//10
    power+=1
n=temp
sum=0
while n>0:
    digit=n%10
    sum=sum+ (digit**power)
    n=n//10

if sum==temp:
    print("armstrong.")
else:
    print("not armstrong.")
'''



n=int(input("Enter a positive number:"))
power=len(str(n))
digits=[]
for i in str(n):
    digits.append(int(i)**power)

print("armstrong") if sum(digits)==n else print("not armstrong.")


'''
n=int(input("Enter a positive number:"))
digit=[int(i)**len(str(n)) for i in str(n)] 
print("armstrong") if sum(digit)==n else print("not armstrong.")
'''


'''
n=int(input("Enter a positive number:"))
print("armstrong") if sum([int(i)**len(str(n)) for i in str(n)] )==n else print("not armstrong.")
'''





