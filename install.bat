@echo off
@echo Check pyBindDesktop requirements
pip show image > .check.cache
pip show pywin32 >> .check.cache

set foundImage=FALSE
set foundPywin32=FALSE
for /f "tokens=2 delims=: " %%i in (.check.cache) do (
  if %%i==image set foundImage=TRUE
  if %%i==pywin32 set foundPywin32=TRUE
)

if not %foundPywin32%==TRUE (
  echo Please download pywin32 that fits your python version
  python -V
  explorer "https://sourceforge.net/projects/pywin32/files/pywin32/Build 221/"
) else (
  echo found pywin32
)
if not %foundImage%==TRUE (
  pip install Image
) else (
  echo found image
  del /Q /F .check.cache
)

REM a directory to store downloaded pictures
if not exist wallpaper mkdir wallpaper

@echo Check done!
