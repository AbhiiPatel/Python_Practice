s1 = "Students of this batch are going to rock the software industry. They are Bill Gates, Elon Musk and Steve Jobs of the future. They have potential to create another microsoft in India. But, some of them always keep their camera off."

"""
print(s1.find("are"))
print(s1.find("are",24))
print(s1.find("are",24,49))
print(s1.index("are",24,49))
"""

"""
print(s1.find("of"))
print(s1.rfind("of"))
print(s1.rfind("of",50))
print(s1.rfind("of",30,200))
print(s1.rfind("of",50,100))


print(s1.rindex("of"))
print(s1.rindex("of",50))
print(s1.rindex("of",30,200))
print(s1.rindex("of",50,100))
"""


#Methods starting with "is" always returns either True or False

'''
s2 = "987654321"
print(s2.isnumeric())
s3 = "AlakhPandya"
print(s3.isalpha())
print(s1.isalpha())
print(s2.isalpha())

s4 = "987Alakh321Pandya654"
print(s4.isalnum())
print(s2.isalnum())
print(s3.isalnum())
print(s1.isalnum())
'''


'''
s5 = "2022"
print(s5.isdecimal())   # strictly considers only digits 0 to 9 as numbers.
print(s5.isdigit())     # also considers subscript, superscript, circled numbers
print(s5.isnumeric())   # also considers roman numerals, vulgar fractions, numbers from other languages

s6 = "2⁸"
print(s6.isdecimal())
print(s6.isdigit())
print(s6.isnumeric())

s7 = "②⓪②②"
print(s7.isdecimal())
print(s7.isdigit())
print(s7.isnumeric())

s8 = "Ⅳ"
print(s8.isdecimal())
print(s8.isdigit())
print(s8.isnumeric())

s9 = "¾"
print(s9.isdecimal())
print(s9.isdigit())
print(s9.isnumeric())

s10 = "二千二十二"
print(s10.isdecimal())
print(s10.isdigit())
print(s10.isnumeric())
'''

'''
s11 = "ifisfor_while34"  #Does not start with number or any space
print(s11.isidentifier())
print(s11.isupper())
print(s11.islower())
a="Abhi "
print(a.istitle())
s12 = "Darshil is a good boy.\nHe keeps camera on."
print(s12.isprintable())
#print(s12)
s13 = "                \n\n\n\n\n     \t\t\t\t        \n"
print(s13.isspace())
print(a.isspace())
'''
s1 = "Students of this batch are going to rock the software industry. They are Bill Gates, Elon Musk and Steve Jobs of the future. They have potential to create another microsoft in India. But, some of them always keep their camera off."

# print(s1.split())
# print(s1.split("o"))
#print(s1.split("are"))
#print(s1.split("of"))
#print(s1.split("of",3))        #first 3
#print(s1.split(" ",5))

#print(s1.rsplit("o"))
#print(s1.rsplit("of",3))


#print(s1.partition("industry."))
# print(s1.partition("of"))
#print(s1.rpartition("of"))

'''
myList=["I","love","India"]
print(" ".join(myList))
print("#".join(myList))
print("".join(myList))
print("Python".join(myList))
'''


'''
s2 = "                           Good Night!"
print(s2.lstrip())
s4 = "&&&&&&&&&&&&&&&&&&&&Python is fun!&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&"
print(s4.lstrip("&"))
print(s4.rstrip("&"))
print(s4.strip("&"))
'''

#print(s1.replace("of","for"))
#print(s1.replace("of","for",4))    #first 4


'''
s4 = "Harshil has started packing his bags.\nHe will go to home from here.\nAtleast, he has told this to his parents."
print(s4.splitlines())
'''

'''
date=input("Enter date:")
month=input("Enter month number:")
year="2022"

print(f"Date in dd/mm/yyyy format:{date.zfill(2)}/{month.zfill(2)}/{year}")
print(f"Date in dd/mm/yyyy format:{date}/{month}/{year}")
'''


#Home Work

'''
#1
a=input("First Name:")
b=input("Middle Name:")
c=input("Surname:")
print(f"{a[0]}.{b[0]}.{c}")
'''

'''
#2
a="happy birthday"
print(a.replace("h","H",1))
'''


'''
#3
a="color"
b="full"
print(a.replace(a[0:3],b[0:3]))
print(b.replace(b[0:3],a[0:3]))
'''

'''
#4
a="superstar"
b="rocking"
print(a.replace(a[0:3],b[-3: ]))
print(b.replace(b[-3: ],a[0:3]))
'''


'''
#5
a="Keep yourself mute while not speaking."
b=a.replace(" ","_",1)
c=b[::-1]
d=c.replace(" ","#",1)
e=d[::-1]
print(e)
'''


'''
#6
a=input("Enter a String:")
temp=a.lower()
vowels=temp.count("a")+temp.count("e")+temp.count("i")+temp.count("o")+temp.count("u")
space=temp.count(" ")
others=len(a)-vowels-space
print(f"Vowels:{vowels}\nWhite spaces:{space}\nOther character:{others}")
'''


#7
a="This is the lion in the cage."
print(a.replace("the",""))
