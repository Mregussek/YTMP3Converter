"""

Written by Mateusz Rzeczyca.
Self-taught software developer
03.02.2019

"""

from pytube import YouTube
import os


class Downloader(object):
    def __init__(self):
        self.url = "None"

    @staticmethod
    def get_video_name(url):
        yt = YouTube(url)
        video_name = yt.title
        return video_name

    @staticmethod
    def path_to_downloaded_file():
        main = os.path.expanduser('~')
        path = os.path.join(main, 'Downloads')
        new_path = path + r'/YTMP3'

        if not os.path.exists(new_path):
            os.makedirs(new_path)

        return new_path

    def set_url(self, text):
        self.url = text

    @staticmethod
    def check_progress(stream = None, chunk = None, file_handle = None, remaining=None):
        percent = (100*(file_size-remaining))/file_size
        print("Downloaded {:00.0f}%".format(percent))

        os.system('cls' if os.name == 'nt' else 'clear')
    
    def download(self, path):
        try:
            video = YouTube(self.url, on_progress_callback=self.check_progress)
        except:
            print("Got issue, try again!")
            exit(0)

        print("File will be downloaded to: {}".format(path))
        video_type = video.streams.filter(progressive=True, file_extension="mp4").last()

        global file_size
        file_size = video_type.filesize

        video_type.download(path, 'a')


