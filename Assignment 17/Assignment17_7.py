def DisplayPattern(no):
    
    for i in range(no):

        for j in range(1, no + 1):
            print(j, end=" ")

        print()

def main():

    value = int(input("Enter number : "))
    DisplayPattern(value)

if __name__ == "__main__":
    main()