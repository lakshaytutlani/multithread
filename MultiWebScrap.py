# -*- coding: utf-8 -*-
import urllib2
from bs4 import BeautifulSoup
import threading

urls = [
    "https://www.google.com",
    "https://www.youtube.com",
    "https://www.wikipedia.org",
    "https://www.reddit.com",
    "https://www.httpbin.org"
]

def scrap_page(url):
    page = urllib2.urlopen(url)
    soup = BeautifulSoup(page, 'html.parser')
    with open("Output/"+str(url.split("//")[-1])+".txt","wb") as file:
        file.write(str(soup))
        
        
if __name__ == "__main__":
    threads = []
    for i in urls:
        p1 = threading.Thread(target=scrap_page,args=(i,))
        p1.start()
        threads.append(p1)
        
    for proc in threads:
        proc.join()
        
    # for i in urls:
        # scrap_page(i)
    