# Duplicate File Removal Automation Using Python

## Project Description

This automation project periodically scans a specified directory,
identifies duplicate files using MD5 checksum,
deletes duplicate copies,
creates a detailed log file,
and sends the generated log file to the specified email address.

---

## Features

- Recursive Directory Scanning
- MD5 Checksum Based Duplicate Detection
- Automatic Duplicate File Deletion
- Timestamp Based Log File
- Periodic Execution
- Email Notification
- Log File Attachment
- Input Validation
- Exception Handling
- Modular Programming

---

## Python Version

Python 3.x

---

## Required Libraries

- os
- sys
- time
- hashlib
- schedule
- smtplib
- email
- re

Install schedule package

pip install schedule

---

## Project Structure

DuplicateFileRemoval.py

DuplicateModule.py

MailSender.py

README.md

Marvellous/
    DuplicateRemovalLog_Date_Time.log

---

## Command Line Arguments

Argument 1

Absolute Directory Path

Argument 2

Time Interval in Minutes

Argument 3

Receiver Email Address

---

## Execution Command

python DuplicateFileRemoval.py "E:\Demo" 1 yourmail@gmail.com

---

## Help

python DuplicateFileRemoval.py --h

---

## Usage

python DuplicateFileRemoval.py --u

---

## Log File Information

The log file is automatically created inside the
Marvellous directory.

Example

DuplicateRemovalLog_Sat_Jul_25_12_15_10_2026.log

The log contains

- Starting Time
- Completion Time
- Directory Name
- Total Files Scanned
- Duplicate Files Found
- Duplicate Files Deleted
- Deleted File Names
- Errors
- Email Status

---

## Email Configuration

Open MailSender.py

Replace

Sender = "yourgmail@gmail.com"

Password = "Your_16_Digit_App_Password"

with your Gmail address and Google App Password.

---

## Important Notes

- Duplicate files are detected using MD5 checksum.
- One original file is preserved.
- Remaining duplicate files are deleted.
- Deleted files cannot be recovered.
- Test the application on a sample directory before using it on important data.
- Do not hard-code your personal email password.
