from .search import searcher
from .download import downloader
from .convert import converter
from .link import text
import os
import time


class Youtube(searcher, downloader, converter, text):
    def __init__(self):
        searcher.__init__(self)
        downloader.__init__(self)
        converter.__init__(self)
        text.__init__(self)

    def menu(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        # shows menu
        print("1. Podaj link do Yt")
        print("2. Wyszukaj po tytule")
        print("3. Wyjscie")

        decision = input("> ")

        if decision == '1':
            # user wants to paste link
            self.link()
        elif decision == '2':
            # user wants to search by title
            self.title()
        elif decision == '3':
            # user decided to leave
            exit()
        else:
            # if unexpected number
            self.menu()

    # function to download by video url
    def link(self):
        self.helperForLink()
        # paste url
        print("Wklej link do filmu: ")
        yt = input("> ")
        # get the right link
        self.setTextToChange(yt)
        url = self.setYtUrl()
        # process it
        self.process(url)

    # function to download by typing title
    def title(self):
        print("Podaj tytul utworu: ")
        yt = input("> ")
        # search the first url of it
        self.setTextToSearch(yt)
        url = self.lookForUrl()
        # use url as argument and process it
        self.process(url)

    # function to download music
    def process(self, text):
        self.setUrl(text)
        videoName = self.getVideoName()

        path = self.fileDownloadedTo()

        self.download(path)

        self.setAudioName(videoName)

        self.convertVideo(path)

        self.moveAudio(path)

        self.deleteMp4(path)

        time.sleep(2)

        # after everything return to menu
        self.menu()

    # Gets path to download directory
    def fileDownloadedTo(self):
        main = os.path.expanduser('~')
        downloadPath = os.path.join(main, 'Downloads')
        newPath = downloadPath + r'\YtToMp3'

        if not os.path.exists(newPath):
            os.makedirs(newPath)
        
        return newPath

    def helperForLink(self):
        print("To jest przykladowy link:")
        print("https://www.youtube.com/watch?v=HluANRwPyNo")
        print("Powinienes mi wkleic:")
        print("> HluANRwPyNo")
        print("-------")
