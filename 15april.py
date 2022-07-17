numbers = [11, 22, 33, 11, 45, 78, 11, -43, 98, 11, -23.32, 11, 500]


'''
n2=numbers.copy()
print("numbers=",numbers)
print("n2=",n2)

n3=numbers
print("n3=",n3)

numbers.append(1000)

print("numbers=",numbers)
print("n3=",n3)
print("n2=",n2)




"""
n3.clear()
print("numbers=",numbers)
print("n3=",n3)
print("n2=",n2)
"""


del numbers
#print("numbers=",numbers)
print("n3=",n3)
print("n2=",n2)
'''


n1 = [11, 22, 33, 11, 45, 78, 11, -43, 98, 11, -23.32, 11, 500]


'''
print(n1.count(11))
#print(n1.count(11,3,10))    Error->count takes exactly one argument

print("length before:",len(n1))
n4=["ahm","bom","del","rtp"]
#n1.append(n4)
n1.extend(n4)
print(n1)

print("length after:",len(n1))
'''


'''
print(n1.index(-43))
print(n1.index(11,4,7))    #second argument=internal & third argument=external
print(n1.index(-43,2))
'''


'''
print(len(n1))
n1.insert(12,"Abhi")         #insert expected 2 argument and insert string at given index 
print(n1)

print(n1.pop())         #LIFO manner
print(n1.pop())
print(n1)
n1.insert(12,500)
print(n1)
#print(n1.pop(78))

print(n1.pop(1))         #pop the element at given index
print(n1)


x=9
n1.pop(x)
print(n1)
n1.remove(11)       #remove has only 1 argument
print(n1)
'''


'''
n1  = [11, 22, 33, 11, 45, 78, 11, -43, 98, 11, -23.32, 11, 500]
# print(sorted(n1))
n1.sort()
n1.reverse()
print(n1)
'''


print(2500/365)
print(2500//365)             #     //     Floor division/Integer division
print(2**3)                  #     **     Exponent/Power
print(round(2500/365))
print(round(2500/365,3))
print(34<23)
print(34>23)

print(3 & 5)
print(3 | 5)
print(3 ^ 5)
print(~3)

print(25<<1)
print(25>>1)

print(25<<3)