
def blank_file(filename : str):
    file = open(filename, "w")
    file.close()

def file_wcontent(filename : str, content : str):
    file = open(filename, "w")
    file.write(content)
    file.close()

def add_content(filename : str, content : str, line : int):
    file = open(filename, "r")
    data = file.readlines()
    file.close()
    filtered_data = []
    for x in data:
        filtered_data.append(x.strip())
    filtered_data.insert(line-1, content)
    new_content = ""
    for y in filtered_data:
        new_content = new_content + y + "\n"
    new_file = open(filename, "w")
    new_file.write(new_content)
    new_file.close()

def replace_content(filename : str, existing_word : str, new_word : str):
    file = open(filename, "r")
    data = str(file.read())
    file.close()
    data = data.replace(existing_word, new_word)
    new_file = open(filename, "w")
    new_file.write(data)
    new_file.close()