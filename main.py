#name_Input = input("whats your name")
#print("your name is " + name_Input)
#print(type(nameInput))
#================================================================
#first_name = "chitiz "
#last_name = "panday"
#full_name = first_name + last_name
#print("my full name is: " + full_name)
#==================================================================================
#age = 6
#print("My sons age is " + str(age)) #here we performed type casting by changing integer data type to string data type
#=================================================================================
#name, age, height = "chitiz panday", 41, 5.5
#print(name,age,height)
#====================================
#name="chitiz"
#print(len(name))
#print(name.find('z'))
#print(name.capitalize())
#print(name.upper())
#print(name.lower())
#print(name.isalpha())
#print(name.isdigit())
#print(name.count('i'))
#print(name.replace('c', 'a'))
#print(name*3)
#=========================================
#name = input("whats your name ? ")
#height = float(input("how tall are you? "))
#age = int(input("how old are you? "))
#print("welcome " + name)
#print(name + " is "+str(height) + " feet tall")
#print(name + " is " + str(age) + "years old")
#======================================================
"""import math

pi = 3.14
print(math.floor(pi))
print(math.ceil(pi))
print(pow(pi, 2))
print(round(pi))
print(math.sqrt(25))"""
#====================================IF STATEMENT=============
# IF STATEMENT IS A BLOCK OF CODE THAT WILL EXECUTE IF ITS CONDITION IS TRUE
# check what is wrong in this block of code. CLUE: if the condition is true, it gets executed and the rest is skipped!!!
"""age= int(input("whats your age? "))
if age >= 18:
    print("you are an adult")
elif age <= 0:
    print("you have not been born yet!")
elif age == 100:                         # = is an assignment operator, while == is a comparison operator
    print("you r a senior citizen")
else:
    print("you are minor")"""
#=========================================LOGICAL OPERATORS======
#LOGICAL OPERATORS (and, or, not) are used to check if two or more conditional statements is true
"""temp = float(input("whats the temperature outside? "))
if temp>0 and temp<=30:
    print("the temperature is good")
elif temp<0 or temp>30:
    print("the temperature is bad")"""
#=======================================WHILE LOOP===============
#WHILE LOOP IS A STATEMENT THAT WILL EXECUTE ITS BLOCK OF CODE AS LONG AS ITS CONDITION REMAINS TRUE.
"""while 1 == 1:
    print("I am stuck in a loop!!")"""
#=========
"""name = ""
while len(name) == 0:
    name = input("whats your name")
print("hello " + name)"""
#=========================================FOR LOOP======================================
#FOR LOOP IS A STATEMENT THAT WILL EXECUTE ITS BLOCK OF CODE A LIMITED NUMBER OF TIMES
#WHILE LOOP = UNLIMITED
#FOR LOOP = LIMITED
"""for index in range(10): #index or i
    print(index)"""
#============
"""for i in "chitiz panday":
    print(i)"""
#===========
"""for i in range(10, 0, -1):
    print(i)"""
#==========