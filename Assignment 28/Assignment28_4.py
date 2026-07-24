#Q4. Copy File Contents

def CopyFile(source, destination):
    file1 = open(source, "r")
    data = file1.read()
    file1.close()
 
    file2 = open(destination, "w")
    file2.write(data)
    file2.close()
 
    print("Contents copied successfully.")
 
 
def main():
    source = input("Enter source file name: ")
    destination = input("Enter destination file name: ")
 
    CopyFile(source, destination)
 
 
if __name__ == "__main__":
    main()