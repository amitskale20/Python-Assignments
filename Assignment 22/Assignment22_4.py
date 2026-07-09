# 4. Write a program that calculates
# 1^5+2^5+3^5+…..+N^5
# for multiple values of N simultaneously using Pool.
# Input [1000000,2000000,3000000,4000000]
# Measure total execution time

import multiprocessing
import os
import time


def SumPowerFive(No):

    print("Process ID :", os.getpid())

    Sum = 0

    for i in range(1, No + 1):
        Sum = Sum + (i ** 5)

    print("Input Number :", No)

    return Sum


def main():

    Data = [1000000, 2000000, 3000000, 4000000]

    StartTime = time.perf_counter()

    pobj = multiprocessing.Pool()

    Result = pobj.map(SumPowerFive, Data)

    pobj.close()
    pobj.join()

    EndTime = time.perf_counter()

    print("Result :")
    print(Result)

    print(f"Time Required : {EndTime - StartTime:.4f} seconds")


if __name__ == "__main__":
    main()