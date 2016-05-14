#coding=utf-8
import urllib.request as urlget
import re
import time
from PIL import Image
import os,sys
import win32gui,win32api,win32con


class bingPaper():
    def __init__(self,homepage,proxy = False):
        self.homepage = homepage
        if len(sys.argv)==1:
            print("Useage: %s [IP Address] [Port]\n" %sys.argv[0])
        self.server = sys.argv[1]
        self.port = sys.argv[2]
        if proxy:
            print("MPW server IP is: %s" %sys.argv[1])
            proxyHandle = urlget.ProxyHandler({"http":'http://mpw:mpw53101@'+self.server+':'+self.port})
            passwd = urlget.HTTPPasswordMgrWithDefaultRealm()
            proxyPassHandle = urlget.ProxyBasicAuthHandler(passwd)
            proxyPassHandle.add_password(None,self.server,"loseall","169253moevpn")
            opener = urlget.build_opener(proxyHandle,proxyPassHandle,urlget.HTTPHandler)
            urlget.install_opener(opener)
        page = urlget.urlopen(self.homepage)
        self.html = page.read()
    def getDate(self):
        date = time.strftime('%Y-%m-%d',time.localtime())
        return date
    def getImg(self):
        # reg = "(?<=g_img\=\{url\:.')+http\://s\.cn\.bing\.net/\w+/\w+/\w+/\w+-\w+1920x1080\.jpg"
        reg = "(?<=g_img\=\{url\:..)+http\:../../s\.cn\.bing\.net../\w+../\w+../\w+../\w+-\w+1920x1080.jpg"
        imgre = re.compile(reg)
        imglist = re.findall(imgre,str(self.html))
        if not imglist:
            fd = open('err.html','w')
            fd.writelines(str(self.html))
            fd.close()
            return None
        for imgurl in imglist:
            imgurl = imgurl.replace('\\','')
            urlget.urlretrieve(imgurl,'[%s]%s' % (self.getDate(),imgurl[-20:]))
        return '['+self.getDate()+']'+imgurl[-20:]

class setPaper():
    def __init__(self,imagepath):
        self.imagepath = imagepath
        self.StoreFolder = os.getcwd()
    def setWallpaperFromBMP(self,imagepath):
        k = win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER,"Control Panel\\Desktop",0,win32con.KEY_SET_VALUE)
        win32api.RegSetValueEx(k, "WallpaperStyle", 0, win32con.REG_SZ, "2") #2拉伸适应桌面,0桌面居中
        win32api.RegSetValueEx(k, "TileWallpaper", 0, win32con.REG_SZ, "0")
        win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER,imagepath, 1+2)
    def setWallPaper(self):
        """
        Given a path to an image, convert it to bmp and set it as wallpaper
        """
        bmpImage = Image.open(self.imagepath)
        newPath = self.StoreFolder + '\\mywallpaper.bmp'
        bmpImage.save(newPath, "BMP")
        self.setWallpaperFromBMP(newPath)
        
myhtml = bingPaper("http://cn.bing.com",False)
fName = myhtml.getImg()
if not fName:
    exit(0)
path = os.getcwd()
print(fName)
wallpaper = setPaper(path+'\\'+fName)
wallpaper.setWallPaper()