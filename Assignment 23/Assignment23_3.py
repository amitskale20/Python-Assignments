# Count Even: Count Even Numbers Between 1 and N Using Multiprocessing

import multiprocessing
import os
import time


def CountEven(No):

    print("Process ID :", os.getpid())

    Count = 0

    for i in range(1, No + 1):

        if i % 2 == 0:
            Count = Count + 1

    print("Input Number :", No)
    print(f"Even Number Count for {No} :", Count)

    return Count


def main():

    Data = [1000000, 2000000, 3000000, 4000000]

    StartTime = time.perf_counter()

    pobj = multiprocessing.Pool()

    Result = pobj.map(CountEven, Data)

    pobj.close()
    pobj.join()

    EndTime = time.perf_counter()

    print("Result :", Result)

    print(f"Time Required : {EndTime - StartTime:.4f} seconds")


if __name__ == "__main__":
    main()