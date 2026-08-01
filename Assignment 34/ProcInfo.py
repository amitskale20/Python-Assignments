import sys
import ProcessModule

def main():
    if len(sys.argv)==1:
        plist=ProcessModule.GetProcessInfo()
        for p in plist:
            print(f"Name: {p['name']} PID: {p['pid']} User: {p['username']}")
    elif len(sys.argv)==2:
        plist=ProcessModule.SearchProcess(sys.argv[1])
        if len(plist)==0:
            print("Process not found")
        else:
            for p in plist:
                print(f"Name: {p['name']} PID: {p['pid']} User: {p['username']}")
    else:
        print("Usage:")
        print("python ProcInfo.py")
        print("python ProcInfo.py ProcessName")

if __name__=='__main__':
    main()
