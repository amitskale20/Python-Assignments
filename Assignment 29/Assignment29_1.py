# 1. Check File Exists in Current Directory
# Write a program that accepts a file name from the user and 
# checks whether that file exists in the current directory. 
import os
 
def CheckFile(filename):
    if os.path.exists(filename):
        print("File exists.")
    else:
        print("File does not exist.")
 
def main():
    name = input("Enter file name: ")
 
    CheckFile(name)
 
if __name__ == "__main__":
    main()