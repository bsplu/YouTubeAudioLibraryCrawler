#/usr/bin/env python3

# -*- coding: utf-8 -*-
# ══════════════════════════════════════════════════════════════════════════════════════════════════════════════════
# Class:   CreateHeaders
# ──────────────────────────
# Author:  Hengyue Li
# ──────────────────────────
# Version: 2018/01/26
# ──────────────────────────
# discription:
#          Get a header dict used in requests
# ──────────────────────────
# Imported  :
# ──────────────────────────
# Standards :
#
#
# Interface :
#
#        ----------------------
#
#        [ini]
#
#        [sub]  AppendGeneral(key,value):
#               append {key : value} to dict 
#
#        [sub]  AppendLanguage(Lan_Str):
#               Lan_Str = "zh" , "en" , ...
#               see the details in definition.
#
#        [sub] AppendUserAgent(Browser_Str):
#              Browser_Str = "Chrome" , ...
#              see definition
#
# ══════════════════════════════════════════════════════════════════════════════════════════════════════════════════


class CreateHeaders():
    def __init__(self):
        self.Initiated = False
        self.status    = 0       # = 0 is appendable
        self.Return    = {}

    def CheckAppendableOrStop(self):
        if not self.status == 0:
            print("ERROR: In createheaders, Headers is created already")
            exit()

    def GetHeaders(self):
        if not self.status  == 0:
            print("ERROR: CreateHeaders object is used.Consider to create anyonther one.")
            exit()
        self.status  = 1
        return self.Return

    def AppendGeneral(self,key,value):
        self.CheckAppendableOrStop()
        self.Return[key] = LanList[value]



    def AppendLanguage(self,Lan_Str):
        self.CheckAppendableOrStop()
        Lan_Str = Lan_Str.lower()
        LanList = {
        #---------------------------------------
            "zh" :  "zh"               ,
            "en" :  "en-US,en;q=0.5"   ,
        #---------------------------------------
        }
        if Lan_Str not in LanList.keys():
            print("ERROR: unknow Language:",Lan_Str)
            exit()
        self.Return["Accept-Language"] = LanList[Lan_Str]

    def AppendUserAgent(self,Browser_Str):
        self.CheckAppendableOrStop()
        Browser_Str = Browser_Str.lower()
        AgentList = {
        #--------------------------------------
        'chrome' : 'Chrome/39.0.2171.95 '
        #--------------------------------------
        }
        if Browser_Str not in AgentList.keys():
            print("ERROR: unknow User-Agent:",Browser_Str)
            exit()
        self.Return["User-Agent"] = AgentList[Browser_Str]
