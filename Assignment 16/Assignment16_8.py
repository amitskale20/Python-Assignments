# 8. Write a program which accept number from user and print that number of “*” on screen. 
# Input : 5    
# Output : * * * * * 
def DisplayStar(no):
    for i in range(no):
        print("*", end=" ")

def main():
    value = int(input("Enter number: "))
    DisplayStar(value)  
      
if __name__ == "__main__":
    main()