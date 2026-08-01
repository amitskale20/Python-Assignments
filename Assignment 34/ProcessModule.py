import psutil
import os
import time

def GetProcessInfo():
    data=[]
    for proc in psutil.process_iter(['pid','name','username']):
        try:
            data.append(proc.info)
        except Exception:
            pass
    return data

def SearchProcess(name):
    result=[]
    for p in GetProcessInfo():
        if p.get('name') and p['name'].lower()==name.lower():
            result.append(p)
    return result

def CreateLog(directory):
    os.makedirs(directory,exist_ok=True)
    logfile=os.path.join(directory,'ProcessLog_'+time.ctime().replace(' ','_').replace(':','_')+'.log')
    with open(logfile,'w') as f:
        for p in GetProcessInfo():
            f.write(f"Name: {p['name']} PID: {p['pid']} User: {p['username']}\n")
    return logfile
