"""
    Topic=Built in Function,
"""

#Built in function

#round
'''
num=float(input("Enter any number:"))

print(round(num,2))                  #34.2356=34.24        #34.5524=34.55
print(round(num,3))
print(round(num,1))
print(round(num,0))                  #34.5678=35.0
print(round(num))                    #34.5678=35
'''

#sum
'''
print(sum(range(1,5)))
# print(sum(1,2,3,4,5))             TypeError: sum() takes at most 2 arguments (5 given)
print(sum([1,2,3],5))                    #6+5=11
print(sum([5,6,7,8,9,10], 100))          #45+100=145
'''

#zip


from sys import getsizeof


# l1=["a","b","c"]
# l2=[1,2,3]

# print(zip(l1,l2))                 #<zip object at 0x0000012C40BB8C00>
# print(dict(zip(l1,l2)))           #{'a': 1, 'b': 2, 'c': 3}   
# print(tuple(zip(l1,l2)))          #(('a', 1), ('b', 2), ('c', 3))
# print(set(zip(l1,l2)))            #{('b', 2), ('a', 1), ('c', 3)}
# print(frozenset(zip(l1,l2)))      #frozenset({('c', 3), ('b', 2), ('a', 1)})
# print(list(zip(l1,l2)))             #[('a', 1), ('b', 2), ('c', 3)]
'''
for x,y in zip(l1,l2):
    print(f"{x}\t{y}")

for x,y in list(zip(l1,l2)):
    print(f"{x}\t{y}")
'''


'''
obj=zip(l1,l2)
list_of_obj=list(zip(l1,l2))
print("size of obj=",getsizeof(obj))
print("size of list=",getsizeof(list_of_obj))
'''


'''
l1=[x for x in range(100)]
t1=tuple(l1)

print("size of l1:",getsizeof(l1))
print("size of t1:",getsizeof(t1))
'''



# We type () after a function only when we want to call it.


# Deleting & Copying a function:
'''
def primeCheck(n):
    if n == 1: return False
    for x in range(2, int(n**0.5) + 1):
        if n % x == 0:
            return False
    return True

print(primeCheck(5))
isPrime=primeCheck

del primeCheck
# print(primeCheck(5))
print(isPrime(5))
'''



#map

def cube(n):
    return n**3

# print(cube(3))

numbers=[1,2,3,4,5,6,7,8,9,10]
# print(map(cube,numbers))           #<map object at 0x00000276A643FFA0>
print(list(map(cube,numbers)))       #[1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]


numbers={1,2,3,4,5,6,7,8,9,10}
print(set(map(cube,numbers)))       #{64, 1, 512, 8, 1000, 343, 216, 729, 27, 125}






