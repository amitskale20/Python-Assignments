import schedule
import time
 
def Display(message):
    print(message)
 
def main():
 
    message = input("Enter message : ")
 
    interval = int(input("Enter interval in seconds : "))
 
    if interval <= 0:
        print("Interval should be greater than zero.")
        return
 
    schedule.every(interval).seconds.do(Display, message)
 
    print("Scheduler Started...")
 
    while True:
        schedule.run_pending()
        time.sleep(1)
 
if __name__ == "__main__":
    main()