@echo off
d:
cd d:\Bing\
python getbing.py child-prc.intel.com 913
if EXIST *.jpg (
    move /Y *.jpg wallpaper
)
if EXIST mywallpaper.bmp (
    del mywallpaper.bmp
    if EXIST err.html (
        del err.html /Q /F
    )
) else (
    @echo Can't get bing.com
    pause
)
REM pause