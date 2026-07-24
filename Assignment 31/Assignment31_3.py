import os
import schedule
import time
from datetime import datetime
 
def ScanDirectory(path):
 
    if not os.path.isdir(path):
        print("Invalid Directory")
        return
 
    files = 0
    folders = 0
 
    for item in os.listdir(path):
 
        fullpath = os.path.join(path, item)
 
        if os.path.isfile(fullpath):
            files += 1
 
        elif os.path.isdir(fullpath):
            folders += 1
 
    print("\nDirectory Scanned :", path)
    print("Total Files :", files)
    print("Total Subdirectories :", folders)
    print("Scan Time :", datetime.now().strftime("%d-%m-%Y %I:%M:%S %p"))
    print("-------------------------------------------")
 
def main():
 
    directory = input("Enter directory path : ")
 
    schedule.every(1).minutes.do(ScanDirectory, directory)
 
    print("Scheduler Started...")
 
    while True:
        schedule.run_pending()
        time.sleep(1)
 
if __name__ == "__main__":
    main()