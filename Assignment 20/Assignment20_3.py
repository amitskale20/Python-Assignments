import threading


def EvenList(Data):

    Sum = 0

    for No in Data:

        if No % 2 == 0:
            Sum = Sum + No

    print("Sum of Even Elements :", Sum)



def OddList(Data):

    Sum = 0

    for No in Data:

        if No % 2 != 0:
            Sum = Sum + No

    print("Sum of Odd Elements :", Sum)



def main():

    size = int(input("Enter number of elements : "))

    Data = []

    for i in range(size):
        no = int(input("Enter number : "))
        Data.append(no)

    T1 = threading.Thread(target=EvenList, args=(Data,))
    T2 = threading.Thread(target=OddList, args=(Data,))

    T1.start()
    T2.start()

    T1.join()
    T2.join()


if __name__ == "__main__":
    main()
