# Write a python script and do the following commands in order to perform the following 
# commands in bash console: 
# pwd, ls, cd, touch, python, mkdir, rm, etc.


import os
import subprocess

print("Current Directory:")
print(os.getcwd())

print("\nFiles and Folders:")
print(os.listdir())

new_dir = "test_folder"
os.mkdir(new_dir)
print(f"\nDirectory '{new_dir}' created.")

os.chdir(new_dir)
print("\nChanged Directory To:")
print(os.getcwd())

filename = "example.txt"
open(filename, "w").close()
print(f"\nFile '{filename}' created.")

print("\nRunning Python Command:")
subprocess.run(["python", "--version"])

os.chdir("..")
print("\nReturned To:")
print(os.getcwd())

os.remove(f"{new_dir}/{filename}")
os.rmdir(new_dir)

print(f"\nRemoved '{filename}' and '{new_dir}' successfully.")