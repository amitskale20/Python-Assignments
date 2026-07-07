# Pattern
# * * * * *
# * * * * *
# * * * * *
# * * * * *
# * * * * *
def DisplayPattern(no):
    
    for i in range(no):
        for j in range(no):
            print("*", end=" ")

        print()

def main():

    value = int(input("Enter number : "))
    DisplayPattern(value)

if __name__ == "__main__":
    main()