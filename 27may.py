'''
                      topic=Dictionary,Dictionary methods,Function

'''
'''
result = {"Nishit":68, "Keyur":72, "Riddh":84, "Parikshit":95}

result["Tirth"]=79
print(result)
'''


#result.clear()
#del result
# print(result)

'''
r1=result.copy()
r2=result

result["Abhi"]=90
print(result)
print(r1)
print(r2)
'''

# result.fromkeys()
# beneficiaries = ["Yug", "Madhav", "Jainam", "Prince", "Daksh"]
# print(dict.fromkeys(beneficiaries,20000))


'''
print(result["Parikshit"])
print(result.get("Parikshit"))


# print(result["Abhi"])                       #KeyError: 'Abhi'
print(result.get("Abhi"))                   #None

print(result.get("Abhi","Sorry this key is not found in dictionary."))
'''





result = {"Nishit":68, "Keyur":72, "Riddh":84, "Parikshit":95}

# print(result.values())
# print(result.keys())

'''
for name in result:
    print(name)

for name in result.keys():
    print(name)
'''


'''
for marks in result.values():
    print(marks)
'''

# print(result.items())

# for x in result.items():
#     print(x)


# for name,marks in result.items():
#     print(f"student {name} got {marks} marks in exam.")


# print(result.pop())                    #TypeError: pop expected at least 1 argument, got 0
# print(result.pop("Keyur"))
# print(result)

# print(result.popitem())


'''
full_pyramid = {"Prakash":72, "Pavan":77, "Karishma":82, "Dipa":64}
result.update(full_pyramid)
print(result)
'''


result = {"Nishit":68, "Keyur":72, "Riddh":84, "Parikshit":95}
# result.setdefault("Tirth",90)
# print(result)
# x=result.setdefault("Tirth",90)
# print(x)

# result.setdefault("Keyur",27)
# print(result)
# x=result.setdefault("Keyur",27)
# print(x)

# result["Keyur"]=27
# print(result)



'''
name=input("Enter name:")
marks=int(input("Enter marks:"))
old_marks=result.setdefault(name,marks)
if marks==old_marks:
    print(f"student {name} successfully added with {marks} marks.")
else:
    print(f"student {name} already exist with {old_marks} marks.")    
    overwrite=input("Do you want to overwrite marks? Yes/No?:").lower()
    if overwrite=="yes":
        result[name]=marks
        print(f"student {name} successfull overwritten with {marks} marks.")
    else:
        print("no problem")    
print(result)
'''




#Function
"""
without argument and without return
with argumnet and without return
without argumnet and with return
with argument and with return

"""

'''
def display():
    print("Remind us again, what is it that they say about women and disgruntlement?\nOh, yes, “Hell hath no fury like a woman scorned.”\nDown there at the ‘Bhool Bhulaiyaa 2’ camp, for writer Aakash Kaushik and director Anees Bazmee, that aphorism takes a life of its own.\nYes, we all have our thoughts and feelings about this sequel but separate yourself from the memories of Akshay Kumar’s debut instalment for a bit and allow the latest rendition to introduce itself.\n")

display()
'''


'''
def display():
    print("Royal Technosoft")

print("Enter two numbers:")
a=int(input())
b=int(input())

if a>b:
    display()
if a>0:
    display()
if b>0:
    display()
'''


'''
def display(x,y):
    if x>y:
        print(f"{x} is max")
    else:
        print(f"{y} is max")

print("Enter two numbers:")
a=int(input())
b=int(input())

display(a,b)
'''


def avg(x,y):
    ans=(x+y)/2
    print(f"average of {x} and {y} is = {ans}")
    return ans            #if return ans is not write then,
            #TypeError: unsupported operand type(s) for +: 'NoneType' and 'NoneType'
print("Enter two numbers:")
a=int(input())
b=int(input())
p=avg(a,b)


print("Enter two numbers:")
c=int(input())
d=int(input())
q=avg(c,d)

print("sum=",p+q)



