#!/usr/bin/env python
#-*- coding:utf-8 -*-

import urllib.request
import sys
import os

def download():
    path = "./pic/"
    # os.mkdir(path)

    url = "https://static8.hentai-image.com/upload/20191021/594/608222/"
    opener = urllib.request.build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/5.0')]
    urllib.request.install_opener(opener)

    for i in range(100):
        try:
            # url_all = url + str(i+1).zfill(3) + ".jpg"
            url_all = url + str(i+1) + ".jpg"
            print (url_all)
            urllib.request.urlretrieve(url_all, path + str(i) + ".jpg")
            # urllib.request.urlretrieve(url_all, path + str(i).zfill(3) + ".jpg")
        except urllib.error.URLError as e:
        	print (e)
        	break

if __name__ == "__main__":
    download()