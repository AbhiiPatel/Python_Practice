'''
         topic=Tuple,methods of tuple,Set,Creating an empty set



'''


#  Tuples: Ordered and Immutable collection of members


'''
Ordered means:
+ve and -ve Index numbers
Access elements by index numbers
Slicing is possible
'''


t1 = (11, 22, 33, 11, 45, 78, 11, -43, 98, 11, -23.32, 11, 500)
# print(t1)
# print(type(t1))

'''
l1=list(t1)
print(l1)
print(list(t1))
'''

'''
name="abhi"
t2=tuple(name)
print(t2)
print(tuple(name))
print(list(name))
'''


# creating a single element tuple
'''
t3 = ("Ahmedabad", "Mumbai", "Delhi", "Bangaluru", "Surat")
country=("India")
print(country)
country=("India",)
print(country)
print(type(country))

total=(484.45,)
print(total)
print(type(total))

t4="Ahmedabad","Mumbai","Delhi","Bangaluru","Surat"
print(t4)
print(type(t4))

t5=475.494,
print(t5)

print(t4[2])

t3[1]="Pune"               #  tuples are immutable
print(t3)

l1=["India"]
print(l1)
'''


#slicing of tuple
'''
print(t1[2:7])
print(sorted(t1))
'''


#methods of tuple
'''
t1 = (11, 22, 33, 11, 45, 78, 11, -43, 98, 11, -23.32, 11, 500)
print(t1.count(11))
#print(t1.count(11,4))    # Not valid in tuples       # it takes exactly one argument

print(sum(t1))

print(t1.index(-43))
print(t1.index(11,6,9))
#print(t1.index(511, 6 , 9))              #ValueError: tuple.index(x): x not in tuple
'''


#Unpacking of collection/Multiple assignment
'''
a=10
b=20
c=30
a,b,c=10,20,30
print("a=",a)
print("b=",b)
print("c=",c)
a,b,c=b,c,a
print("a=",a)
print("b=",b)
print("c=",c)
'''

'''
student_data=("abhi",20)
name=student_data[0]
age=student_data[1]

print(f"name={name}\nage={age}")


#student_data=("abhi",20)
name,age=student_data
print(f"name={name}\nage={age}")
'''

#name,age,gender=student_data
#print(f"name={name}\nage={age}\ngender={gender}")  
#ValueError: not enough values to unpack (expected 3, got 2)

'''
result = [
    [81, 72],
    [74, 85],
    [79, 68]
]

i=1
for x,y,z in result:
    print(f"student-{i} got {x} marks in c , {y} marks in python and {z} marks in java.")
    i+=1
'''           #ValueError: not enough values to unpack (expected 3, got 2)



student_data=("Abhi",20,"Male","Cricket","M.tech")

# name,age,*others=student_data
# print(f"Name={name}\nAge={age}\nOthers details={others}")


# *others,hobby,qualification=student_data
# print(f"Others details={others}\nHobby={hobby}\nQualification={qualification}")


# name,*others,qualification=student_data
# print(f"Name={name}\nQualification={qualification}\nOthers details={others}")


# name,*others,male,*others1,qualification=student_data                      #error




#Set: Unordered and Mutable collection of members in which repeatition is eliminated

"""
Unordered means:
order is not import
no index numbers
no -ve index
no slicing
no accessing through index
"""

'''
s1={12, 34, 56, 78, 90}
print(s1)
print(type(s1))
#print(s1[1:4])                 #TypeError: 'set' object is not subscriptable
#print(s1[2])

s1.add(100)
s1.add(34)
s1.add(56)
print(s1)                    #remove duplicate


s2={53}
print(s2)

t=()
print(t)
print(type(t))                     #<class 'tuple'>

s3={}
print(s3)
print(type(s3))                    #<class 'dict'>


result={"Physics=":60,"Chemistry=":70,"Maths=":75}
print(result)
print(type(result))                ##<class 'dict'>
'''

#creating an empty set

s3=set()
print(s3)
print(set())
print(type(s3))                   #<class 'set'>
print(len(s3))  



s4=set([1,2,3,4])
print(s4)





