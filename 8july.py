"""
        Topic=Module(Date,Time),Memoization

"""

#some important module:

#datetime module

#import datetime

'''
print(dir(datetime))

print(datetime.MAXYEAR)                   #9999
print(datetime.MINYEAR)                   #1
'''

#date= Attributes: year, month, and day
'''
last_lecture=datetime.date(2022,7,8)
# print(last_lecture)
# print(last_lecture.year)
# print(last_lecture.month)
# print(last_lecture.day)

valentine_day=datetime.date(2023,2,14)
gap=valentine_day-last_lecture                #answer in days
print(gap)
'''


#time=Attributes: hour, minute, second, microsecond, and tzinfo.
'''
x=datetime.time(15,25,47,5872)
print(x)
'''

#datetime=Attributes: year, month, day, hour, minute, second, microsecond, and tzinfo
'''
abhi=datetime.datetime(2002,4,13,8,5,34)
# print(abhi)
today_date=datetime.datetime.now()
# print(today_date)
gap=today_date-abhi
print("your age in days=",gap)
'''

'''
today_date=datetime.datetime.now()

example=datetime.timedelta(5)
print("target date=",today_date+example)

example=datetime.timedelta(5)
print("target date=",today_date-example)

example=datetime.timedelta(-5)
print("target date=",today_date+example)
'''



#strftime=string format time
'''
moon_mission=datetime.datetime(2021,10,20,5,45)
# print(moon_mission)
#format= Sunday, Oct 20th 2021 at 05:45am
format_date=datetime.datetime.strftime(moon_mission,"%A, %b %dth %Y at %I:%M %p")
print(format_date)
'''


#time module

import time

#print(dir(time))
# print(time.time())                    #for example=1657886063.6642058
# print(time.gmtime())


"""
t1=time.time()
def fibonacci(n):
    if n<=2:
        return 1
    else:
        return (fibonacci(n-1)+fibonacci(n-2))

print("No.\tTerm")
for i in range(1,51):
        print(f"{i}\t{fibonacci(i)}")

t2=time.time()
print("Execution time of program:",t2-t1)
"""


# Memoization - Explicit
'''
cache_memory={}
def rec_fib(n):
    if n in cache_memory.keys():
        return cache_memory[n]
    if n<=1:
        cache_memory[n]=n
        return n
    else:
        term=rec_fib(n-1)+rec_fib(n-2)
        cache_memory[n]=term
        return term


print("No.\tTerm")
for i in range(1,1001):
        print(f"{i}\t{rec_fib(i)}")
'''



#Memoization -Implicit
'''
from functools import lru_cache

@lru_cache(maxsize=100)

def rec_fib(n):
    if n<=1:
        return n
    else:
        return  rec_fib(n-1)+rec_fib(n-2)

print("No.\tTerm")
for i in range(1, 1001):
    print(f"{i}\t{rec_fib(i)}")
'''

