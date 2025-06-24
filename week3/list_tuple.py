
list_s3 = ["demo-s3", "test-s3", "prod-s3"]

print(type(list_s3))
list_s3.append("stage_s3")
x = list_s3.sort()
print(list_s3)


print()

tuple_admin = ("admin1", "admin2")

print(type(tuple_admin))
print(tuple_admin)

print()
print(list_s3[0:2])
print(tuple_admin[0])

print()
print(len(list_s3))
print(len(tuple_admin))


