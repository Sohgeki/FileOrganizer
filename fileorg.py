import os
import sys
import shutil
import extensions
from extensions import *

def main():
    try:
        os.chdir(dir)
    except OSError:
        print("Directory does not exist.")
        exit(0)

    files = []
    with os.scandir(dir) as it:
        for entry in it:
            if not entry.name.startswith('.') and entry.is_file():
                files.append(entry.name)


    print(f"\nChecking file types and moving them to corresponding folders...\n")
    if len(files) > 0:
        pic(dir, files)
        music(dir, files)
        video(dir, files)
        text(dir, files)
    else:
        print("No files found!")
        exit(0)


if(len(sys.argv) == 1):
    print("Enter directory: ")
    dir = input("> ")
    if dir.startswith('./'):
        dir = str(os.getcwd())
    main()

elif(len(sys.argv) == 2):
    dir = sys.argv[1]
    str(dir)
    main()

elif(sys.argv[1].endswith(('f', 'files', 'extensions', 'ext'))):
    ext = []
    dir = ''
    for x in range(len(sys.argv)):
        if sys.argv[x].endswith(('d', 'dir', 'destination')):
            dir = sys.argv[x+1]
            break
        else:
            ext.append(sys.argv[x])

    del ext[:2]
    custom(dir, ext)

else:
    print("Invalid number of arguments! Exiting...")
    exit(0)
