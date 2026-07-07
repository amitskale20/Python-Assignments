# Shared Counter Using Lock
import threading

Counter = 0

LockObj = threading.Lock()


def Increment():

    global Counter

    for i in range(100000):

        LockObj.acquire()

        Counter = Counter + 1

        LockObj.release()


def main():

    T1 = threading.Thread(target=Increment)
    T2 = threading.Thread(target=Increment)

    T1.start()
    T2.start()

    T1.join()
    T2.join()

    print("Final Counter Value :", Counter)


if __name__ == "__main__":
    main()