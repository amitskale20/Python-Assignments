# # 2. Monitor File Size Every 30 Seconds
# Monitor the size of a specified file every 30 seconds and store the following details in FileSizeLog.txt:
# File path
# File size in bytes
# Date and time
# Handle the case where the file does not exist.

import os
import schedule
import time
from datetime import datetime
 
def MonitorFile(filename):
    file = open("FileSizeLog.txt", "a")
 
    if os.path.exists(filename):
        size = os.path.getsize(filename)
 
        file.write("File : " + filename + "\n")
        file.write("Size : " + str(size) + " bytes\n")
        file.write("Time : " +
                   datetime.now().strftime("%d-%m-%Y %I:%M:%S %p"))
        file.write("\n\n")
 
        print("File information stored.")
    else:
        file.write(filename + " does not exist.\n\n")
        print("File does not exist.")
 
    file.close()
 
def main():
    filename = input("Enter file name : ")
 
    schedule.every(30).seconds.do(MonitorFile, filename)
 
    print("Monitoring Started...")
 
    while True:
        schedule.run_pending()
        time.sleep(1)
 
if __name__ == "__main__":
    main()