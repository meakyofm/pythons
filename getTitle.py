#!/usr/bin/env python
#-*- coding:utf-8 -*-

def getTitle(url):
    from bs4 import BeautifulSoup
    import urllib.request
    opener = urllib.request.build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/5.0')]
    urllib.request.install_opener(opener)
    html = urllib.request.urlopen(url)
    soup = BeautifulSoup(html, "html.parser")
    return soup.title.string

# if __name__ == "__main__":
#     print("pleae enter URL")
#     url=input("--->")
#     print(getTitle(url))