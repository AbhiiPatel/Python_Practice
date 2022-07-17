#List=Ordered and Mutable 




l1 = [11, 22, 33, 11, 45, 78, 11, -43, 98, 11, -23.32, 11, 500]
#print(l1)
# print(type(l1))

'''
print(l1[4])
print(l1[-3])
print(l1[3 : -1 : 2])
print(l1[-1 : 3 : -1 ])     #slicing will always give you a new collections
print(l1)
'''


l1[5]=780

'''
print(l1)

print(l1[1:7])

print(min(l1))
print(max(l1))

print(sorted(l1))     #sorted() always give you a NEW LIST
print(l1)
'''


"""
print(sum(l1))
print(round(sum(l1),2))
print(round(sum(l1)))
"""


'''
vegetables = ["capsicum", "tomato", "onions", "corn", "olive", "mushrooms", "carrot", "cabbage", "Potato"]
print(len(vegetables))
print(vegetables)
print(min(vegetables))
print(max(vegetables))
print(sorted(vegetables))
'''


'''
mix_veg = ["capsicum", 2, "tomato", 5, "onions", -3.5, "corn", 0.75]
print(mix_veg)

mix_veg = ["capsicum", "2", "tomato", "5", "onions", "-3.5", "corn", "0.75"]
print(mix_veg)
print(min(mix_veg))
print(max(mix_veg))
print(sorted(mix_veg))
'''


#List method


numbers = [11, 22, 33, 11, 45, 78, 11, -43, 98, 11, -23.32, 11, 500]
'''
numbers.append(1000)
print(numbers)
print(max(numbers))
'''


'''
myString = "Next friday we will go to watch a movie.       "
yourString = "Above sentence is False."

print(myString.split())
'''


#numbers.clear()
#print(numbers)

# print(numbers)
#del numbers
#print(numbers)



'''
print(len(numbers))
print(numbers.count(11))    #how many times 11 in numbers
'''


'''
myFavoriteStudent = "Chinmay"
print(myFavoriteStudent)
print(min(myFavoriteStudent))
print(min("Chinmay"))
print(max("Chinmay"))
print(sorted("Chinmay"))
'''