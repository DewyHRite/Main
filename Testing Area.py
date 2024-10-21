import os

# Rename a file
new_name = "newfile.txt"

try:
    os.rename(file_name, new_name)
    print(f"File renamed from {old_name} to {new_name}.")

    file_name = new_name
except FileNotFoundError:
    print(f"The file {old_name} does not exist.")
except Exception as e:
    print(f"Error renaming file: {e}")



    list_files()
    modify_permission('755', 'test_file.txt')