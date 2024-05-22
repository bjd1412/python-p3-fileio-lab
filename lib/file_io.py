def write_file(file_name, file_content):
    with open(f"{file_name}.txt", encoding='utf-8', mode = "w") as file:
        file.write(file_content)
    pass

def append_file(file_name, append_content):
    with open(f"{file_name}.txt", encoding='utf-8', mode= "a") as file:
        file.write(append_content)
    pass

def read_file(file_name):
    with open(f"{file_name}.txt", encoding='utf-8', mode = "r") as file:
        return file.read()

    pass
