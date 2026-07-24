# Q2. Count Words in a File
def CountWords(filename):
    file = open(filename, "r")
 
    count = 0
 
    for line in file:
        words = line.split()
        count += len(words)
 
    file.close()
 
    return count
 
 
def main():
    name = input("Enter file name: ")
 
    result = CountWords(name)
 
    print("Total number of words:", result)
 
 
if __name__ == "__main__":
    main()