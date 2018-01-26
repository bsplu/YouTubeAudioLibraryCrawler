#/usr/bin/env python3

# -*- coding: utf-8 -*-
#           download music list on : https://www.youtube.com/audiolibrary/music
#
#

import Usage
import LoadCookiesTest as lct
import CreateHeaders as ch
import Scraping
import RuleSelection




#-----------------------------------------------------
#  get cookies
cookies = lct.GetLocalCookies().GetCookies()
#-----------------------------------------------------
#  scraping list
sa = Scraping.Scraping(SegLen=1000,Cookies=cookies )
sa.ScrapingAll()
Music = sa.GetMusicList()
#-----------------------------------------------------
# get xml
xml = { jc['vid']:jc  for jc in Music}
xml = Usage.dicttoxml.dicttoxml(xml)
#-----------------------------------------------------
# write file
dom = Usage.parseString(xml)
st = dom.toprettyxml()
file_handle = open("MusicList.xml","w")
file_handle.write(st)
file_handle.close()

# k = Music[0].keys()
# for jc in k:
#     print(jc,"  ",Music[0][jc],"\n")






#
#
# f = open("testlist.txt","w")
#
# for jc in Music:
#     f.write(jc['title'])
#     f.write(' '.join(jc['instruments']))
#     f.write("\n")
# f.write("-----------")
#
# Selc = RuleSelection.RuleSelection(Music)
# Rule = {   'genre': 'Ambient'  ,   "mood":"Dark" , 'instruments':'Trumpet'    }
#
# New = Selc.GetSelection(Rule)
#
# for jc in New:
#     print(jc['title'])
