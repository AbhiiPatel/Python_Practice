#Try nesting collections of Python in one another and deduce a conclusion.


#conclusion of list
'''
l1=[12,"abhi"]
print(l1)


l2=[12,"abhi",[1,2,3,4]]
print(l2)


l3=[12,"abhi",[1,2,3],(4,5,"tirth")]
print(l3)

l4=[12,"abhi",[1,2,3],(4,5,"tirth"),{"rudra","nisarg"}]
print(l4)

l5=[12,"abhi",[1,2,3],(4,5,"tirth"),{"rudra","nisarg"},frozenset({"nirav","jalkesh"})]
print(l5)


l6=[12,"abhi",[1,2,3],(4,5,"tirth"),{"rudra","nisarg"},{1:"c",2:"c++",3:"java"}]
print(l6)
'''

#All type of collection are allow in list





#conclusion of tuple
'''
t1=12,"abhi"
print(t1)

t2=12,"abhi",[1,2,3,4]
print(t2)


t3=12,"abhi",[1,2,3],(4,5,"tirth")
print(t3)


t4=12,"abhi",[1,2,3],(4,5,"tirth"),{"rudra","nisarg"}
print(t4)


t5=12,"abhi",[1,2,3],(4,5,"tirth"),{"rudra","nisarg"},frozenset({"nirav","jalkesh"})
print(t5)


t6={12,"abhi",[1,2,3],(4,5,"tirth"),{"rudra","nisarg"},{1:"c",2:"c++",3:"java"}}
print(t6)
'''

#All type of collection are allow in tuple





#conclusion of set

'''
s1={12,"abhi"}
print(s1)

 
# s2={12,"abhi",[1,2,3,4]}                          #TypeError: unhashable type: 'list'
# print(s2)

s3={12,"abhi",(4,5,"tirth")}
print(s3)


# s4={12,"abhi",(4,5,"tirth"),{"rudra","nisarg"}}      #TypeError: unhashable type: 'set'
# print(s4)


s5={12,"abhi",(4,5,"tirth"),frozenset({"nirav","jalkesh"})}
print(s5)


# s6={12,"abhi",(4,5,"tirth"),{1:"c",2:"c++",3:"java"}}
# print(s6)                                            #TypeError: unhashable type: 'dict'
'''


#list,set and dictionary(they are mutable) are not allow in set(Unordered)

# List: Ordered,Mutable
# Set: Unordered,Mutable
# Dictionary:Unordered,Mutable





#conclusion of frozenset

'''
fs1=frozenset({12,"abhi"})
print(fs1)


# fs2=frozenset({12,"abhi",[1,2,3,4]})
# print(fs2)                             #TypeError: unhashable type: 'list'


fs3=frozenset({12,"abhi",(4,5,"tirth")})
print(fs3)

# fs4=frozenset({12,"abhi",(4,5,"tirth"),{"rudra","nisarg"}})
# print(fs4)                            #TypeError: unhashable type: 'set'


fs5=frozenset({12,"abhi",(4,5,"tirth"),frozenset({"nirav","jalkesh"})})
print(fs5)


# fs6=frozenset({12,"abhi",(4,5,"tirth"),{1:"c",2:"c++",3:"java"}})
# print(fs6)                             #TypeError: unhashable type: 'dict'
'''

#list,set and dictionary(they are mutable) are not allow in frozenset(Unordered)

# List: Ordered,Mutable
# Set: Unordered,Mutable
# Dictionary:Unordered,Mutable



