#!/usr/bin/env python
#-*- coding:utf-8 -*-

import urllib.request
import sys
import os

def download(folderpath, url, pages):
    opener = urllib.request.build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/5.0')]
    urllib.request.install_opener(opener)

    for i in range(pages):
        try:
            # url_all = url + str(i+1).zfill(3) + ".jpg"
            url_pix = url + str(i+1).zfill(3) + ".jpg"
            urllib.request.urlretrieve(url_pix, folderpath + str(i) + ".jpg")
        except urllib.error.URLError as e:
        	break

if __name__ == "__main__":
    print("pleae enter URL")
    url=input("--->")

    print("please enter folder name")
    foldername=input("--->")
    folderpath = "./" + foldername + "/"
    os.makedirs(folderpath, exist_ok=True)    
    
    # print("please enter number of pages")
    # pages=int(input("--->"))
    pages=999
    download(folderpath, url, pages)
