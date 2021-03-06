#/usr/bin/env python3

# -*- coding: utf-8 -*-
# ══════════════════════════════════════════════════════════════════════════════════════════════════════════════════
# Class:   Scraping
# ──────────────────────────
# Author:  Hengyue Li
# ──────────────────────────
# Version: 2018/01/26
# ──────────────────────────
# discription:
#          Scraping all the list
# ──────────────────────────
# Imported  :
import Usage
import CreateHeaders as ch
# ──────────────────────────
# Standards :
#
#
# Interface :
#
#        ----------------------
#
#        [ini]  SegLen_int , Cookies_CookiesObject  , show_int=None
#
#        [sub]  ScrapingAll()
#
#        [fun]  GetMusicList()
#                return pointer directly.
#
#
#
# ══════════════════════════════════════════════════════════════════════════════════════════════════════════════════


class Scraping():
    def __init__(self,SegLen,Cookies,show=None):
        self.SegLen  = SegLen
        self.Cookies = Cookies
        self.Music   = []
        if show == None :
            self.show = 0
        else:
            self.show = show

    def GetAudioSwapUrl(self,mr,si,qid):
        return 'https://www.youtube.com/audioswap_ajax?action_get_tracks=1&ads=false&dl=true&s=music&mr='+str(mr)+'&si='+str(si)+'&qid='+str(qid)+'&sh=true'

    def GetHeaders(self):
        headers = ch.CreateHeaders()
        headers.AppendLanguage('en')
        return headers.GetHeaders()


    # return has_more = True/False
    def AppendSegDict(self,mr,si,qid):
        url      = self.GetAudioSwapUrl(mr,si,qid)
        tempPage = Usage.requests.get( url = url , cookies = self.Cookies ,headers = self.GetHeaders() )
        soup     = Usage.BeautifulSoup(tempPage.content, 'html.parser')
        d        = Usage.json.loads(soup.prettify())
        has_more = d['has_more']
        tracks   = d['tracks']
        conto    = d['continuation_token'] #None
        for jc in tracks:
            self.Music.append(jc)
        return has_more

    def ScrapingAll(self):
        mr  = self.SegLen
        si  = 0
        qid = 0
        while True:
            if self.show>0:
                print("Recently qid:",qid , "si:",si  , "mr:",mr)
            HasMore = self.AppendSegDict(mr,si,qid)
            if not HasMore:
                break
            else:
                si  = si + mr
                qid = qid + 1

    def GetMusicList(self):
        return  self.Music
