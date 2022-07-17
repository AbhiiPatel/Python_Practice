'''
Functions Examples:

'''


#1) Write a Python function to find factorial of a number given in its argument. Develop a main program that takes five integers from user and print sum of their factorials using that function.
'''
def factorial(n):
    """
    This function return factorial of number.
    """
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    return fact


a=int(input("Enter number :"))
b=int(input("Enter number :"))
c=int(input("Enter number :"))
d=int(input("Enter number :"))
e=int(input("Enter number :"))
sum=factorial(a)+factorial(b)+factorial(c)+factorial(d)+factorial(e)
print(f"{a}! +{b}! +{c}! +{d}! +{e}! ={sum}")
print(factorial.__doc__)
'''


#2) Write a Python function that prints whether the number passed in its argument is prime or not. Using a main program pass the number given by the user to that function.


def prime(n):
    
    count=0
    for i in range(1,n+1):
        if n%i ==0:
            count+=1
    if count==2:
        print(f"{n} is a prime number.")        
    else:
        print(f"{n} is not a prime number.")    


# num=int(input("Enter number:"))
prime(97)



#3)  Make a Python program that uses a function to find average of 5 given numbers and write Python main program that takes 5 integers from user, uses the factorial function that you have already written in ex-1 to find factorial of each one of them and using average function prints the average of factorials of them.
'''
def factorial(n):
    """
    This function return factorial of number.
    """
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    return fact

def average(x,y,z,m,n):
    """
    This function return average of 5 numbers and average of factorial of them
    """
    avg=(x+y+z+m+n)/5
    sum=factorial(a)+factorial(b)+factorial(c)+factorial(d)+factorial(e)
    ans=sum/5
    print(f"Average of factorial:{ans}")
    print(f"Average of number:{avg}")
    # return avg

a=int(input("Enter number :"))
b=int(input("Enter number :"))
c=int(input("Enter number :"))
d=int(input("Enter number :"))
e=int(input("Enter number :"))

average(a,b,c,d,e)
# print(factorial.__doc__)
# print(average.__doc__)
'''



#4) Make a Python program that uses a function to find nth term of an arithmetic progression whose first term is a & common difference is d.
    # ap:
    # first term = a = 5
    # difference = d = 4
    # ap = 5, 9, 13, 17, 21, 25,...
    # nth term = a + (n-1)d


def ap(x,y,n):
    """
        This function return nth term of arithmetic progression.
    """
    term=x+(n-1)*y

    return term

list=[]
size=int(input("Enter size:"))
print("Enter element:")

for i in range(0,size):
    ele=int(input())
    list.append(ele)
# print(list)    

a=list[0]
b=list[1]

d=b-a

t=ap(a,d,size)
print(f"{size}th term of the serires:{t}")



#5) Make a Python program that uses a function to find nth term of an geometric progression whose first term is a & common ratio is r.
'''
def power(n,e):
    ""
        This function return power of number.
    """"
    ans=1
    for i in range(e):
        ans*=n

    return ans        
# print(power(2,5))

def gp(a,p):
    """
         This function return nth term of geometric  progression.
    """
    ans=a*p
    return ans


list=[]
size=int(input("Enter size:"))
print("Enter element:")

for i in range(0,size):
    ele=int(input())
    list.append(ele)

a=list[0]
b=list[1]

r=b/a
p=int(power(r,size-1))

t=gp(a,p)

print(f"{size}th term of the serires:{t}")
'''



#6)  Make a function that checks whether the given number is a perfect number or not. Make a Python program that uses this function to print all the perfect numbers between a given range. A perfect number is one whose all factors (excluding itself), when added up, you get the number itself. eg, factors of 6: 1, 2, 3, 6 & 1+2+3 = 6. so 6 is a perfect number.
'''
def perfect(n):
    """
        This function for perfect number.
    """
    sum=0
    for i in range(1,n):
        if n%i==0:
            sum+=i
    return sum
        
num=int(input("Enter number:"))
ans=perfect(num)

if ans==num:
    print(f"{num} is perfect number.")
else:
    print(f"{num} is not perfect number.")


r1=int(input("Enter range r1:"))
r2=int(input("Enter range r2:"))
for j in range(r1,r2+1):
        
        if j==perfect(j):
            print(j)
'''



#7) Write a Python function that determines whether the number given in its argument is a Prime number or not. Build a main program that takes two integers from user and print all the Prime numbers between those two integers using that function.
'''
def prime(n):
    """
        This function for prime number.
    """
    
    count=0
    for i in range(1,n+1):
        if n%i ==0:
            count+=1
    return count   


num=int(input("Enter number:"))
ans=prime(num)

if ans==2:
    print(f"{num} is a prime number.")        
else:
    print(f"{num} is not a prime number.") 


r1=int(input("Enter range r1:"))
r2=int(input("Enter range r2:"))

for i in range(r1,r2+1):
    c=prime(i)
    if c==2:
        print(i)
'''


#8) Write a Python function that determines whether the number given in its argument is Armstrong number or not. Build a main program that takes two integers from user and print all the Armstrong numbers between those two integers using that function.

'''
def armstrong(n):
    """
        This function for armstrong number.
    """
    list=[]
    power=len(str(n))
    for i in str(n):
        list.append(int(i)**power)
   
    return sum(list)


num=int(input("Enter number:"))

ans=armstrong(num)
if ans==num:
    print(f"{num} is armstrong number.")
else:
    print(f"{num} is not armstrong number.")


r1=int(input("Enter range r1:"))
r2=int(input("Enter range r2:"))

for i in range(r1,r2+1):
    if i==armstrong(i):
        print(i)
print(armstrong.__doc__)
'''


