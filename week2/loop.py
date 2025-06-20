# simple loop
num = [1, 2, 3, 4, 5, 6]
for i in num:
    print(i)


print()

count = 0 
while count < 5:
    print(count)
    count+=1


print()
# loop control break and continue

# break
numbers = [1,2,3,4,5,6,7,8,9]

for i in numbers:
    if i == 4:
        break
    print(i)

print()
# continue
for i in numbers:
    if i == 5:
        continue
    print(i)


print()

log_file = [
   "INFO: Operation successful",
   "ERROR: File not found",
   "DEBUG: Connection established",
   "ERROR: Database connection failed",
]

for line in log_file:
   if "ERROR" in line:
       print(line)


