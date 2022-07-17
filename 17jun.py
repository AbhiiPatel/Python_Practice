#filter
#filter(function,collection)
'''
def output(num):
    if num>=avg:
        return True
    else:
        return False
    
sensor_data = [1.5, 2.5, 5.9, 3.5, 34.2, -5.7, 12.8, 44.6, 20.1]
avg=sum(sensor_data)/len(sensor_data)

print("Average=",avg)
print(list(filter(output,sensor_data)))
'''


#reduce

"""
Write a program to multiply all the members of a list.
"""
'''
myList = [1.5, 2.5, 5.9, 3.5, 34.2, -5.7, 12.8, 44.6, 20.1]

mul=1
for x in myList:
    mul *= x

print(mul)
'''

#reduce(function,collection)
'''
from functools import reduce


myList = [2,3,4,3,2]

def mul(a,b):
    return a*b

print(reduce(mul,myList))

print(mul(mul(mul(mul(2,3),4),3),2))
'''


#lambda function/Anonymous function/In-Line function

# def cube(n):
#     return n**3
'''
cube=lambda n:n**3

print(cube(3))

mul=lambda a,b:a*b

print(mul(2,3))

max=lambda x,y:print(f"{x} is max") if x>y else print(f"{y} is max")

max(67,78)
'''
"""
numbers = [1,2,3,4,5,6,7,8,9,10]
print(list(map(lambda n:n**3 ,numbers)))



sensor_data = [1.5, 2.5, 5.9, 3.5, 34.2, -5.7, 12.8, 44.6, 20.1]
avg=sum(sensor_data)/len(sensor_data)
print(list(filter(lambda n:True if n>=avg else False,sensor_data )))
"""

#Nesting of functions & Scope:

#average of factorial
'''
def avg_of_fact(p,q,r,s,t):
    
    def fact(n):
        f=1
        for x in range(1,n+1):
            f=f*x
        return f
    sum=fact(p)+fact(q)+fact(r)+fact(s)+fact(t)
    return sum/5


"""
def average(p,q,r,s,t):
    ans=(p+q+r+s+t)/5
    return ans

def fact(n):
    f=1
    for x in range(1,n+1):
        f=f*x
    return f
"""
print("Enter 5 numbers:")
a=int(input())
b=int(input())
c=int(input())
d=int(input())
e=int(input())

# print("Average of factorial=",average(fact(a),fact(b),fact(c),fact(d),fact(e)))
print("Average of factorial=",avg_of_fact(a,b,c,d,e))
'''



# scope of a variable, global variables, local variables and global keyword:

a=10                # global variable
d=40

def fun1():
    global a,d
    a -=1
    print("'a' through func1 =", a) 
    c=30          # local variable of func1
    print("'c' through func1 =", c)
    def func3():
        print("'c' through func3 =", c)
    func3()
    # d=50
    d +=10
    print("'d' through func1 =", d)



def fun2():
    print("'b' through func2 =", b)

print("'a' through main =", a)
fun1()
b = 20              # can be used by all the functions those are CALLED after this point
fun2()
print("'d' through main =", d)




