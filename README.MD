# FileOrganizer

This simple script will organize your files into different folders based on file type

## Installation

1. Clone this repository to your target directory

```
git clone https://github.com/Sohgeki/FileOrganizer
```

2. Execute using the following command

```
Windows
python fileorg.py
```
```
Linux
python3 fileorg.py
```

## Usage

Running this script will ask you what directory to search and organize files from.
It will then find and filter files into 4 different folders: 
```
Documents: txt, docx, pdf, ini, rtf, pptx
Pictures: png, jpg, jpeg, gif, xwd
Music: mp3, wav, flac, aac, au, aiff, pcm, ogg, alac, wma
Videos: mp4, mkv, avi, webm, wmv, mpeg, mov, flv
```

You can give certain arguments to control what files or directories to organize:
```
python fileorg.py ./Files/  : Specify what directory to organize
```
```
python fileorg.py -f mp3 webm exe txt -d ./Files/ : Specify file type and directory to move files to
```

