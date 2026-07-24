# 2. Display File Contents
# Write a program that accepts a file name, opens the file, and displays its contents on the console. 
def DisplayFile(filename):
    file = open(filename, "r")
 
    print(file.read())
 
    file.close()
 
def main():
    name = input("Enter file name: ")
 
    DisplayFile(name)
 
if __name__ == "__main__":
    main()