# 6. Schedule Two Different Tasks
# Problem Statement
# Print "Good Morning" every day at 9:00 AM.
# Print "Good Night" every day at 10:00 PM.

import schedule
import time
 
def GoodMorning():
    print("Good Morning")
 
def GoodNight():
    print("Good Night")
 
def main():
    schedule.every().day.at("09:00").do(GoodMorning)
    schedule.every().day.at("22:00").do(GoodNight)
 
    print("Scheduler Started...")
 
    while True:
        schedule.run_pending()
        time.sleep(1)
 
if __name__ == "__main__":
    main()