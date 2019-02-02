# for download video from youtube
from pytube import YouTube
import os


class downloader(object):
    def __init__(self):
        self.url = "None"

    def setUrl(self, text):
        self.url = text

    def getVideoName(self):
        yt = YouTube(self.url)
        videoName = yt.title
        return videoName

    def checkProgress(self, stream = None, chunk = None, file_handle = None, remaining=None):
        # Gets the percentage of the file that has been downloaded
        percent = (100*(fileSize-remaining))/fileSize
        print("Pobrano {:00.0f}%".format(percent))

        os.system('cls' if os.name == 'nt' else 'clear')
    
    def download(self, path):
        print("Plik zostanie pobrany do: {}".format(path))
    
        # Searches for the video and sets up the callback to run the progress indicator. 
        try:
            video = YouTube(self.url, on_progress_callback=self.checkProgress)
        except:
            print("Blad - sprobuj ponownie!")
    
        #Get the first video type - usually the best quality.
        videoType = video.streams.filter(progressive = True, file_extension = "mp4").last()

        global fileSize
        fileSize = videoType.filesize

        #Starts the downloading
        videoType.download(path, 'a')
