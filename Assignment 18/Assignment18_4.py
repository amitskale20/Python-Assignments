# Find frequency of a given element in a list.
def Frequency(arr, search):
    
    count = 0

    for value in arr:

        if value == search:
            count += 1

    return count


def main():

    size = int(input("Enter number of elements : "))

    data = []

    for i in range(size):
        no = int(input("Enter number : "))
        data.append(no)

    element = int(input("Enter element to search : "))

    result = Frequency(data, element)

    print(f"Frequency of {element} is :", result)


if __name__ == "__main__":
    main()