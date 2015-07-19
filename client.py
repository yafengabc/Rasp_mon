import urllib.parse
import urllib.request
import os

file="/sys/devices/virtual/thermal/thermal_zone0/temp"
url="http://127.0.0.1:8000/post"
dat={"temp":100}
if os.path.exists(file):
    fi=open("/sys/devices/virtual/thermal/thermal_zone0/temp")
    tem=fi.read()
    dat["temp"]=float(tem)/100
    urllib.request.urlopen(url,str(dat).encode())
