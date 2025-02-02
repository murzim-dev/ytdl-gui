# ytdl-gui
ytdl-gui provides an easy way to download audio and video media from YouTube and other sources by wrapping a [Gooey](https://github.com/chriskiehl/Gooey.git) UI around the [yt-dl](https://github.com/yt-dlp/yt-dlp) downloading package to provide both single URL and bulk URL downloading.

## First-Time Setup (MacOS)
1.	Install Homebrew 

       ``` /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"```

2.	Install [ffmpeg](https://ffmpeg.org/)

     ``` brew install ffmpeg ```
3.	Install Python (if not yet installed by this point)

    ``` brew install python```
4.	Create venv

    ``` python3 -m venv ytdl-venv```

    ``` source ytdl-venv/bin/activate```
5.	Clone repo

    ``` git clone https://github.com/murzim-dev/ytdl-gui.git ```
6.	Install Python requirements

    ``` pip install -r ytdl-gui-main/requirements.txt ```
## Usage
Click on the YoutubeDL app on the desktop to launch the application. You can grab your videos either singly or in bulk:
1. Single-URL Download
    - Simply fill in the URL in the URL box and the file title (just the name, no .mp3 or .mp4 extension needed!) in the Title box, then click `Start`
2. Bulk Download
    - Select a .csv file containing your list of videos with the same header structure as the file at [https://github.com/murzim-dev/ytdl-gui/blob/main/samples/songtest.csv](https://github.com/murzim-dev/ytdl-gui/blob/main/samples/songtest.csv) and click `Start`
3. Comparative Bulk Download
    - If you have several .csv files and only want songs that are 'new' to the lists, you can select multiple .csv files in the `oldfile newfile` section. This feature is useful if you add songs to a list over time; you can compare the old list to the new list and donwload the new additions. 

