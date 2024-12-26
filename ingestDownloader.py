import os
import sys
import csv
import subprocess
import time
import argparse
from gooey import Gooey, GooeyParser
from pathlib import Path

# Usage:
# Currently, just hop into the venv containing yt-dlp and set your PATH to include ffmpeg location

# C:\Users\Loren\Documents\Development\yt-dlpDownloading\venv\Scripts\activate
# set PATH=%PATH%;C:\Users\Loren\Documents\Development\ffmpeg\ffmpeg-master-latest-win64-gpl\ffmpeg-master-latest-win64-gpl\bin
# ytdlp_dir = r"C:\Users\Loren\Documents\Development\yt-dlpDownloading"
# ffmpeg_dir = r"C:\Users\Loren\Documents\Development\ffmpeg\ffmpeg-master-latest-win64-gpl\ffmpeg-master-latest-win64-gpl\bin"


home = str(Path.home())
default_dir = os.path.join(home, "Desktop")
format_options = [".mp3", ".mp4"]

@Gooey(program_name = "YouTube Downloader")
def main():
    parser = GooeyParser( # Switch to argparse.ArgumentParser() when not using Gooey
        description = "Video Grabbin' Machine!"
    )
    filetype_group = parser.add_argument_group(
        "Output Settings", 
        "Customize your output options"
    )
    singleimport_group = parser.add_argument_group(
        "Single URL Download",
        "Fill in both of the two fields below, then hit Start!"
    )
    importtype_group = parser.add_argument_group(
        "Bulk Download",
        "Select a .csv file containing the list of URLs you'd like to download, then hit Start!"
    )
    filetype_group.add_argument(
        "--type",
        nargs = 1,
        metavar = ("File Type"),
        choices = ['.mp3', ".mp4"],
        default = '.mp3',
        help = "Select the desired file type. Currently supported: .mp3 (audio-only), .mp4 (video)"
    )
    filetype_group.add_argument(
        "--destination",
        type = str,
        nargs = 1,
        metavar = ("File Destination"),
        widget = "DirChooser",
        default = default_dir,
        help = "Select a directory to store your files in. Your desktop is the default."
    )
    importtype_group.add_argument(
        "--file",
        type = str,
        nargs = 1,
        metavar = ("CSV"),
        widget = "FileChooser",
        help = "Use a .csv file listing the songs to be downloaded."
    )
    singleimport_group.add_argument(
        "--url",
        type = str,
        nargs = 1,
        metavar = ("URL"),
        help = "Imports a single song from a single URL. This needs both the URL and the desired song title.",
    )
    singleimport_group.add_argument(
        "--title",
        type = str,
        nargs = '+',
        metavar = "Title",
        help = "Give your downloaded file a title."
    )
    importtype_group.add_argument(
        "--difference",
        type = str,
        nargs = 2,
        metavar = ("oldfile newfile"),
        widget = "MultiFileChooser",
        help = "Compares two songlists and only obtains new songs on the list."
    )

    args = parser.parse_args()
    if args.file:
        importList(args.file, args.type[0], args.destination[0])
    elif args.difference:
        diffLists(args.difference[0], args.difference[1], args.type[0], args.destination[0]) 
    elif args.url and args.title:
        singleSong(args.url[0], args.title, args.type[0], args.destination[0])

def importList(arg_file, arg_type, arg_dest):
    inputfile = arg_file[0]
    csvname = os.path.splitext(os.path.basename(inputfile))[0]
    with open(inputfile, newline='') as csv_file:
        data = csv.DictReader(csv_file)
        for row in data:
            print(row['Title'], row["URL"])
            url = row["URL"]
            destination = os.path.join(arg_dest, csvname, row["Category"]) 
            filename = row["Title"] + arg_type
            print(filename)
            downloader(url, filename, arg_type, destination)

def diffLists(arg_file1, arg_file2, arg_type, arg_dest):
    with open(arg_file1) as f1, open(arg_file2) as f2:
        fileone = f1.readlines()
        filetwo = f2.readlines()
        with open('input/difflist.csv', 'w') as outfile:
            for line in filetwo:
                if line not in fileone:
                    outfile.write(line)
    with open("input/difflist.csv", newline='') as csv_file:
        csvname = os.path.splitext(os.path.basename(arg_file2))[0]
        data = csv.DictReader(csv_file)
        for row in data:
            print(row['Title'], row["URL"])
            url = row["URL"]
            destination = os.path.join(arg_dest, csvname, row["Category"])
            filename = row["Title"] + arg_type
            print(filename)
            downloader(url, filename, arg_type, destination)

def singleSong(arg_url, arg_title, arg_type, arg_dest):
    title = ' '.join(arg_title)
    filename = title + arg_type
    downloader(arg_url, filename, arg_type, arg_dest)
    return

def downloader(url, filename, arg_type, arg_dest):
    print("Downloading "+ filename + " to " + arg_dest)
    try: 
        if arg_type == ".mp3":
            output = subprocess.run(["yt-dlp", "-P " + arg_dest, "-o " + filename , str(url), "-x", "--audio-format", "mp3"], capture_output=True, text=True, check=False)
            print(output.stdout)
            print(output.stderr)
        elif arg_type == ".mp4":
            output = subprocess.run(["yt-dlp", "-P " + arg_dest, "-o " + filename , str(url), "-S", "vcodec:h264, ext:mp4:mp3", "--recode-video", "mp4" ], capture_output=True, text=True, check=False)
            print(output.stdout)
            print(output.stderr)
        
    except subprocess.CalledProcessError as e:
        print(f"Failed with return code {e.returncode}")
        
    print("Waiting...")
    time.sleep(15)
    return
    
if __name__ == '__main__':
    main()

    #downloader(video, videotitle,  foldername)