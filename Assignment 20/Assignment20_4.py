import threading


def Small(Str):

    Count = 0

    for Ch in Str:

        if Ch.islower():
            Count += 1

    print("Thread ID:", threading.get_ident())
    print("Thread Name:", threading.current_thread().name)
    print("Small characters:", Count)



def Capital(Str):

    Count = 0

    for Ch in Str:

        if Ch.isupper():
            Count += 1

    print("Thread ID:", threading.get_ident())
    print("Thread Name:", threading.current_thread().name)
    print("Capital characters:", Count)



def Digits(Str):

    Count = 0

    for Ch in Str:

        if Ch.isdigit():
            Count += 1

    print("Thread ID:", threading.get_ident())
    print("Thread Name:", threading.current_thread().name)
    print("Digits:", Count)



def main():

    Value = input("Enter string : ")

    T1 = threading.Thread(target=Small, args=(Value,), name="Small")
    T2 = threading.Thread(target=Capital, args=(Value,), name="Capital")
    T3 = threading.Thread(target=Digits, args=(Value,), name="Digits")

    T1.start()
    T1.join()
    T2.start()
    T2.join()
    T3.start()
    T3.join()



if __name__ == "__main__":
    main()