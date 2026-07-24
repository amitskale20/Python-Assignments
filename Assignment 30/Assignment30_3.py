# 3. Print "Coding Kar..!" Every 30 Minutes

import schedule
import time
 
def Coding():
    print("Coding Kar..!")
 
def main():
    schedule.every(30).minutes.do(Coding)
 
    print("Scheduler started...")
 
    while True:
        schedule.run_pending()
        time.sleep(1)
 
if __name__ == "__main__":
    main()