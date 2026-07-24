# 5. Delete All Empty Files Every Hour
# Write a program that
# Scans the directory recursively.
# Detects empty files (0 bytes).
# Deletes empty files.
# Stores deleted file paths in a log file.
# Handles permission errors.

import os
import schedule
import time
from datetime import datetime
 
def DeleteEmptyFiles(directory):
 
    logfile = open("DeleteLog.txt", "a")
 
    for foldername, subfolders, filenames in os.walk(directory):
 
        for file in filenames:
 
            filepath = os.path.join(foldername, file)
 
            try:
 
                if os.path.getsize(filepath) == 0:
 
                    os.remove(filepath)
 
                    logfile.write(filepath + " deleted ")
                    logfile.write(datetime.now().strftime("%d-%m-%Y %I:%M:%S %p"))
                    logfile.write("\n")
 
                    print(filepath, "deleted.")
 
            except PermissionError:
                logfile.write("Permission denied : " + filepath + "\n")
 
            except Exception as e:
                logfile.write(str(e) + "\n")
 
    logfile.close()
 
def main():
 
    directory = input("Enter directory : ")
 
    schedule.every(1).hours.do(DeleteEmptyFiles, directory)
 
    print("Scheduler Started...")
 
    while True:
        schedule.run_pending()
        time.sleep(1)
 
if __name__ == "__main__":
    main()