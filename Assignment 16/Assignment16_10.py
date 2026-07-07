# 10. Write a program which accept name from user and display length of its name. 
# Input : Marvellous   
# Output : 10
def NameLength(name):
    return len(name)

def main():
    name = input("Enter name: ")
    print(f"Length of name {name} is:", NameLength(name))
    
if __name__ == "__main__":
    main()