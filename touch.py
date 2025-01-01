import os
import sys
import time
from datetime import datetime

def modC(fileName):
    """Handles the -c option (no file creation)."""
    if not os.path.exists(fileName):
        print(f"File '{fileName}' does not exist. Skipping creation (-c).")
    else:
        print(f"File '{fileName}' exists. No action taken.")

def modA(fileName):
    """Handles the -a option (update access time)."""
    if os.path.exists(fileName):
        current_time = time.time()
        mtime = os.stat(fileName).st_mtime  # Keep modification time unchanged
        os.utime(fileName, (current_time, mtime))
        print(f"Access time updated for '{fileName}'.")
    else:
        print(f"File '{fileName}' does not exist.")

def modM(fileName):
    """Handles the -m option (update modification time)."""
    if os.path.exists(fileName):
        current_time = time.time()
        atime = os.stat(fileName).st_atime  # Keep access time unchanged
        os.utime(fileName, (atime, current_time))
        print(f"Modification time updated for '{fileName}'.")
    else:
        print(f"File '{fileName}' does not exist.")

def modR(fileName, referenceFile):
    """Handles the -r option (reference another file's timestamps)."""
    if os.path.exists(fileName) and os.path.exists(referenceFile):
        ref_stat = os.stat(referenceFile)
        os.utime(fileName, (ref_stat.st_atime, ref_stat.st_mtime))
        print(f"Timestamps for '{fileName}' updated to match '{referenceFile}'.")
    else:
        print(f"Either '{fileName}' or reference file '{referenceFile}' does not exist.")

def modD(fileName, timeString):
    """Handles the -d option (set specific timestamps)."""
    if os.path.exists(fileName):
        try:
            timestamp = time.mktime(datetime.strptime(timeString, "%Y-%m-%d %H:%M:%S").timetuple())
            os.utime(fileName, (timestamp, timestamp))
            print(f"Timestamps for '{fileName}' set to '{timeString}'.")
        except ValueError:
            print("Invalid time format. Use 'YYYY-MM-DD HH:MM:SS'.")
    else:
        print(f"File '{fileName}' does not exist.")

def main():
    if len(sys.argv) < 3:
        print("Usage: touch <modifier> <fileName> [<extra_argument>]")
        return

    mod = sys.argv[1].replace("-", "")  # Remove the dash from the modifier
    fileName = sys.argv[2]

    if mod == "c":
        modC(fileName)
    elif mod == "a":
        modA(fileName)
    elif mod == "m":
        modM(fileName)
    elif mod == "r":
        if len(sys.argv) < 4:
            print("Error: Reference file is required for -r.")
            return
        referenceFile = sys.argv[3]
        modR(fileName, referenceFile)
    elif mod == "d":
        if len(sys.argv) < 4:
            print("Error: Time string is required for -d.")
            return
        timeString = sys.argv[3]
        modD(fileName, timeString)
    else:
        print("Error: Modifier is invalid")

if __name__ == "__main__":
    main()

