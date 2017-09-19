@echo off
REM make a wallpaper to store past images
IF NOT EXIST wallpaper (
    mkdir wallpaper
)
REM call python script (python3 required)
python getbing.py
REM we use converted bmp file as wallpaper, and store downloaded jpg(s).
IF EXIST *.jpg (
    MOVE /Y *.jpg wallpaper
)
REM fail to download image from bing.com
IF NOT EXIST mywallpaper.bmp (
    @echo Can't get bing.com
    pause
    IF EXIST err.html (
        DEL err.html /Q /F
    )
)
