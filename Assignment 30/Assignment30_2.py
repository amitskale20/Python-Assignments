# 2. Display Current Date and Time Every One Minute

import schedule
import time
from datetime import datetime
 
def ShowDateTime():
    current = datetime.now()
 
    print("Current Date and Time:",
          current.strftime("%d-%m-%Y %I:%M:%S %p"))
 
def main():
    schedule.every(1).minutes.do(ShowDateTime)
 
    print("Scheduler started...")
 
    while True:
        schedule.run_pending()
        time.sleep(1)
 
if __name__ == "__main__":
    main()