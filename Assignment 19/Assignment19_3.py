from functools import reduce

CheckRange = lambda No : No >= 70 and No <= 90
Increase = lambda No : No + 10
Product = lambda A, B : A * B


def main():

    Data = [4, 34, 36, 76, 68, 24, 89, 23, 86, 90, 45, 70]

    print("Input List :", Data)

    FData = list(filter(CheckRange, Data))
    print("List after filter :", FData)

    MData = list(map(Increase, FData))
    print("List after map :", MData)

    Result = reduce(Product, MData)
    print("Output of reduce :", Result)


if __name__ == "__main__":
    main()