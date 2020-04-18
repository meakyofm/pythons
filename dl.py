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
            url_pix = url + str(i+1) + ".jpg"
            print(folderpath)
            urllib.request.urlretrieve(url_pix, folderpath + str(i) + ".jpg")
        except urllib.error.URLError as e:
        	break

if __name__ == "__main__":
    print("please enter folder name")
    foldername=input("--->")
    folderpath = "./" + foldername + "/"
    os.makedirs(folderpath, exist_ok=True)
    
    print("pleae enter URL")
    # url=input("--->")
    url = "https://static8.hentai-image.com/upload/20191021/594/608222/"
    
    print("please enter number of pages")
    pages=int(input("--->"))
    download(folderpath, url, pages)