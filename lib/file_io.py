from pathlib import Path

def write_file(file_name, file_content):
    if isinstance(file_name, Path):
        file_name = str(file_name)

    if not file_name.endswith('.txt'):
        file_name +='.txt'
    
    with open(file_name,'w') as file:
        file.write(file_content)
    

def append_file(file_name, append_content):
    if isinstance(file_name, Path):
        file_name = str(file_name)

    if not file_name.endswith('.txt'):
        file_name +='.txt'
    
    with open(file_name,'a') as file:
        file.write(append_content)
    


def read_file(file_name):
    if isinstance(file_name, Path):
        file_name = str(file_name)
    
    if not file_name.endswith('.txt'):
        file_name +='.txt'
    
    with open(file_name,'r') as file:
        return file.read()
    
    
