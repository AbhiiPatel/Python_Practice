"""
                Topic=kwargs(Keyword args),import and packages
"""



'''
def avg(a,b,c=10,d=20,*args):
    print(f"a={a}\nb={b}\nc={c}\nd={d}\nargs={args}")

avg(1,2)
avg(1,2,4,5,6,7,8)
# avg(1,2,4,5,6,Maths=34,Science=45)      #TypeError: avg() got an unexpected keyword argument 'Maths'
'''


#kwargs=key word args(to make a dictionary)
'''
def avg(**kwargs):
    # print(kwargs)
    return sum(kwargs.values())/len(kwargs)

# avg(Maths=34,Science=35,English=45)
print(avg(Maths=34,Science=35,English=45))
'''
#common mistakes

# avg(Maths:34 ,Science:35 ,English:56)
# avg("Maths"=34,"Science"=35,"English"=56)
# avg("Maths":34,"Science":35,"English":56)
# avg(1=34,2=45,3=55)


#variable
# maths_3=56
# maths3=56
# Maths=45
# 3maths=45



#Passing a dictionary to function:
'''
def average(marks):
    return sum(marks.values())/len(marks)

subject={"Maths":45,"Science":67,"English":78}
print("Average=",average(subject))
'''



#Organizing our code in modules and packages
'''
import FunQue

print(FunQue.prime)
'''


'''
from FunQue import *

print(prime(97))
'''


'''
import FunQue as imp

print(imp.prime)
'''

'''
from FunQue import prime , ap
print(prime(5))
print(ap())
'''

'''
from FunQue import prime as p , ap as a

print(p(78))
print(a(1,3,5))
'''
'''
import FunQue 

print(dir(FunQue))
'''

#Packages

#Wrong way to import something from  a package

import myPackage

myPackage

