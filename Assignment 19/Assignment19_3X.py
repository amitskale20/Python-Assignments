from functools import reduce

CheckRange = lambda No : No >= 70 and No <= 90
Increase = lambda No : No + 10
Product = lambda A, B : A * B


def main():

    size = int(input("Enter number of elements : "))

    Data = []

    for i in range(size):
        no = int(input("Enter number : "))
        Data.append(no)

    print("Input List :", Data)

    FData = list(filter(CheckRange, Data))
    print("List after filter :", FData)

    MData = list(map(Increase, FData))
    print("List after map :", MData)

    Result = reduce(Product, MData)
    print("Output of reduce :", Result)


if __name__ == "__main__":
    main()