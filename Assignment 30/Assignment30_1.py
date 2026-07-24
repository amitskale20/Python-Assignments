# 1. Print "Jay Ganesh..." Every Two Seconds

import schedule
import time
 
def Display():
    print("Jay Ganesh...")
 
def main():
    schedule.every(2).seconds.do(Display)
 
    print("Scheduler started...")
 
    while True:
        schedule.run_pending()
        time.sleep(1)
 
if __name__ == "__main__":
    main()