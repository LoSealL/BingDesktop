@echo off
d:
cd d:\Works\PythonTEST\Bing\
python getbing.py 0 0
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