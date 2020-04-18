#!/usr/bin/env python
#-*- coding:utf-8 -*-

import urllib.request
import sys
import os
from getTitle import getTitle

def download(folderpath, url, pages):
    opener = urllib.request.build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/5.0')]
    urllib.request.install_opener(opener)

    for i in range(pages):
        try:
            # url_all = url + str(i+1).zfill(3) + ".jpg"
            url_pix = url + str(i+1).zfill(2) + ".jpg"
            urllib.request.urlretrieve(url_pix, folderpath + str(i) + ".jpg")
        except urllib.error.URLError as e:
            break

if __name__ == "__main__":
    print("pleae enter pix URL")
    url=input("--->")

    print("please enter TOP page url")
    toppage=input("--->")
    foldername=getTitle(toppage)
    folderpath = "./" + foldername + "/"
    os.makedirs(folderpath, exist_ok=True)    
    
    # print("please enter number of pages")
    # pages=int(input("--->"))
    pages=99
    download(folderpath, url, pages)
