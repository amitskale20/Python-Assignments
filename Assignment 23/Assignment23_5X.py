# Factorial: Factorial of Multiple Numbers Using multiprocessing.Pool() with detailed explanation.

import multiprocessing
import os
import time
import math


def Factorial(No):

    print("Process ID :", os.getpid())
    print("Input Number :", No)

    Result = math.factorial(No)

    print("Factorial :", Result)

    return Result


def main():

    size = int(input("Enter number of elements:"))

    Data = []

    for i in range(size):
        no = int(input("Enter the element:"))
        Data.append(no)        

    StartTime = time.perf_counter()

    pobj = multiprocessing.Pool()

    Result = pobj.map(Factorial, Data)

    pobj.close()
    pobj.join()

    EndTime = time.perf_counter()

    print("Final Result :", Result)

    print(f"Time Required : {EndTime - StartTime:.4f} seconds")


if __name__ == "__main__":
    main()