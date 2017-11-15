# -*- coding: UTF-8 -*-
import os,datetime,shutil,time
#"/volume1/photo/test/1900-01-01 待整理"
srcpath = os.path.join("/volume1/photo/","test","1900-01-01 待整理")
#srcpath=os.path.join("/Users/test/Documents/test")
dirname,filen = os.path.split(srcpath)
print(dirname,filen)
for it in os.listdir(srcpath):
    srcfile=os.path.join(srcpath,it)
    timestamp = os.path.getctime(srcfile)
    date = (datetime.datetime.fromtimestamp(timestamp)).date()
    despath=os.path.join(dirname,str(date))
    if(os.path.exists(despath)==False):
        os.mkdir(despath)
    shutil.move(srcfile,despath)



