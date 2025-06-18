# Arithmetic operator
a = 5
b = 6

sum = a + b
min = b - a 
mul = a * b
div = b / a

print("this is arithmetic operator")
print("sum:",sum)
print("minus:",min)
print("multi:",mul)
print("division:",div)


print()
print("this is comparison operator")
# comparison operator
less = a < b
gre = a > b
less_eql = a <= b
gre_eql =  a >= b
equl = a == b 
not_equl = a != b

print("less:", less)
print("gre:", gre)
print("less equal:", less_eql)
print("gre eql:", gre_eql)
print("equal:", equl)
print("not equal:",not_equl)


print()


print("this is Logical operator")
x = True
y = False

and_res = x and y
or_res = x or y
not_x = not x
not_y = not y

print("and:",and_res)
print("or:", or_res)
print("not x:", not_x)
print("not y:", not_y)

print()

print("this is assignment operator")

total = 10

total += 5 # total 15
total -= 4 # total 15 - 4 = 11
total *= 3 # total 11 * 3 = 33
total /= 2 # total 33 / 2 = 16.5

print("total:", total)


print()

my_list = [1,2,3,4,5]

a = my_list
b = [1,2,3,4,5,6,7]

print("this is identity operator")

a_is = a is my_list
a_is_not = a is not b

print("a is:", a_is)
print("a is not:", a_is_not)

print()

print("this is membership operator")

in_list = 5 in my_list
in_not_list = 8 not in my_list

print("list in:", in_list )
print("list not in:",in_not_list)



print()

print("this is bitwise operator")

a = 6
b = 8

AND_gate = a & b
OR_gate = a | b
XOR_gate = a ^ b
NOT_gate = ~ b
left_shift = a << b
right_shift = a >> b

print("and:", AND_gate)
print("or", OR_gate)
print("xor", XOR_gate)
print("not:", NOT_gate)
print("left shift:", left_shift)
print("right shift:", right_shift)