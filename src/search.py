# import to load site and parse it using BeautifulSoup
import urllib.request
import urllib.parse
import re

class searcher(object):
    def __init__(self):
        self.textToSearch = "None"

    def setTextToSearch(self, text):
        self.textToSearch = text

    def lookForUrl(self):
        queryString = urllib.parse.urlencode({"search_query" : self.textToSearch})
        htmlContent = urllib.request.urlopen("http://www.youtube.com/results?" + queryString)
        searchResults = re.findall(r'href=\"\/watch\?v=(.{11})', htmlContent.read().decode())
        result = "http://www.youtube.com/watch?v=" + searchResults[0]
        return result
