import schedule
import time
 
def MondayTask():
    print("Start your weekly goals")
 
def WednesdayTask():
    print("Review your weekly progress")
 
def FridayTask():
    print("Weekly work completed")
 
def main():
 
    schedule.every().monday.at("09:00").do(MondayTask)
 
    schedule.every().wednesday.at("17:00").do(WednesdayTask)
 
    schedule.every().friday.at("18:00").do(FridayTask)
 
    print("Scheduler Started...")
 
    while True:
        schedule.run_pending()
        time.sleep(1)
 
if __name__ == "__main__":
    main()