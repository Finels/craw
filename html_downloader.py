import urllib.request
'''
html链接抓取器，使用python自带的urllib模块
a htmlfinder is used for catch any url , a normal python module named urllib is used 
'''

class HtmlDownloader(object):
    def download(self, url):
        if url is None:
            return None
        response = urllib.request.urlopen(url)
        if response.getcode() != 200:
            return None
        return response.read()
