import schedule
import time
from datetime import datetime
 
def CreateLogFile():
 
    current = datetime.now()
 
    filename = current.strftime("MarvellousLog_%d_%m_%Y_%H_%M_%S.txt")
 
    file = open(filename, "w")
 
    file.write("Log File Created Successfully\n")
    file.write("Creation Time : ")
    file.write(current.strftime("%d-%m-%Y %I:%M:%S %p"))
 
    file.close()
 
    print(filename, "created successfully.")
 
def main():
 
    schedule.every(10).minutes.do(CreateLogFile)
 
    print("Scheduler Started...")
 
    while True:
        schedule.run_pending()
        time.sleep(1)
 
if __name__ == "__main__":
    main()