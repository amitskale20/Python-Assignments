# 5. Write Current Date and Time into a Log File Every 5 Minutes

import schedule
import time
from datetime import datetime
 
def WriteLog():
    file = open("Marvellous.log", "a")
 
    current = datetime.now()
 
    file.write(current.strftime("%d-%m-%Y %H:%M:%S"))
    file.write("\n")
 
    file.close()
 
    print("Log updated successfully.")
 
def main():
    schedule.every(5).minutes.do(WriteLog)
 
    print("Scheduler Started...")
 
    while True:
        schedule.run_pending()
        time.sleep(1)
 
if __name__ == "__main__":
    main()