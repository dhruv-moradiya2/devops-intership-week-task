import os

# list in advance 

folder_list = input("please provide list of folder name: ").split()

for folder in folder_list:
    try:
        files = os.listdir(folder)
    except FileNotFoundError:
        print("please provide valid folder or path look like provide folder not exit in system:", folder)
        continue
    except PermissionError:
        print("you have not permission for provide folder:", folder)
        continue

    print("listing files for the folder: ",folder)

    for file in files:
        print(file)

