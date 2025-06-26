# dictionaries
x = {
    "hello":"good",
    "Name":"ram",
    "age":10,
    "class":"7"
}

print(type(x))

print(x["class"])


# List of Dictionaries
ec2_instance_info = [
    {
        "id":"i-001",
        "type":"t2.micro"
    },

    {
        "id":"i-002",
        "type":"t2.medium"
    },

    {
        "id":"i-003",
        "type":"t2.large"
    },
]

print(type(ec2_instance_info))

print(ec2_instance_info[1]["id"])


# simple set example

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print(type(set1))

print(f"", set1)

# in set we can perform union, intersection and difference.