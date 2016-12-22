@echo off
d:
cd d:\Works\BingDesktop
python getbing.py child-prc.intel.com 913
if EXIST *.jpg (
    move /Y *.jpg wallpaper
)
if EXIST mywallpaper.bmp (
    if EXIST err.html (
        del err.html /Q /F
    )
) else (
    @echo Can't get bing.com
    pause
)
REM pause