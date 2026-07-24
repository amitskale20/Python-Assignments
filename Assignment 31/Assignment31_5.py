import os
import schedule
import time
from datetime import datetime
 
def CountFiles(directory):
 
    if not os.path.isdir(directory):
        print("Invalid Directory")
        return
 
    count = 0
 
    for item in os.listdir(directory):
 
        path = os.path.join(directory, item)
 
        if os.path.isfile(path):
            count += 1
 
    file = open("DirectoryCountLog.txt", "a")
 
    file.write("Directory : " + directory + "\n")
    file.write("Total Files : " + str(count) + "\n")
    file.write("Scan Time : ")
    file.write(datetime.now().strftime("%d-%m-%Y %I:%M:%S %p"))
    file.write("\n")
    file.write("-" * 40)
    file.write("\n")
 
    file.close()
 
    print("Directory scanned successfully.")
    print("Total Files :", count)
 
def main():
 
    directory = input("Enter directory path : ")
 
    schedule.every(5).minutes.do(CountFiles, directory)
 
    print("Scheduler Started...")
 
    while True:
        schedule.run_pending()
        time.sleep(1)
 
if __name__ == "__main__":
    main()