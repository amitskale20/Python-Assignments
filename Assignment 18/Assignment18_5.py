# This program accepts numbers from the user, stores them in a list, finds the prime numbers 
# using the ChkPrime() function from the MarvellousNum module, and returns the sum of all prime 
# numbers

import MarvellousNum

def ListPrime(arr):

    total = 0

    for value in arr:

        if MarvellousNum.ChkPrime(value):
            total = total + value

    return total


def main():

    size = int(input("Enter number of elements : "))

    data = []

    for i in range(size):
        no = int(input("Enter number : "))
        data.append(no)

    result = ListPrime(data)

    print(f"Addition of prime numbers in {data} :", result)


if __name__ == "__main__":
    main()
