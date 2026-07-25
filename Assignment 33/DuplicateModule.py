##########################################################
#
#   Import Required Libraries
#
##########################################################

import os
import hashlib
import time

##########################################################
#
#   Function name :     CalculateChecksum
#   Input :             File Name
#   Output :            Checksum
#   Description :       Calculates MD5 checksum of file
#   Date :              24/07/2026
#   Author :            Amit Sahebrao Kale
#
##########################################################

def CalculateChecksum(Path):

    hobj = hashlib.md5()

    fobj = open(Path,"rb")

    Buffer = fobj.read(1024)

    while(len(Buffer) > 0):
        hobj.update(Buffer)
        Buffer = fobj.read(1024)

    fobj.close()

    return hobj.hexdigest()

##########################################################
#
#   Function name :     FindDuplicate
#   Input :             Directory Name
#   Output :            Dictionary
#   Description :       Finds duplicate files using checksum
#   Date :              24/07/2026
#   Author :            Amit Sahebrao Kale
#
##########################################################

def FindDuplicate(DirectoryName):

    Duplicate = {}

    TotalFiles = 0

    for FolderName, SubFolder, FileName in os.walk(DirectoryName):

        for fname in FileName:

            fname = os.path.join(FolderName, fname)

            try:

                Checksum = CalculateChecksum(fname)

                if Checksum in Duplicate:
                    Duplicate[Checksum].append(fname)
                else:
                    Duplicate[Checksum] = [fname]

                TotalFiles = TotalFiles + 1

            except PermissionError:
                pass

            except FileNotFoundError:
                pass

            except Exception:
                pass

    return Duplicate, TotalFiles

##########################################################
#
#   Function name :     DisplayDuplicate
#   Input :             Dictionary
#   Output :            None
#   Description :       Displays duplicate files
#   Date :              24/07/2026
#   Author :            Amit Sahebrao Kale
#
##########################################################

def DisplayDuplicate(Data):

    for Key in Data:

        if(len(Data[Key]) > 1):

            print("-----------------------------------------")
            print("Checksum :",Key)

            for FileName in Data[Key]:
                print(FileName)

##########################################################
#
#   Function name :     DeleteDuplicate
#   Input :             Dictionary, Log File Object
#   Output :            Duplicate Count, Deleted Count
#   Description :       Deletes duplicate files
#   Date :              24/07/2026
#   Author :            Amit Sahebrao Kale
#
##########################################################

def DeleteDuplicate(Data, fobj):

    DuplicateCount = 0
    DeletedCount = 0

    for Key in Data:

        if(len(Data[Key]) > 1):

            DuplicateCount = DuplicateCount + (len(Data[Key]) - 1)

            fobj.write("\n")
            fobj.write("Checksum : " + Key + "\n")

            for FileName in Data[Key][1:]:

                try:

                    os.remove(FileName)

                    DeletedCount = DeletedCount + 1

                    fobj.write("Deleted File : " + FileName + "\n")

                except Exception as E:

                    fobj.write("Unable to delete : " + FileName + "\n")
                    fobj.write(str(E) + "\n")

    return DuplicateCount, DeletedCount

##########################################################
#
#   Function name :     CreateLog
#   Input :             Directory Name
#   Output :            Log File Name, Statistics
#   Description :       Creates log file
#   Date :              24/07/2026
#   Author :            Amit Sahebrao Kale
#
##########################################################

def CreateLog(DirectoryName):

    Border = "-" * 50

    if(os.path.exists("Marvellous") == False):
        os.mkdir("Marvellous")

    StartTime = time.ctime()

    LogFileName = "DuplicateRemovalLog_%s.log"%(StartTime)

    LogFileName = LogFileName.replace(" ","_")
    LogFileName = LogFileName.replace(":","_")

    LogFileName = os.path.join("Marvellous",LogFileName)

    fobj = open(LogFileName,"w")

    fobj.write(Border+"\n")
    fobj.write(" Marvellous Automation Script \n")
    fobj.write(Border+"\n\n")

    fobj.write("Starting Time : "+StartTime+"\n")
    fobj.write("Directory Scanned : "+DirectoryName+"\n")
    fobj.write(Border+"\n")

    Data,TotalFiles = FindDuplicate(DirectoryName)

    DuplicateCount,DeletedCount = DeleteDuplicate(Data,fobj)

    EndTime = time.ctime()

    fobj.write(Border+"\n")
    fobj.write("Completion Time : "+EndTime+"\n")
    fobj.write("Total Files Scanned : "+str(TotalFiles)+"\n")
    fobj.write("Duplicate Files Found : "+str(DuplicateCount)+"\n")
    fobj.write("Duplicate Files Deleted : "+str(DeletedCount)+"\n")
    fobj.write(Border+"\n")

    fobj.close()

    Statistics = {
        "StartTime":StartTime,
        "EndTime":EndTime,
        "Directory":DirectoryName,
        "TotalFiles":TotalFiles,
        "Duplicate":DuplicateCount,
        "Deleted":DeletedCount
    }

    return LogFileName, Statistics

