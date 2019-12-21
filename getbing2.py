# coding=utf-8
import os
import re
import time
import win32api
import win32con
import win32gui

import requests
from PIL import Image
from lxml.html import fromstring

_MAIN_PAGES = [
  "https://cn.bing.com/",
  "https://www2.bing.com/",
  "https://www4.bing.com/",
  "http://www.bing.com/",
]


def set_wallpaper(imagepath):
  k = win32api.RegOpenKeyEx(
    win32con.HKEY_CURRENT_USER,
    "Control Panel\\Desktop",
    0,
    win32con.KEY_SET_VALUE)
  win32api.RegSetValueEx(
    k, "WallpaperStyle", 0, win32con.REG_SZ, "2")  # 2拉伸适应桌面,0桌面居中
  win32api.RegSetValueEx(
    k, "TileWallpaper", 0, win32con.REG_SZ, "0")
  win32gui.SystemParametersInfo(
    win32con.SPI_SETDESKWALLPAPER, imagepath, 3)


def main():
  sess = requests.session()
  for page in _MAIN_PAGES:
    try:
      bing = sess.get(page, timeout=5)
      if bing.status_code == 200:
        html = fromstring(bing.content.decode())
        break
      else:
        print("HTTP error: {}".format(bing.status_code))
        exit(1)
    except:
      print(" [!] {} connection error!".format(page))
      continue
  wallpaper_url = html.find(".//link[@id]").get('href')
  if not re.findall("\\d+x\\d+\.jpg", wallpaper_url):
    wallpaper_url = html.find(".//link[@href]").get('href')
  print(page + wallpaper_url)
  wallpaper = sess.get(page + wallpaper_url, timeout=10)
  date = time.strftime('%Y-%m-%d', time.localtime())
  pat = re.compile("\w*?\.jpg")
  name = re.findall(pat, wallpaper_url)[0]
  temp_jpeg = "wallpaper/[{}]{}.jpg".format(date, name)
  with open(temp_jpeg, 'wb') as fp:
    fp.write(wallpaper.content)
  Image.open(temp_jpeg).save('mywallpaper.bmp')
  set_wallpaper(os.getcwd() + '\\mywallpaper.bmp')


if __name__ == '__main__':
  main()
