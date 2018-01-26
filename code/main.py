#/usr/bin/env python3

# -*- coding: utf-8 -*-
# ══════════════════════════════════════════════════════════════════════════════════════════════════════════════════
# Class:   main
# ──────────────────────────
# Author:  Hengyue Li
# ──────────────────────────
# Version: 2018/01/26
# ──────────────────────────
# discription:
#          Scraping music at : https://www.youtube.com/audiolibrary/music
# ──────────────────────────
# Imported  :
import Usage
import LoadCookiesTest as lct
import CreateHeaders as ch
import Scraping
import RuleSelection
# ──────────────────────────
# Standards :
#
#
# Interface :
#
#        ----------------------
#
#        [ini] XmlPath_str
#              input a file path to saving music.xml
#
#        [sub] ReNewMusicList()
#
# ══════════════════════════════════════════════════════════════════════════════════════════════════════════════════



class main():
    def __init__(self,XmlPath_str):
        self.xmlpath = XmlPath_str

    def ReNewMusicList(self):
        #-----------------------------------------------------
        #  get cookies
        cookies = lct.GetLocalCookies().GetCookies()
        #-----------------------------------------------------
        #  scraping list
        sa = Scraping.Scraping( SegLen = 1000 , Cookies = cookies )
        sa.ScrapingAll()
        Music = sa.GetMusicList()
        #-----------------------------------------------------
        # get xml
        xml = { ("MusicId_"+str(jc['vid'])):jc  for jc in Music}

        keys = xml.keys()
        for jc in keys:
            print(jc)


        xml = Usage.dicttoxml.dicttoxml(xml)
        #-----------------------------------------------------
        # write file
        dom = Usage.parseString(xml)
        st = dom.toprettyxml()
        file_handle = open(self.xmlpath,"w")
        file_handle.write(st)
        file_handle.close()







if __name__ == "__main__":
    f = main("MusicList.xml")
    f.ReNewMusicList()









# -*- coding: utf-8 -*-
#           download music list on : https://www.youtube.com/audiolibrary/music
#
#


################################################################################
#    one first install all the lib that marked in Usage.py














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
