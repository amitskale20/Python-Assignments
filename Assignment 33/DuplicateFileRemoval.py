##########################################################
#
#   Import Required Libraries
#
##########################################################

import sys
import os
import time
import schedule

import DuplicateModule
import MailSender

##########################################################
#
#   Function name :     DuplicateFileRemoval
#   Input :             Directory Name, Receiver Email
#   Description :       Removes duplicate files and
#                       sends email
#   Date :              24/07/2026
#   Author :            Amit Sahebrao Kale
#
##########################################################

def DuplicateFileRemoval(DirectoryName,Receiver):

    LogFileName,Statistics = DuplicateModule.CreateLog(DirectoryName)

    Ret = MailSender.SendMail(Receiver,LogFileName,Statistics)

    if(Ret == True):
        print("Email sent successfully")
    else:
        print("Unable to send email")

##########################################################
#
#   Function name :     main
#   Input :             Command Line Arguments
#   Description :       Entry point of automation script
#   Date :              24/07/2026
#   Author :            Amit Sahebrao Kale
#
##########################################################

def main():

    Border = "-" * 50

    print(Border)
    print(" Marvellous Automation Script ")
    print(Border)

    if(len(sys.argv) == 2):

        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):

            print("Duplicate File Removal Automation")
            print("This script removes duplicate files,")
            print("creates a log file and sends email.")
            print("Use --u option for usage.")

        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):

            print("Usage :")
            print("python DuplicateFileRemoval.py")
            print("<DirectoryPath>")
            print("<IntervalInMinutes>")
            print("<ReceiverEmail>")

        else:

            print("Invalid option")

    elif(len(sys.argv) == 4):

        DirectoryName = sys.argv[1]

        if(os.path.exists(DirectoryName) == False):

            print("Directory does not exist")
            return

        if(os.path.isdir(DirectoryName) == False):

            print("Invalid Directory")
            return

        try:

            Interval = int(sys.argv[2])

            if(Interval <= 0):

                print("Interval should be greater than zero")
                return

        except ValueError:

            print("Invalid interval")
            return

        Receiver = sys.argv[3]

        print("Automation Started...")

        DuplicateFileRemoval(DirectoryName,Receiver)

        schedule.every(Interval).minutes.do(
            DuplicateFileRemoval,
            DirectoryName,
            Receiver
        )

        while(True):

            schedule.run_pending()

            time.sleep(1)

    else:

        print("Invalid number of arguments")
        print("Use --h or --u option")

    print(Border)
    print(" Thank you for using Marvellous Automation ")
    print(Border)

##########################################################
#
#   Starter
#
##########################################################

if __name__ == "__main__":
    main()