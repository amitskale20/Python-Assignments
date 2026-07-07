# Count Digits
def CountDigits(no):
    
    count = 0

    while no > 0:

        count = count + 1
        no = no // 10

    return count

def main():

    value = int(input("Enter number : "))

    result = CountDigits(value)

    print(f"Number of digits in {value} :", result)

if __name__ == "__main__":
    main()