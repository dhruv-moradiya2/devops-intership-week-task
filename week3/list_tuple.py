# list
list_s3 = ["demo-s3", "test-s3", "prod-s3"]

# show type 
print(type(list_s3))

# add in list
list_s3.append("stage_s3")
# short according to number or a-z
x = list_s3.sort()
print(list_s3)

print()

# tuple 
tuple_admin = ("admin1", "admin2")

print(type(tuple_admin))
print(tuple_admin)

print()
# split list indexing
print(list_s3[0:2])
print(tuple_admin[0])

print()
# for know about length of list and tuple
print(len(list_s3))
print(len(tuple_admin))
