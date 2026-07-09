# 1. Write a program that accepts a list of integers and uses Pool.map() 
# to calculate the sum of squares from 1 to N for every element in the 
# list.

import multiprocessing
import os
import time


def SumSquare(No):

    print("Process ID :", os.getpid())

    Sum = 0

    for i in range(1, No + 1):
        Sum = Sum + (i * i)

    print("Input Number :", No)

    return Sum


def main():

    Data = [1000000, 2000000, 3000000, 4000000]

    StartTime = time.perf_counter()

    pobj = multiprocessing.Pool()

    Result = pobj.map(SumSquare, Data)

    pobj.close()
    pobj.join()

    EndTime = time.perf_counter()

    print("Result :", Result)

    print(f"Time Required : {EndTime - StartTime:.4f} seconds")


if __name__ == "__main__":
    main()