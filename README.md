# ytdl-gui
ytdl-gui provides an easy way to download audio and video media from YouTube and other sources by wrapping a [Gooey](https://github.com/chriskiehl/Gooey.git) UI around the [yt-dl](https://github.com/yt-dlp/yt-dlp) downloading package to provide both single URL and bulk URL downloading.
## First-Time Setup (Windows)
1.  Verify Python install  
    This application runs on Python, and has an easy method for updating the stuff we'll need.
    - Open Command Prompt and type:  
    ```python -V```  
    - If no Python installation is found, or Python version < 3.0, visit [Download Python](https://www.python.org/downloads/) and click Download. When prompted in the installer, select "Add Python to PATH"  
2.  (Optional-ish) Install [ffmpeg](https://www.ffmpeg.org/)  
    FFMPEG provides extra utilities for working with audio files. This application can work without it, but works best when it can see it.  
    - [https://github.com/BtbN/FFmpeg-Builds/releases](https://github.com/BtbN/FFmpeg-Builds/releases)  
    - Right-click the downloaded file and click "Extract All...".  
    Download the Asset titled: "ffmpeg-master-latest-win64-gpl-shared.zip"  
    Unzip it, but take a note of where it's located. We'll want to reference it when we run the application.  
3.  Install [Git for Windows](https://gitforwindows.org/)  
    - Feel free to follow the guide at [https://phoenixnap.com/kb/how-to-install-git-windows](https://phoenixnap.com/kb/how-to-install-git-windows) for the installer dialog options; the only important installer question is "Adjusting your PATH environment". You will likely want to select "Git from the command line and also from 3rd-party software." so that you don't have to add it to PATH yourself later.   
4.  Download the ytdl-gui application scripts by clicking the green "<> Code" button near the top of this page and clicking "Download ZIP".   
    Right-click the downloaded file and click "Extract All..." . You may leave it in the Downloads folder or move the 'ytdl-gui-main' folder wherever is convenient, do note where you move it if you do.
5.  Open a new Command Prompt window and use the 'cd' command to change directories to the folder you have the 'ytdl-gui-main' folder stored in. If you kept it in your Downloads folder for example, use the command:  
    ```cd Downloads\ytdl-gui-main\ytdl-gui-main```  
6.  Create venv (virtual environment)  
    ``` python -m venv ytdl-venv```  
    And activate it  
    ``` source ytdl-venv/bin/activate```  
7.  Install Python requirements  
    ``` pip install -r requirements.txt ```  
8. Run it with:  
    ```python ingestDownloader.py```  
9. (Optional) Setting up the YTDownloader easy-click icon  
    - In the 'ytdl-gui-main' folder, right-click YTDownloader.bat and select 'Edit'.   
    - In Notepad, edit the folder path lines as described in the comments. If you need to look up what the file paths are to the items you have downloaded, you can open a File Browser window, navigate to the folder, and click into the Address bar at the top to view and copy the full file address.    
    - Once you have edited the icon, you can simply click the icon and it will automagically run the application! You may copy this to your desktop or wherever else you prefer, since it is using the full file paths and won't mind being used outside the ytdl-gui-main folder.   


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

