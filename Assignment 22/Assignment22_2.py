# 2.  Write a program that calculates factorials of multiple numbers 
# simultaneously using Pool.map().
# Input [10,15,20,25]
# Display
# • Process ID
# • Input Number
# • Factorial

import multiprocessing
import os
import math
import time


def Factorial(No):

    print("Process ID :", os.getpid())
    print("Input Number :", No)

    Result = math.factorial(No)

    print("Factorial :", Result)

    return Result


def main():

    Data = [10, 15, 20, 25]

    StartTime = time.perf_counter()

    pobj = multiprocessing.Pool()

    Result = pobj.map(Factorial, Data)

    pobj.close()
    pobj.join()

    EndTime = time.perf_counter()

    print("Final Result :", Result)

    print(f"Time Required : {EndTime-StartTime:.4f} seconds")


if __name__ == "__main__":
    main()