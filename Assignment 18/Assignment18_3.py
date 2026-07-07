# Accept N numbers from user and return minimum number.
def Minimum(arr):
    
    min_no = arr[0]

    for value in arr:
        if value < min_no:
            min_no = value

    return min_no


def main():

    size = int(input("Enter number of elements : "))

    data = []

    for i in range(size):
        no = int(input("Enter number : "))
        data.append(no)

    result = Minimum(data)

    print("Minimum number is :", result)


if __name__ == "__main__":
    main()