# 3. Read and Display File Every Minute
# Read and display the contents of a specified text file every minute.
# Handle the following exceptions:
# File does not exist
# File is empty
# Permission denied
# File cannot be opened.

import schedule
import time
 
def DisplayFile(filename):
    try:
        file = open(filename, "r")
 
        data = file.read()
 
        if len(data) == 0:
            print("File is empty.")
        else:
            print("\nFile Contents:")
            print(data)
 
        file.close()
 
    except FileNotFoundError:
        print("File does not exist.")
 
    except PermissionError:
        print("Permission denied.")
 
    except IOError:
        print("File cannot be opened.")
 
def main():
    filename = input("Enter file name : ")
 
    schedule.every(1).minutes.do(DisplayFile, filename)
 
    print("Scheduler Started...")
 
    while True:
        schedule.run_pending()
        time.sleep(1)
 
if __name__ == "__main__":
    main()