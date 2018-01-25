#!/usr/bin/env python3




#------------------------------------------------------
#       get password
#------------------------------------------------------
import sys,os
from pathlib import Path
home = str(Path.home())
AutoPassDirc = home + '/Documents/AutoPassword'
sys.path.insert(0,AutoPassDirc)
import password as pw


username = pw.GetAutoPasswd('git2','username').get()
password = pw.GetAutoPasswd('git2','password').get()
project  = pw.GetAutoPasswd('git2','project').get()
#------------------------------------------------------



import datetime,os
time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
gitadd = "git add .;"
gitcom = "git commit -m "+"\""+time+"\";"
gitpus = "git push https://"+username+":"+password+"@"+project+" --force;"


os.system(  gitadd + gitcom + gitpus )
