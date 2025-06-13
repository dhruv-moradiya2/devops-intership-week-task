#
# Day 1 basic python
print("hello")

x="dhruv"
print("my name is",x)

#y = input("enter the number:")
#print(y)

#z = int(input("enter the number"))
#print(z)

#print(type(y)) # it show string
#print(type(z)) # it show int

# day 2  string, data type

str1 = "hello"
str2 = "dhruv"
result = str1 + " " + str2
print(result)

# count lenth all
text = "bash and python use for scripting"
length = len(text)
print(length)

# convert in upper
upper = "HELLO THIS PYTHON"
low = upper.lower()
print(low)

# convert in lower
lowr = "hellow this python"
up = lowr.upper()
print(up)

# split in word as ["",""]
t = "Python is awesome with help to web dev"
words = t.split()
print("Words:", words)

# it is use for manipulation 
text = "  here both side some space  "
w = text.strip()
print(w)

# below basic calculation
num1 = 50
num2 = 5

result1 = num1 // num2
print("Integer division", result1)

result2 = num1 + num2
print ("sub", result2)

# day 3 Keyword, variable & Global vs Local

# their are many keyword in python which is use for programming
# keyword not write as variable

# global variable vs local variable
# defining variable in function are know as local variable
# defining variable in outside of blog it know as global variable

# rule 1 always variable write in lower case and 
# rule 2 two way declare variable snake casing and camel casing 
# - snake casing: ec2_instant_list
# - camel casing: ec2InstantList
# rule 3 keep variable descriptive so other people can understand 

my_variable = 43

print(my_variable)

# local variable

def my_function():
    x = 10
    print(x)

my_function() # print x as 10
print(x)   # this will give error

# global variable

y = 10
def my_global():
    print(y)

my_global()
print(y)
