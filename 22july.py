# import time

# t1=time.time()
# print(t1)
'''
from time import time
t1=time()

for i in range(100000):
    t = (1,2,3,4,5,6,7,8,9,10)
    # print(t1)

t2=time()
print("gap=",t2-t1)
'''

#timeit module
'''
import timeit

tuple_time=timeit.timeit(stmt="t = (1,2,3,4,5,6,7,8,9,10)",number=100000)
list_time=timeit.timeit(stmt="t = [1,2,3,4,5,6,7,8,9,10]",number=100000)
print("Tuple_time=",tuple_time)
print("List_time=",list_time)

'''


#Random Module

#caesar cipher
'''
voice -> zsmgi

a + 4 = e
b + 4 = f
c + 4 = g
d + 4 = h
e + 4 = i
...

'''

from optparse import Option
import random
'''
# print(dir(random))
# print(random.random())         # [0, 1)

for i in range(10):
    # print(random.random())
    print((random.random()*4)+3)          # 3.0 to 6.99999
    # print(int((random.random()*6)+1))
'''

'''

counter1=0
counter2=0

for i in range(1000):
    n=random.uniform(3,7)
    # print(n)
    if 3<= n <5:
        counter1+=1
    else:
        counter2+=1

print("counter1=",counter1)
print("counter2=",counter2)
'''


'''
for i in range(10):
    print(random.normalvariate(10,1))
'''


'''
for i in range(10):
    # print(random.randint(1,6))                  #here 6 is included
    print(random.randrange(1,6))
'''                  


#Normal game(stone,paper,scissor)
'''
option=["stone","paper","scissor"]

c1=c2=c3=0

for i in range(10):
    c=random.choice(option)
    if c=="stone":
        c1+=1
    elif c=="paper":
        c2+=1
    else:
        c3+=1
print("c1(stone)=",c1)
print("c2(paper)=",c2)
print("c3(scissor)=",c3)
'''

from random import choice


def random_walk(path_length):
    x=0
    y=0
    option=["N","S","E","W"]
    for i in range(path_length):
        c=choice(option)
        if c=="N":
            y+=1
        elif c=="S":
            y-=1
        elif c=="E":
            x+=1
        else:
            x=-1
    
    # print(f"x={x}\ty={y}")
    return x,y



path_length=7
number_of_walks=10

for j in range(number_of_walks):
    x,y=random_walk(path_length)
    d=abs(x)+abs(y)
    print(d)
