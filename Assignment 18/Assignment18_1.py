# Accept N numbers from user, store them in a list and return the addition of all elements
def Addition(arr):
    
    total = 0

    for value in arr:
        total = total + value

    return total


def main():

    size = int(input("Enter number of elements : "))

    data = []

    for i in range(size):
        no = int(input("Enter number : "))
        data.append(no)

    result = Addition(data)

    print("Addition of all elements is :", result)


if __name__ == "__main__":
    main()