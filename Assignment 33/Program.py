import sys
import os
import schedule
import time
import re
 
def DisplayHelp():
 
    print("Duplicate File Removal Automation")
    print("---------------------------------")
    print("This application removes duplicate files")
    print("and sends the log file through email.")
 
def DisplayUsage():
 
    print("Usage :")
    print("python DuplicateFileRemoval.py")
    print("<DirectoryPath> <TimeInterval> <EmailID>")
 
def ValidateDirectory(path):
 
    if os.path.isdir(path):
        return True
 
    return False
 
def ValidateInterval(interval):
 
    if interval.isdigit() and int(interval) > 0:
        return True
 
    return False
 
def ValidateEmail(email):
 
    pattern = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'
 
    if re.match(pattern, email):
        return True
 
    return False
 
def main():
 
    if len(sys.argv) == 2:
 
        if sys.argv[1] == "--help" or sys.argv[1] == "-h":
            DisplayHelp()
            return
 
        elif sys.argv[1] == "--usage" or sys.argv[1] == "-u":
            DisplayUsage()
            return
 
    if len(sys.argv) != 4:
 
        print("Invalid Number of Arguments")
        DisplayUsage()
        return
 
    directory = sys.argv[1]
    interval = sys.argv[2]
    email = sys.argv[3]
 
    if ValidateDirectory(directory) == False:
 
        print("Invalid Directory")
        return
 
    if ValidateInterval(interval) == False:
 
        print("Invalid Time Interval")
        return
 
    if ValidateEmail(email) == False:
 
        print("Invalid Email Address")
        return
 
    if os.path.exists("Marvellous") == False:
 
        os.mkdir("Marvellous")
 
    print("All Inputs are Valid")
    print("Automation Started...")
 
    while True:
 
        print("Scanning Directory :", directory)
 
        schedule.run_pending()
 
        time.sleep(1)
 
if __name__ == "__main__":
    main()