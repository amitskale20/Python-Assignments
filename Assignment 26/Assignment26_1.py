class Demo:
    
    Value = 100

    def __init__(self, A, B):
        self.no1 = A
        self.no2 = B

    def Fun(self):
        print("Inside Fun")
        print("no1 :", self.no1)
        print("no2 :", self.no2)

    def Gun(self):
        print("Inside Gun")
        print("no1 :", self.no1)
        print("no2 :", self.no2)


def main():

    Obj1 = Demo(11, 21)
    Obj2 = Demo(51, 101)

    Obj1.Fun()
    Obj2.Fun()
    Obj1.Gun()
    Obj2.Gun()


if __name__ == "__main__":
    main()