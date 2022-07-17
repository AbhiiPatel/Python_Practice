'''
                topic=set methods,set operation methods,Frozenset,Dictionary

'''
#set=Unordered and mutable


s1 = {11, 22, 33, 11, 45, 78, 11, -43, 98, 11, -23.32, 11, 500}

s1.add(100)
# print(s1)
# s1.clear()
# print(s1)

# del s1
# print(s1)             #NameError: name 's1' is not defined

'''
s2=s1.copy()
s3=s1

print("s1=",s1)
print("s2=",s2)
print("s3=",s3)
'''

# s1.discard(-23.32)
# print(s1)
# s1.remove(-43)
# print(s1)
# s1.discard(5000)             #no error
# print(s1)                    
# s1.remove(5000)              #KeyError: 5000
# print(s1)    

'''
print(s1.pop())
print(s1)

print(len(s1))
s4 = {1000, 78, 2000, 45, 3000}
s1.update(s4)
print(s1)
print(len(s1))
'''



#set operation methods

s1 = {1,2,3,4}
s2 = {3,4,5,6}
s3 = {5,6,7,8}
universal={i for i in range(1,11)}
# print(universal)
'''
u=s1.union(s2)
print(u)
u=s2.union(s1)
print(u)
print(s1.union(s2))


print(s1.intersection(s2))
'''

'''
d1=s1.difference(s2)
print(d1)
d2=s2.difference(s1)
print(d2)
print(d1.union(d2))
print(s1.symmetric_difference(s2))
'''

'''
# s1 = s1.symmetric_difference(s2)
s1.symmetric_difference_update(s2)
# s2.symmetric_difference_update(s1)
s1.difference_update(s2)    # s1 = s1 - s2
s2 = s1.difference(s2)

s1.intersection_update(s2)  # s1 = s1.intersection(s2)
'''


'''
print(s1.isdisjoint(s2))             #False
print(s1.isdisjoint(s3))             #True


print(s1.issubset(universal))           #True 
print(universal.issuperset(s1))         #True 
'''  


#Frozenset=Immutable version of set
                           #frozenset expected at most 1 argument
'''
fs1=frozenset({1,2,3,4})
print(fs1)
t1=(5,6,7,8)
fs2=frozenset(t1)
print(fs2)
fs3=frozenset([2,4,6,7])
print(fs3)
fs4=frozenset("Abhi")
print(fs4)

e=frozenset()
print(e)
print(type(e))
'''


#Dictionary: Unordered and Mutable collection of key:value pairs
                                                  #left=key
                                                  #right=value

'''
result = {"Physics":87, "Maths":92, "Python":99}
print(result)
print(result["Physics"])
print(result["Python"])

print(result["Maths"])
result["Maths"]=29
print(result)
'''

'''
batch = {1:"Yug", 2:"Naitik", 3:"Chinmay", 4: "Madhav", 2:"Manthan"}
print(batch)
print(batch[1])
print(batch[2])
'''



# key of a dictionary must be immutable and unique.
# working=number,string,tuple,frozenset
# not working=list,set,dictionary


#not working=list,set,dictionary
'''
# sample = {1:"number", "Physics":45, {"Physics":87, "Maths":92} :"fzst" }
# print(sample)                          #TypeError: unhashable type: 'dict'


# sample1={1:"number","Physics":45,{"Physics"}:"fzst"}
# print(sample1)                           #TypeError: unhashable type: 'set'


# sample2={1:"number","Physics":45,["Physics","Maths"]:"fzst"}
# print(sample2)                            #TypeError: unhashable type: 'list'
'''


#working=number,string,tuple,frozenset

# sample={1:"number", "Physics":45 }
# print(sample)


# sample1={1:"number", "Physics":45,("Physics","Maths"):75 }
# print(sample1)


# sample2={1:"number", "Physics":45,frozenset({"Physics","Maths"}):75 }
# print(sample2)





