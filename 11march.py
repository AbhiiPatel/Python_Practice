s1="Happy birthday to"
s2="Abhi!"
print(s1+" "+s2)

'''
s3='15'
s4='20'
print(s3+s4)
'''


"""
s3=15
s4=20
print(s3+s4)
print(s3.__add__(s4))
print(s1.__add__(s2))
"""


#print(s1)
#print(s2)

'''
b="my name is "
print(b.capitalize())               #only first letter convert into capital
'''


'''
print(s1.upper())
print(s2.upper())
print(s1.lower())
print(s2.lower())
'''

#print(s1.swapcase())
#print(s2.swapcase())

#print(s1.title())              #First letter of each word convert into capital


'''
print(s1.casefold())
a="What is ß!"
print(a.casefold())

print(a.lower())
print(a.upper())
print(a.title())
print(a.swapcase())
'''


'''
print(len(s1))
s2=s1.center(50)
print(s2)
print(len(s2))

print(s1.center(50,'.'))
print(s1.ljust(50,'*'))
print(s1.rjust(50,"#"))
print(s1.ljust(50))
print(s1.rjust(30))
'''


s3 = "Students of this batch are going to rock the software industry. They are Bill Gates, Elon Musk and Steve Jobs of the future. They have potential to create another microsoft in India. But, some of them always keep their camera off."

'''
print(s3.count("e"))
print(s3.count(" e "))
#print(s1.count("a"))
#print(s2.count("A"))
print(s3.count("are"))
print(s3.count(" are "))
print(s3.count("are",25))
print(s3.count(" are ",25))
print(s3.count("are",25,55))
'''

# print(s1.encode())           #encode=  b'String' 
# print(s2.encode())


'''
print(s3.endswith("off."))
print(s3.endswith("camera off."))
print(s3.endswith("off"))
print(s3.endswith("off.",100))
print(s3.endswith("off.",50,70))
'''

'''
print(s3.startswith("T"))
print(s3.startswith("S"))
print(s3.startswith("this",12))
print(s3.startswith("this",13))
print(s3.startswith("this",12,50))
print(s3.startswith("this",13,50))
'''

# print("Sr.No\tSubject\tMarks")
'''
print("Sr.No\t" + "Subject\tMarks".expandtabs(20))
print("1\t\t\t"+"Maths\t90".expandtabs(20))
print("2\t\t\t"+"C++\t95".expandtabs(20))
print("3\t\t\t"+"Computer Science\t96".expandtabs(20))
print("4\t\t\t"+"Chemistry\t70".expandtabs(20))
print("5\t\t\t"+"Social science\t86".expandtabs(20))
'''


'''
print(s1.find("a"))
a=s1.find("b")
print(a)
print(s1.find("y",10))
print(s1.find("p"))
print(s1.find("t"))
print(s1.find("t",10))

print(s1.index("a"))
a=s1.index("b")
print(a)
print(s1.index("y",10))
print(s1.index("p"))
print(s1.index("t"))
print(s1.index("t",10))
'''


'''
x1=int(input("Enter first index:"))
x2=int(input("Enter end index:"))
print(f"Index number of 'are' between {x1} and {x2}:",s3.find("are",x1,x2))


x1=int(input("Enter first index:"))
x2=int(input("Enter end index:"))
print(f"Index number of 'are' between {x1} and {x2}:",s3.index("are",x1,x2))
'''


# find return (-1) if error occur
# index return (substring not found)if error occur




