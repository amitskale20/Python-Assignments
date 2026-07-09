# Prime Count

import multiprocessing
import os


def ChkPrime(No):

    if No <= 1:
        return False

    for i in range(2, int(No ** 0.5) + 1):

        if No % i == 0:
            return False

    return True


def PrimeCount(No):

    print("Process ID :", os.getpid())

    Count = 0

    for i in range(1, No + 1):

        if ChkPrime(i):
            Count = Count + 1

    print("Input Number :", No)
    print("Prime Count :", Count)

    return Count


def main():

    Data = [10000, 20000, 30000, 40000]

    pobj = multiprocessing.Pool()

    Result = pobj.map(PrimeCount, Data)

    pobj.close()
    pobj.join()

    print("Final Result :", Result)


if __name__ == "__main__":
    main()