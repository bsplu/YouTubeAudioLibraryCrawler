#/usr/bin/env python3

# -*- coding: utf-8 -*-
# ══════════════════════════════════════════════════════════════════════════════════════════════════════════════════
# Class:   RuleSelection
# ──────────────────────────
# Author:  Hengyue Li
# ──────────────────────────
# Version: 2018/01/26
# ──────────────────────────
# discription:
#          Input Dictionary list. According to a rule, output any other list of  disctionary.
# ──────────────────────────
# Imported  :
import Usage
# ──────────────────────────
# Standards :
#
#
# Interface :
#
#        ----------------------
#
#        [ini]  InputDicList
#
#        [fun]  GetSelection(rule_dict)
#               return a list of Dictionary
#
#        [sub]  GetSelectionToXmlFile(rule_dict,XmlPath)
#
#
#
#
#
# ══════════════════════════════════════════════════════════════════════════════════════════════════════════════════




class RuleSelection():
    def __init__(self,Data):
        self.DicList = Data


    def GetSelection(self,rule):
        R = []
        Rulekeys = rule.keys()
        for jc in self.DicList:
            if self.IsTarget(jc,Rulekeys,rule):
                R.append(jc)
        return R

    def IsTarget(self,Dict,Rulekeys,rule):
        R = True
        for jc in Rulekeys:
            if type(Dict[jc]==list):
               if not rule[jc] in Dict[jc]:
                    R = False
                    break
            else:
               if not rule[jc] == Dict[jc] :
                  R = False
                  break
        return R

    def GetSelectionToXmlFile(self,rule_dict,XmlPath):
        Selected = self.GetSelection(rule_dict)
        xml = { jc['vid']:jc  for jc in Selected}
        xml = Usage.dicttoxml.dicttoxml(xml)
        dom = Usage.parseString(xml)
        st = dom.toprettyxml()
        file_handle = open(XmlPath,"w")
        file_handle.write(st)
        file_handle.close()
