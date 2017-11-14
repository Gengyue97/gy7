Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import urllib
>>> import urllib2
>>> values = {}
>>> values['username'] = "1486373118@qq.com"
>>> values['password'] = "XXXX"
>>> data = urllib.urlencode(values)
>>> url = "https://github.com/Gengyue97/gy7.git"
>>> request = urllib2.Request(url,data)
>>> response = urllib2.urlopen(request)
>>> print response.geturl()
https://github.com/Gengyue97/gy7
>>> 
