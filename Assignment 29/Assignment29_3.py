# 3. Copy File Contents into Demo.txt (Using Command Line)
# Accept an existing file name through the command line, create a new file named Demo.txt, 
# and copy the contents of the given file into it. 
import sys

def CopyFile(source):
    file1 = open(source, "r")
 
    data = file1.read()
 
    file1.close()
 
    file2 = open("Demo.txt", "w")
 
    file2.write(data)
 
    file2.close()
 
    print("Contents copied successfully.")
 
def main():
    if len(sys.argv) != 2:
        print("Usage: python program.py <SourceFile>")
        return
 
    CopyFile(sys.argv[1])
 
if __name__ == "__main__":
    main()