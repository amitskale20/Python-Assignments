# 4. Compare Two Files (Using Command Line)
# Accept two file names through command-line arguments and compare their contents.
# If both files contain the same contents, display Success.
# Otherwise, display Failure. 
import sys
 
def CompareFiles(file1, file2):
    fp1 = open(file1, "r")
    fp2 = open(file2, "r")
 
    data1 = fp1.read()
    data2 = fp2.read()
 
    fp1.close()
    fp2.close()
 
    if data1 == data2:
        print("Success")
    else:
        print("Failure")
 
def main():
    if len(sys.argv) != 3:
        print("Usage: python program.py <File1> <File2>")
        return
 
    CompareFiles(sys.argv[1], sys.argv[2])
 
if __name__ == "__main__":
    main()