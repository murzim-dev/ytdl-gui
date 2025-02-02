:: Edit the PATH below to where you have ffmpeg installed:
set PATH=%PATH%;C:\Users\Loren\Documents\Development\ffmpeg\ffmpeg-master-latest-win64-gpl\ffmpeg-master-latest-win64-gpl\bin
:: The first filepath (the one before the &) should be edited to the location where you installed the venv. We want to keep the \Scripts\activate at the end of the path. 
:: Mine is located at C:\Users\Loren\Documents\Development\yt-dlpDownloading\ytdl-venv
:: So mine will look like C:\Users\Loren\Documents\Development\yt-dlpDownloading\ytdl-venv\Scripts\activate 
:: Next, edit the filepath after the '& python' to where the 'ytdl-gui-main' folder is located, adding \ingestDownloader.py at the end.
:: Mine is at C:\Users\Loren\Documents\Development\ytdl-gui\, which becomes python C:\Users\Loren\Documents\Development\ytdl-gui\ingestDownloader.py
:: This will run the Python script
C:\Users\Loren\Documents\Development\yt-dlpDownloading\ytdl-venv\Scripts\activate & python C:\Users\Loren\Documents\Development\ytdl-gui\ingestDownloader.py