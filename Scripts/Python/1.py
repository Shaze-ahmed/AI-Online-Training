#import cv2
#import math

#https://docs.python.org/3/py-modindex.html
#print (math.gcd(3,6))

# a = "34"
#b = "Harry"
#c = 45.32
#d = float(a)
#print(type(d))

#name = "Shahzad"
#name = 'Shahzad'
#name = '''Shahzad
#is a 
#Oracle Programmer'''
#name = "Shahzad Ahmed"
#print(name.strip())
#print(len(name))
#print(len(name.strip()))
#print(name.upper())
# #print(name.lower())
# #print(name.strip().capitalize())
# #print(name.replace('a','e'))
# #print(name.replace(' ','\n'))

# str1 = "This is a "
# str2 = "This ia not a "
# #print(str1 + "Dog" + str2)
# name1 = "Shahzad"
# name2 = "Boy"
# #temp = "This is a {0} and he is a good {0}".format(name1, name2)
# temp = f"This is a {name1} and he is a good {name2}"
# # print (temp)
# # print (7**2)  #square cube
# # print (7//2)  #divied by
# # print (7%2)   #remainder like mod

# ''' 
# Python Collection
# 1. List
# 2. Tuple
# 3. Set
# 4. Dictionary
# '''

# # LIST  values can changes
# lst = [1, 2, 3, 4, 5]
# print (type(lst))
# print(lst)
# print(lst[2])
# print(lst[2:4])

# # lst[2] = 33  # replace index value
# # # lst.append(100)
# # lst.insert(2, 100) # insert index value
# # print(lst)
# # # print (len(lst))
# # lst.remove(5)  #remove particular number
# # lst.pop()  # remove last value
# # # del lst[1] # remove index value
# # # del lst
# # lst.clear
# # print(lst)

# #Tuple value cannot change
# # a = ("Shahzad","Iqbal","Zubair")
# # b = list(a)
# # b.append("Nawaz")
# # a = tuple(b)
# # print (a)
# # print (type(a))

# # SET eliminate duplicate
s1 = {1, 2, 2, 3, 3 ,4,4, 5,5,6,6}
# s2 = {2,8}
# s1.add(123321)
# s1.update([7,8])
# # s1.remove(1000)
# s1.discard(1000)
# print (len(s1))
# print(s1.union(s2))
# print(s1.intersection(s2))
# print(s1.difference(s2))
# print(s1)
# print(s2)
# print(s1 | s2) #union
# print(s1 & s2) #intersection
# print(s1 - s2) #difference
# print(s1 ^ s2) #Symmetric difference
# print(s1)

# Dictionary
myDics = {
        "Name" : "Shahzad Ahmed",
        "Class" : "12th",
        "Marks" : 100
}

print (myDics)
print(myDics["Marks"])
myDics["Marks"] = 101
print(myDics["Marks"])
# myDics.pop("Marks")
print (myDics)


# if then else
# age = input("Emter Your Age\n")
# age = int(age)

# age = 20
# if age > 18:
#     print("Adults")
# elif age==18:
#         print("Child")
# else:
#    print("else    condition")
 



# a = 200
# b = 33

# if b > a:
#   print("b is greater than a")
# elif a == b:
#   print("a and b are equal")
# else:
#   print("a is greater than b")

# LOOPS FOR LOOP
# a = input("Enter Table Number")
# b = input("Enter Table Range")
# a = int(a)
# b = int(b)
# a = 2
# b = 10
# for i in range(0, b):
#     # print (i)
#     print(a + 'x' + (a*(i+1)))

# print ("hello")

# LOOPS WHILE LOOP
# i = 0
# while (i<10):    
#     print(i)
#     if i == 5:
#         break    
#     i= i + 1

# i = 0
# while (i<10):
#     i= i + 1
    
#     if i == 5:
#         continue
#     print(i)

# def greet():
#     print("Good Morning HBL")

#greet()

# def sum(a, b):
#     c = a+b
#     print(c)

# sum(10,20)

# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

# p1 = Person("John", 36)

# print(p1.name)
# print(p1.age)

# class Employee:
#     def __int__(self, gname, gage):
#         self.name = gname
#         self.age = gage

# p2 = Employee("Shahzad",15)
# print(p2.name )





# pets = ['cats', 'dogs', 'rabbits', 'hamsters']

#     for myPets in pets:
#     print (myPets)