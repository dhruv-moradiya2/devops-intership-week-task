import sys 

type = sys.argv[1]

if type == "t2.micro":
    print("list out all t2.micro")
elif type == "t2.medium":
    print("list all t2.medium")
else:
    print("list is not available")
