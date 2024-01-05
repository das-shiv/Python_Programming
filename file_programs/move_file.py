import os

source = input("Enter the source path: ")
destination = input("Enter the destination path: ")

try:
    if os.path.exists(destination):
        print("The file/directory already exists.")
    else:
        os.replace(source, destination)
        print("File/directory moved successfully.")
except FileNotFoundError as e:
    print(f"Error: {e}. The source file/directory was not found.")
except Exception as e:
    print(f"An error occurred: {e}")
