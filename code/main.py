#!/usr/bin/env python3


######################################################
#       test



import requests
import LoadCookiesTest as lct
import CreateHeaders as ch
import Scraping
import RuleSelection


cookies = lct.GetLocalCookies().GetCookies()

sa = Scraping.Scraping(SegLen=1000,Cookies=cookies,show=1)
sa.ScrapingAll()

Music = sa.GetMusicList()

f = open("testlist.txt","w")

for jc in Music:
    f.write(jc['title'])
    f.write(' '.join(jc['instruments']))
    f.write("\n")
f.write("-----------")





Selc = RuleSelection.RuleSelection(Music)
Rule = {   'genre': 'Ambient'  ,   "mood":"Dark" , 'instruments':'Trumpet'    }



New = Selc.GetSelection(Rule)



for jc in New:
    print(jc['title'])
