# 4. Print "Namaskar..." Every Day at 9:00 AM

import schedule
import time
 
def Greeting():
    print("Namaskar...")
 
def main():
    schedule.every().day.at("09:00").do(Greeting)
 
    print("Waiting for 09:00 AM...")
 
    while True:
        schedule.run_pending()
        time.sleep(1)
 
if __name__ == "__main__":
    main()