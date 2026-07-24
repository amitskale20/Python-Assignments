#Q5. Search a Word in a File

def SearchWord(filename, word):
    file = open(filename, "r")
 
    data = file.read()
 
    file.close()
 
    if word in data:
        print(word, "is present in the file.")
    else:
        print(word, "is not present in the file.")
 
 
def main():
    name = input("Enter file name: ")
    word = input("Enter word to search: ")
 
    SearchWord(name, word)
 
 
if __name__ == "__main__":
    main()


# C:\Users\amit.kale02\Desktop\Python\Assignments\Assignment 28>py Assignment28_5.py
# Enter file name: Assignment28_5.py
# Enter word to search: main
# main is present in the file.