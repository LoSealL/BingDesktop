@echo off
@echo Check pyBindDesktop requirements
pip install pywin32 Image pillow requests lxml
REM a directory to store downloaded pictures
if not exist wallpaper mkdir wallpaper

@echo Check done!
