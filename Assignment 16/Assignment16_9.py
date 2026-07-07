# 9. Write a program which display first 10 even numbers on screen. 
# Output : 4 6 8 10 12 14 16 18 20 
def EvenNumbers():
    for i in range(1, 11):
        print(i * 2, end=" ")

def main():
    EvenNumbers()
    
if __name__ == "__main__":
    main()