import os
import sys
import csv
import subprocess
import time
import argparse
from gooey import Gooey, GooeyParser


# Usage:
# Currently, just hop into the venv containing yt-dlp and set your PATH to include ffmpeg location

# C:\Users\Loren\Documents\Development\yt-dlpDownloading\venv\Scripts\activate
# set PATH=%PATH%;C:\Users\Loren\Documents\Development\ffmpeg\ffmpeg-master-latest-win64-gpl\ffmpeg-master-latest-win64-gpl\bin
# ytdlp_dir = r"C:\Users\Loren\Documents\Development\yt-dlpDownloading"
# ffmpeg_dir = r"C:\Users\Loren\Documents\Development\ffmpeg\ffmpeg-master-latest-win64-gpl\ffmpeg-master-latest-win64-gpl\bin"

target_dir = r"results"

#@Gooey
def main():
    parser = argparse.ArgumentParser( # Switch to argparse.ArgumentParser() when not using Gooey
        description="Music Grabbin' Machine!"
    )
    parser.add_argument(
        "-f",
        "--file",
        type = str,
        #widget = "FileChooser",
        help = "Use a .csv file listing the songs to be downloaded."
    )
    parser.add_argument(
        "-u",
        "--url",
        type = str,
        nargs = 2,
        #metavar = ("URL", "Songname.mp3"),
        help = "Imports a single song from a single URL. Needs both the URL and the desired song title.",
    )
    parser.add_argument(
        "-d",
        "--difference",
        type = str,
        nargs = 2,
        #metavar = ("oldfile", "newfile"),
        #widget = "MultiFileChooser",
        help = "Compares two songlists and only obtains new songs on the list."
    )

    args = parser.parse_args()
    if args.file:
        importList(args.file)
    elif args.difference:
        diffLists(args.difference[0], args.difference[1]) 
    elif args.url:
        singleSong(args.url[0], args.url[1])

def importList(arg_file):
    inputfile = arg_file
    csvname = os.path.splitext(os.path.basename(inputfile))[0]
    with open(inputfile, newline='') as csv_file:
        data = csv.DictReader(csv_file)
        for row in data:
            print(row['Title'], row["URL"])
            url = row["URL"]
            filename = os.path.join(target_dir, csvname, row["Category"], row["Title"] + ".mp3")
            print(filename)
            downloader(url, filename)

def diffLists(arg_file1, arg_file2):
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
            filename = os.path.join(target_dir, csvname, row["Category"], row["Title"] + ".mp3")
            print(filename)
            #downloader(url, filename)

def singleSong(arg_url, arg_title):
    return

def downloader(url, filename):
    print("Downloading "+ filename)
    try: 
        output = subprocess.run(["yt-dlp", "-o " + str(filename), str(url), "-x", "--audio-format", "mp3"], capture_output=True, text=True, check=False)
        print(output.stdout)
        print(output.stderr)
        
    except subprocess.CalledProcessError as e:
        print(f"Failed with return code {e.returncode}")
        
    print("Napping... Dreaming...")
    time.sleep(15)
    return
    
if __name__ == '__main__':
    main()

    #downloader(video, videotitle,  foldername)