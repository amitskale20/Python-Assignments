# Sum Even: Sum of All Even Numbers from 1 to N Using Multiprocessing

import multiprocessing
import os
import time


def SumEven(No):

    print("Process ID :", os.getpid())

    Sum = 0

    for i in range(2, No + 1, 2):
        Sum = Sum + i

    print("Input Number :", No)
    print("Sum of Even Numbers :", Sum)

    return Sum


def main():

    Data = [1000000, 2000000, 3000000, 4000000]

    StartTime = time.perf_counter()

    pobj = multiprocessing.Pool()

    Result = pobj.map(SumEven, Data)

    pobj.close()
    pobj.join()

    EndTime = time.perf_counter()

    print("Result :", Result)

    print(f"Time Required : {EndTime-StartTime:.4f} seconds")


if __name__ == "__main__":
    main()