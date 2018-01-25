#!/usr/bin/env python3

# url = 'http://types.yuzeli.com/=/msg.ref'
# r = requests.get(url)
#
#
# print(r.text)
import requests
import LoadCookiesTest as lct



cookies = lct.GetLocalCookies().GetCookies()


url = 'https://www.youtube.com/audiolibrary/music'
#
r = requests.get( url = url , cookies = cookies )



print(r.text)




# print(lct.SelectBrowser)
