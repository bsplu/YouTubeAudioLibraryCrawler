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

Page = requests.get( url = url , cookies = cookies )



l = Page.json

# r = requests.post('http://httpbin.org/post', data = {'key':'value'}, cookies = cookies)
# r = Page.post(  data = {'key':'value'})
print( l  )




# print(lct.SelectBrowser)
