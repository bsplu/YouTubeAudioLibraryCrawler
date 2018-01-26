#!/usr/bin/env python3


import requests
import LoadCookiesTest as lct
import CreateHeaders as ch
import Scraping


cookies = lct.GetLocalCookies().GetCookies()

sa = Scraping.Scraping(SegLen=1000,Cookies=cookies,show=1)
sa.ScrapingAll()

Music = sa.GetMusicList()

f = open("testlist.txt","w")

for jc in Music:
    f.write(jc['title'])
    f.write("\n")
f.write("-----------")

for jc in Music[0].keys():
    s = jc + "  " + Music[0][jc]
    f.write(s)
