# 5. Frequency of a String in a File
# Write a program that accepts a file name and a string from the user and counts how many times that string appears in the file. 
def CountFrequency(filename, word):
    file = open(filename, "r")
 
    data = file.read()
 
    file.close()
 
    words = data.split()
 
    count = words.count(word)
 
    return count
 
def main():
    name = input("Enter file name: ")
    word = input("Enter string to search: ")
 
    result = CountFrequency(name, word)
 
    print("Frequency of", word, "is", result)
 
if __name__ == "__main__":
    main()