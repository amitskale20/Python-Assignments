from functools import reduce


def ChkPrime(No):
    if No <= 1:
        return False

    for i in range(2, No):
        if No % i == 0:
            return False

    return True


Double = lambda No : No * 2
Maximum = lambda A, B : A if A > B else B


def main():

    size = int(input("Enter number of elements : "))

    Data = []

    for i in range(size):
        no = int(input("Enter number : "))
        Data.append(no)

    print("Input List :", Data)

    FData = list(filter(ChkPrime, Data))
    print("List after filter :", FData)
    MData = list(map(Double, FData))
    print("List after map :", MData)
    Result = reduce(Maximum, MData)
    print("Output of reduce :", Result)


if __name__ == "__main__":
    main()
