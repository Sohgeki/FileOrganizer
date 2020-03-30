import os
import shutil

#Organizes pictures
def pic(dir, file):
    pics = []
    for ext in file:
        if ext.endswith(('png', 'jpg', 'jpeg', 'gif', 'xwd')):
            pics.append(ext)

    if len(pics) > 0:
        destination = dir + '/Pictures'
        if not os.path.exists(destination):
            os.mkdir(destination)
    else:
        print('No images found!')
        return

    for img in pics:
        print(f"Moving {img} to {destination}")
        shutil.move(img, destination)

#Organizes text files
def text(dir, file):
    txt = []
    for ext in file:
        if ext.endswith(('txt', 'docx', 'pdf', 'ini', 'rtf', 'pptx')):
            txt.append(ext)

    if len(txt) > 0:
        destination = dir + '/Documents'
        if not os.path.exists(destination):
            os.mkdir(destination)
    else:
        print("No text files found!")
        return
    
    for t in txt:
        print(f"Moving {t} to {destination}")
        shutil.move(t, destination)

#Organizes music
def music(dir, file):
    audio = []
    for ext in file:
        if ext.endswith(('mp3', 'flac', 'wav', 'webm', 'au', 'aiff', 'pcm', 'aac', 'ogg', 'alac', 'wma')):
            audio.append(ext)

    if len(audio) > 0:
        destination = dir + '/Music'
        if not os.path.exists(destination):
            os.mkdir(destination)
    
    else:
        print("No audio files found!")
        return

    for a in audio:
        print(f"Moving {a} to {destination}")
        shutil.move(a,destination)

#Organizes videos
def video(dir, file):
    media = []
    for ext in file:
        if ext.endswith(('mp4', 'mkv', 'avi', 'webm', 'wmv', 'mpeg', 'mov', 'flv')):
            media.append(ext)

    if len(media) > 0:
        destination = dir + '/Videos'
        if not os.path.exists(destination):
            os.mkdir(destination)

    else:
        print("No video files found!")
        return

    for vid in media:
        print(f"Moving {vid} to {destination}")
        shutil.move(vid, destination)

#Organizes files with extensions user specifies
def custom(dir, ext):
    if dir.startswith('/'):
        dir = str(os.getcwd()) + dir
    elif dir.startswith(('./', ':')):
        print("Invalid directory")
        exit(0)
    
    files = []
    with os.scandir(os.getcwd()) as it:
        for entry in it:
            if entry.name.endswith(tuple(ext)) and entry.is_file():
                files.append(entry.name)

    if len(files) > 0:
        print("\nList of files found: ")
        print(*files, sep = '\n')
        print()
        if not os.path.exists(dir):
            os.mkdir(dir)

    else:
        print("No files found!")
        exit(0)

    for f in files:
        print(f"Moving {f} to {dir}")
        shutil.move(f,dir)
    
    print("Done")
    exit(0)
    

