#!/usr/bin/env python3

# -*- coding: utf-8 -*-
#══════════════════════════════════════════════════════════════════════════════════════════════════════════════════
# Class:   LoadCookiesTest
#──────────────────────────
# Author:  Hengyue Li
#──────────────────────────
# Version: 2018/01/25
#──────────────────────────
# discription:
#          Load cookies from a local browser. Use browser_cookie3
#          Details of module can be found in:
#                  https://github.com/borisbabic/browser_cookie3
#──────────────────────────
# Imported :
import browser_cookie3
#──────────────────────────
#
# Interface:
#
#        ----------------------
#
#        [ini]
#
#        [fun] GetCookies():
#              return the loaded cookies
#
#══════════════════════════════════════════════════════════════════════════════════════════════════════════════════

#$$$$$$$$$$$$$$$$$$$$$$$$$$$

#   "Chrome" / "Firefox"
SelectBrowser = "Firefox"

#$$$$$$$$$$$$$$$$$$$$$$$$$$$




class GetLocalCookies(object):
    def __init__(self):
        self.browser = SelectBrowser#browser

    def GetCookies(self):
        #-------------------------------------
        Browserlist = {
           "chrome" : browser_cookie3.chrome   ,
           "firefox": browser_cookie3.firefox  ,
        }
        #-------------------------------------
        if self.browser.lower() not in list(Browserlist.keys()):
            print("ERROR: Unknow browser type:",self.browser)
            exit()
        fun = Browserlist[self.browser.lower()]
        return fun()



if __name__ == "__main__":
    f = GetLocalCookies()
    f = f.GetCookies()
