import sys
import os
import ProcessModule
import MailSender

##########################################################
#
#   Function Name : ProcInfoLog
#   Description   : Creates process log and optionally
#                   sends it through email.
#
##########################################################

def ProcInfoLog(DirectoryName, Email=None):

    try:
        LogFile = ProcessModule.CreateLog(DirectoryName)

        print("Log file created successfully : ", LogFile)

        if Email is not None:
            Ret = MailSender.SendMail(Email, LogFile)

            if Ret:
                print("Email sent successfully")
            else:
                print("Unable to send email")

    except Exception as E:
        print("Error :", E)

##########################################################
#
#   Function Name : main
#
##########################################################

def main():

    if(len(sys.argv) == 2):

        DirectoryName = sys.argv[1]

        ProcInfoLog(DirectoryName)

    elif(len(sys.argv) == 3):

        DirectoryName = sys.argv[1]
        Email = sys.argv[2]

        ProcInfoLog(DirectoryName, Email)

    else:

        print("Usage :")
        print("Assignment 3")
        print("python ProcInfoLog.py DirectoryName")
        print("")
        print("Assignment 4")
        print("python ProcInfoLog.py DirectoryName EmailID")

##########################################################

if __name__ == "__main__":
    main()
