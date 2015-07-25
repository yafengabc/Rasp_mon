import urllib.parse
import urllib.request
import os
import time

file="/sys/devices/virtual/thermal/thermal_zone0/temp"
url="http://127.0.0.1:8000/post"
dat={"time":"","temp":100}
if os.path.exists(file):
    while True:
        fi=open("/sys/devices/virtual/thermal/thermal_zone0/temp")
        tem=fi.read()
        dat["time"]=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
        dat["temp"]=float(tem)/1000
        print(dat)
        try:
            res=urllib.request.urlopen(url,str(dat).encode())
            print(res.read().decode())
            time.sleep(5)
        except:
            print("Post fail")
            time.sleep(5)
            pass
