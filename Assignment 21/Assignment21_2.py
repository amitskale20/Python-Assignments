# Maximum and Minimum Element
import threading

def Maximum(Data):
    print("Maximum element :", max(Data))


def Minimum(Data):
    print("Minimum element :", min(Data))


def main():

    Size = int(input("Enter number of elements : "))

    Data = []

    for i in range(Size):
        No = int(input("Enter number : "))
        Data.append(No)

    T1 = threading.Thread(target=Maximum, args=(Data,))
    T2 = threading.Thread(target=Minimum, args=(Data,))

    T1.start()
    T2.start()

    T1.join()
    T2.join()


if __name__ == "__main__":
    main()