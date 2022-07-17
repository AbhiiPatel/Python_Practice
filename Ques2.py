
#1
'''
list1 = ['no bun', 'bug bun bug bun bug bug', 'bunny bug', 'buggy bug bug buggy']

list1.sort()
print(list1)
'''

#2
'''
s1=set()

size=int(input("Enter size of element to store in set:"))
print("Enter element")
for i in range(0,size):
    ele=input()
    s1.add(ele)

print(s1)    

num=input("Enter number")
for i in s1:
    if num==i:
        print("present")
        break
else:
    print("not present")    
'''       


#3
'''
l1=[]
print("Enter 10 numbers:")

for i in range(0,10):
    num=input()
    l1.append(num)

print(l1)
l2=[]
l1.reverse()
l2=l1.copy()
print(l2)

'''


#4
'''
antonyms={'right':'left','up':'down','big':'small','beautiful':'ugly'}
print(antonyms)
print(antonyms.keys())

word=input("Enter word:").lower()

for i in antonyms.keys():
    if i==word:
        print(antonyms[word])
        break
else:
       print("Given word is not present in antonyms.")
'''



#5
'''
dict={}

for i in range(1,4):
    print(f"student{i}:")
    name=input("Enter name:")
    mark=int(input("Enter mark:"))
    dict.setdefault(name,mark)

print(dict)
print(sorted(dict.keys()))
print(sorted(dict.values()))
'''


    


'''
def char_frequency(str1):
    dict = {}
    for n in str1:
        keys = dict.keys()
        if n in keys:
            dict[n] += 1
        else:
            dict[n] = 1
    return dict
print(char_frequency('MISSISSIPPI'))
'''

#8
'''
string="MISSISSIPPI"

dict={}


for i in string:
    dict[i]=dict.get(i,0)+1
   
print(dict)
'''


#9
'''
dict={'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}
# x=[]
# x.append(dict.keys())
# print(x)
l1=[]
for x in dict:
    l1.append(x)
print(l1)


for sub,mark in dict.items():
    print(sub,mark)
'''


#1)
'''
Make a list containing of only strings. Now ask user for any string and re-arrange the list in the decending order of occurance of that string.
for example:
list1 = ['no bun', 'bug bun bug bun bug bug', 'bunny bug', 'buggy bug bug buggy']
input string = 'bug'
output list = ['bug bun bug bun bug bug', 'buggy bug bug buggy', 'bunny bug', 'no bun']
'''

'''
words=['no bun', 'bug bun bug bun bug bug', 'bunny bug', 'buggy bug bug buggy']
string=input("Enter string:")
temp=[]

for phrase in words:
    count=phrase.count(string)  
    temp.append(str(count)+"_"+phrase)    #= 0_no bun, 4_bug bun bug bun bug bug,    1_bunny bug, 4_buggy bug bug buggy

# print(temp)
temp.sort()
temp.reverse()
# print(temp)

sorted_list=[]

for phrase in temp:
    split_list=phrase.split("_")
    sorted_list.append(split_list[1])

print(sorted_list)
'''



#8) Make a Python program to count letters of the word: MISSISSIPPI. Your program should store them in a dictionary as: {"M":1, "I":4, "S":4, "P":2}. Next, generalize this program for any word entered by user.

'''
word=input("Enter string:").lower()
dict={}

for letter in word:
    dict[letter]=word.count(letter)

print(dict)
'''


# 9. Write a Python program to split a given dictionary of lists into list of dictionaries.
# Original dictionary of lists:
# {'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}
# Split said dictionary of lists into list of dictionaries:
# [{'Science': 88, 'Language': 77}, {'Science': 89, 'Language': 78}, {'Science': 62, 'Language': 84}, {'Science': 95, 'Language': 80}]


dict= {'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}
list=[]
for i in range(4):
    student_result={}
    for x in dict:
        student_result[x]=dict[x][i]
    # print(student_result)
    list.append(student_result)
print(list)






















