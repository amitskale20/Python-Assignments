# 3. Write a program which contains one function named as Add() which accepts two numbers 
# from user and return addition of that two numbers. 
# Input : 11    5   
# Output : 16
def Add(no1, no2):
    return no1 + no2

def main():
    value1 = int(input("Enter first number: "))
    value2 = int(input("Enter second number: "))

    result = Add(value1, value2)
    print("Addition is:", result)
    
if __name__ == "__main__":
    main() 