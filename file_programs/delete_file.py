import os
import shutil

file_name = 'file.txt'
directory_name = 'folder'
try:

    os.remove(file_name) #remove a file
except Exception as e:
    print(e)

try:

    os.rmdir(directory_name) #remove an empty directory
except Exception as e:
    print(e)

try:
    shutil.rmtree(directory_name) # tp remove non empty directory
except Exception as e:
    print(e)
