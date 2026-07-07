# Sum and Product of List Elements

import threading

SumResult = 0
ProductResult = 1


def SumList(Data):

    global SumResult

    for No in Data:
        SumResult = SumResult + No


def ProductList(Data):

    global ProductResult

    for No in Data:
        ProductResult = ProductResult * No


def main():

    size = int(input("Enter number of elements : "))

    Data = []

    for i in range(size):
        no = int(input("Enter number : "))
        Data.append(no)

    T1 = threading.Thread(target=SumList, args=(Data,))
    T2 = threading.Thread(target=ProductList, args=(Data,))

    T1.start()
    T2.start()

    T1.join()
    T2.join()

    print("Sum of elements :", SumResult)
    print("Product of elements :", ProductResult)


if __name__ == "__main__":
    main()