# 4. Copy All .txt Files from One Directory to Another Every 10 Minutes 
# Write a program that:
# Accepts source and destination directories.
# Validates both directories. 
# Copies only .txt files. 
# Maintains a log of copied files.
# Continues execution even if one file cannot be copied.

import os
import shutil
import schedule
import time
from datetime import datetime
 
def CopyTextFiles(source, destination):
 
    if not os.path.isdir(source):
        print("Source directory does not exist.")
        return
 
    if not os.path.isdir(destination):
        print("Destination directory does not exist.")
        return
 
    logfile = open("CopyLog.txt", "a")
 
    for file in os.listdir(source):
 
        if file.endswith(".txt"):
 
            sourcefile = os.path.join(source, file)
            destinationfile = os.path.join(destination, file)
 
            try:
                shutil.copy(sourcefile, destinationfile)
 
                logfile.write(file + " copied successfully. ")
                logfile.write(datetime.now().strftime("%d-%m-%Y %I:%M:%S %p"))
                logfile.write("\n")
 
                print(file, "copied.")
 
            except Exception as e:
                logfile.write(file + " : " + str(e) + "\n")
 
    logfile.close()
 
def main():
 
    source = input("Enter source directory : ")
    destination = input("Enter destination directory : ")
 
    schedule.every(10).minutes.do(CopyTextFiles, source, destination)
 
    print("Scheduler Started...")
 
    while True:
        schedule.run_pending()
        time.sleep(1)
 
if __name__ == "__main__":
    main()