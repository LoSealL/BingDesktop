#coding=utf-8
import re, time, os, sys
import win32gui, win32api, win32con
import urllib.request as urlget
from PIL import Image

class bingPaper():
  '''
  homepage: must be "http://cn.bing.com"
  I havn't tested on other bing sites.
  '''
  def __init__(self, homepage):
    print("Useage: %s" %sys.argv[0])
    print("Proxy Useage: %s [IP Address] [Port]" %sys.argv[0])
    self.homepage = homepage
    if len(sys.argv) == 3:
      # using proxy server
      server = sys.argv[1]
      port = sys.argv[2]
      # using http proxy, you can modify this to meet your requirement
      print("Proxy server IP is: {}:{}".format(server, port))
      proxyProtocol = "http"
      proxyHandle = urlget.ProxyHandler({proxyProtocol: "{}://{}:{}".format(proxyProtocol, server, port)})
      passwd = urlget.HTTPPasswordMgrWithDefaultRealm()
      proxyPassHandle = urlget.ProxyBasicAuthHandler(passwd)
      # if your proxy has password, add your password here
      # proxyPassHandle.add_password(None, server, "user", "12345678")
      opener = urlget.build_opener(proxyHandle,proxyPassHandle,urlget.HTTPHandler)
      urlget.install_opener(opener)
    page = urlget.urlopen(self.homepage)
    self.html = page.read()
    
  '''
  get the background image url from the page
  '''
  def getImg(self):
    # this reg was deprecated since 2017.1
    reg1 = "(?<=g_img\=\{url\:..)+http\://s\.cn\.bing\.net/\w+/\w+/\w+/\w+-\w+1920x1080.jpg"
    reg2 = "(?<=g_img\=\{url\:..)+/\w+/\w+/\w+/\w+-\w+1920x1080.jpg"
    imgre2 = re.compile(reg2)
    imglist = re.findall(imgre2,str(self.html))
    if not imglist:
      fd = open('err.html','w')
      fd.writelines(str(self.html))
      fd.close()
      return None
    date = time.strftime('%Y-%m-%d', time.localtime())
    for imgurl in imglist:
      imgurl = "http://cn.bing.com" + imgurl
      print(imgurl)
      urlget.urlretrieve(imgurl, "[{}]{}".format(date, imgurl[-20:]))
    return "[{}]{}".format(date, imgurl[-20:])
  
  """
  Given a path to an image, convert it to bmp and set it as wallpaper
  """
  def setWallPaper(self):
    file = self.getImg()
    if not file:
      return
    print(file)
    Image.open(file).save('mywallpaper.bmp', "BMP")
    self.setWallpaperFromBMP(os.getcwd() + '\\mywallpaper.bmp')
  
  '''
  Using pywin32 to set windows desktop wallpaper
  imagepath should be absolute path
  '''
  def setWallpaperFromBMP(self, imagepath):
    k = win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER, "Control Panel\\Desktop", 0, win32con.KEY_SET_VALUE)
    win32api.RegSetValueEx(k, "WallpaperStyle", 0, win32con.REG_SZ, "2")  #2拉伸适应桌面,0桌面居中
    win32api.RegSetValueEx(k, "TileWallpaper", 0, win32con.REG_SZ, "0")
    win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER, imagepath, 3)

# app starts
bingPaper("http://cn.bing.com").setWallPaper()
