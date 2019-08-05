"""

Written by Mateusz Rzeczyca.
Self-taught software developer
03.02.2019

"""

import urllib.request
import urllib.parse
from bs4 import BeautifulSoup


class Searcher(object):
    """
    Base class, which main point is to search YT url from given title.

    Attributes:
        textToSearch(str): title of the video
    """

    def __init__(self):
        self.textToSearch = "None"

    def set_text_to_search(self, text):
        """
        Set class textToSearch attribute with parameter.
        Setter method.

        Args:
            text(str): text which will be set
        """

        self.textToSearch = text

    def look_for_urls(self):
        """
        Looks for some Youtube URLs with the title (textToSearch).

        Returns:
            tab_of_urls(list): contains urls of videos
        """
        tab_of_urls = []
        query = urllib.parse.quote(self.textToSearch)
        url = "https://www.youtube.com/results?search_query=" + query
        response = urllib.request.urlopen(url)
        html = response.read()
        soup = BeautifulSoup(html, 'html.parser')
        meter = 0
        for vid in soup.findAll(attrs={'class': 'yt-uix-tile-link'}):
            if self.if_yt_watch_url(vid['href']):
                meter += 1
                if meter == 6:
                    break

                one_url = 'https://www.youtube.com' + vid['href']
                tab_of_urls.append(one_url)

        return tab_of_urls

    @staticmethod
    def if_yt_watch_url(text):
        """
        Decides whether given parameter is Youtube URL or not.

        Args:
            text(str): Youtube URL

        Returns:
            decision(bool): true if it YT URL, false if not
        """
        if '/watch?' in text:
            return True
        else:
            return False
