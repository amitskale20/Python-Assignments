# Prime and NonPrime Threads
import threading

def ChkPrime(No):

    if No <= 1:
        return False

    for i in range(2, No):
        if No % i == 0:
            return False

    return True


def Prime(Data):

    print("Prime Numbers :")

    for No in Data:
        if ChkPrime(No):
            print(No, end=" ")

    print()


def NonPrime(Data):

    print("Non Prime Numbers :")

    for No in Data:
        if not ChkPrime(No):
            print(No, end=" ")

    print()


def main():

    size = int(input("Enter number of elements : "))

    Data = []

    for i in range(size):
        no = int(input("Enter number : "))
        Data.append(no)

    T1 = threading.Thread(target=Prime, args=(Data,))
    T2 = threading.Thread(target=NonPrime, args=(Data,))

    T1.start()
    T2.start()

    T1.join()
    T2.join()


if __name__ == "__main__":
    main()