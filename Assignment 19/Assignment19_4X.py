from functools import reduce

CheckEven = lambda No : No % 2 == 0
Square = lambda No : No ** 2
Addition = lambda A, B : A + B


def main():

    size = int(input("Enter number of elements : "))

    Data = []

    for i in range(size):
        no = int(input("Enter number : "))
        Data.append(no)

    print("Input List :", Data)

    FData = list(filter(CheckEven, Data))
    print("List after filter :", FData)
    MData = list(map(Square, FData))
    print("List after map :", MData)
    Result = reduce(Addition, MData)
    print("Output of reduce :", Result)


if __name__ == "__main__":
    main()
