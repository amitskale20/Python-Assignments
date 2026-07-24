# Q3. Display File Contents

def DisplayFile(filename):
    file = open(filename, "r")
 
    for line in file:
        print(line, end="")
 
    file.close()
 
 
def main():
    name = input("Enter file name: ")
 
    DisplayFile(name)
 
 
if __name__ == "__main__":
    main()