# Accept N numbers from user and return maximum number
def Maximum(arr):
    
    max_no = arr[0]

    for value in arr:
        if value > max_no:
            max_no = value

    return max_no


def main():

    size = int(input("Enter number of elements : "))

    data = []

    for i in range(size):
        no = int(input("Enter number : "))
        data.append(no)

    result = Maximum(data)

    print("Maximum number is :", result)


if __name__ == "__main__":
    main()