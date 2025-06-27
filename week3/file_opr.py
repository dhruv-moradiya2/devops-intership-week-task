
def update_server_config(file_path, key, value):
    
    with open(file_path, "r") as file:
        lines = file.readlines()

    
    with open(file_path, "w") as file:
        for line in lines:
            if key in line:
                file.write(key + "=" + value + "\n")
            else:
                file.write(line)


server_file_path = "demo_server.conf"
key_words = "MAX_CONNECTIONS"
new_value = "60000"

update_server_config(server_file_path, key_words, new_value)