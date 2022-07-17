#Recursive Functions

#Factorial
"""
5! = 5 x 4 x 3 x 2 x 1

5! = 5 x 4! = 120
4! = 4 x 3! = 24
3! = 3 x 2! = 6
2! = 2 x 1! = 2
1! = 1 x 0! = 1

0! = 1


15! = 15 x 14!
39! = 39 x 38!


Recursive Definition:
Recursive step:
n! = n x (n-1)!
Non-recursive step
0! = 1
"""
'''
def rec_fact(n):
    if n==0:
        return 1
    else:
        return n*rec_fact(n-1)

print(rec_fact(5))
'''

#Arithmetic Progression
"""
Write a Python recursive function that returns nth term of an Arithmetic Progression.
Arithmetic Progression:
first term (a) = 7
common difference (d) = 3

AP: 7, 10, 13, 16, 19, 22, 25, 28, 31....

200th term: 199th term + 3
Recursive Definition:
Recursive Step:
nth term = (n-1)th term + d
Non Recursive Step:
1st term = a
"""
'''
def rec_ap(a,d,n):
    if n==1:
        return a
    else:
        return rec_ap(a,d,n-1) + d

a=7
d=3
print(rec_ap(a,d,7))
'''


#Geometric Progression
'''
Write a Python recursive function that returns nth term of an Geometric Progression.
Geometric Progression:
first term (a) = 3
common ratio (r) = 4

GP: 3, 12, 48, 192, 768.....

200th term: 199th term * r
Recursive Definition:
Recursive Step:
nth term = (n-1)th term * r
Non Recursive Step:
1st term = a
'''

'''
a=3
r=4

def rec_gp(a,r,n):
    if n==1:
        return a
    else:
        return rec_gp(a,r,n-1) * r

print(rec_gp(a,r,5))
'''

#Fibonacci Sequence.
"""
Write a Python recursive function that returns nth term of Fibonacci Sequence.

1, 1, 2, 3, 5, 8, 13

Recursive Definition:
Recursive Step:
nth term = (n-1)th term + (n-2)th term
Non Recursive Step:
1st term = 1
2nd term = 1
"""
# from functools import lru_cache
# @lru_cache(maxsize=100)
'''
def fibonacci(n):
    if n<=1:
        return n
    else:
        return (fibonacci(n-1)+fibonacci(n-2))


print(fibonacci(2))


num=int(input("Enter number till you print series:"))

for i in range(1,num+1):
    print(fibonacci(i))
'''


#Passing collection as argument to the function
'''
def avg(n):
    return sum(n)/len(n)


numbers = (1,2,3,4,5,6,7,8,10)
print(avg(numbers))
# result = {"Manthan":34, "Prakash":33, "Neet":35}
# print(avg(result))            #TypeError: unsupported operand type(s) for +: 'int' and 'str'
myClass = {12:"Chinmay", 23:"Vidhi", 45:"Kavya"}
print(avg(myClass))             #26.666666666666668
'''


# positional arguments, default arguments, variable length arguments, keyword arguments
"""
def avg(a, b = 5, c = 10):
    return (a + b + c)/3

print(avg(5))           # 6.666666
print(avg(5, 6))        # 7.0
print(avg(5, 6, 7))     # 6.0
"""

'''
def avg(n):
    return sum(n)/len(n)

length=int(input("Enter size of number:"))
print(f"Enter {length} numbers:")
numbers=[]

for i in range(length):
    numbers.append(float(input()))

print(numbers)
print(avg(numbers))
'''

#Arbitrary arguments,*args
#If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.

#This way the function will receive a tuple of arguments, and can access the items accordingly:
"""
def avg(*args):
    # args=list(args)
    print(args)
    print(type(args))

avg()
# avg(3)
"""

def avg(*args):
    return sum(args)/len(args)

print(avg(1,2,3,4,5))
