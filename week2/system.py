import os 
import sys
import socket

def sum(num1, num2):
    result = num1 + num2
    return result

def min(num1, num2):
    result = num1 - num2
    return result

num1 = float(sys.argv[1])
operation = sys.argv[2]
num2 = float(sys.argv[3])


if operation == "sum":
    output = sum(num1, num2)
    print(output)
elif operation == "min":
    output = min(num1, num2)
    print(output)
else:
    print("operation not add") 


x = os.getenv("password")
print(x)

y = os.getenv("WAYLAND_DISPLAY")
print(y)
