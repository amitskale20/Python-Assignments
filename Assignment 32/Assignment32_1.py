# 1. Create a New Text File Every Minute
# Create a new text file every minute. 
# The filename should contain the current timestamp. Write the filename, creation date, 
# and creation time into the file.

import schedule
import time
from datetime import datetime
 
def CreateFile():
    current = datetime.now()
 
    filename = current.strftime("File_%d_%m_%Y_%H_%M_%S.txt")
 
    file = open(filename, "w")
 
    file.write("Filename : " + filename + "\n")
    file.write("Creation Date : " + current.strftime("%d-%m-%Y") + "\n")
    file.write("Creation Time : " + current.strftime("%I:%M:%S %p"))
 
    file.close()
 
    print(filename, "created successfully.")
 
def main():
    schedule.every(1).minutes.do(CreateFile)
 
    print("Scheduler Started...")
 
    while True:
        schedule.run_pending()
        time.sleep(1)
 
if __name__ == "__main__":
    main()