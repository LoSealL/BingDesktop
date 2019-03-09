@echo off

REM REM make a wallpaper to store past images
REM IF NOT EXIST wallpaper (
    REM mkdir wallpaper
REM )
REM REM call python script (python3 required)
REM python getbing.py child-prc.intel.com 913
REM REM python getbing.py
REM REM we use converted bmp file as wallpaper, and store downloaded jpg(s).
REM IF EXIST *.jpg (
    REM MOVE /Y *.jpg wallpaper
REM )
REM REM fail to download image from bing.com
REM IF NOT EXIST mywallpaper.bmp (
    REM @echo Can't get bing.com
    REM pause
    REM IF EXIST err.html (
        REM DEL err.html /Q /F
    REM )
REM )

python getbing2.py