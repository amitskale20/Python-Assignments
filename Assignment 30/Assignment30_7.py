# 7. Automatically Create Backup of a File Every Hour

import schedule
import time
import shutil
 
def Backup():
    source = input("Enter source file name: ")
    destination = input("Enter backup file name: ")
 
    shutil.copy(source, destination)
 
    print("Backup created successfully.")
 
def main():
    schedule.every(1).hours.do(Backup)
 
    print("Scheduler Started...")
 
    while True:
        schedule.run_pending()
        time.sleep(1)
 
if __name__ == "__main__":
    main()