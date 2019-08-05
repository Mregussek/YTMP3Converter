"""

Written by Mateusz Rzeczyca.
Self-taught software developer
03.02.2019

"""

from pytube import YouTube
import os


class Downloader(object):
    """ 
    Base Class for managing downloading.
    
    Attributes:
        url(str): stores Youtube URL
    """

    def __init__(self):
        self.url = "None"

    @staticmethod
    def get_video_name(url):
        """
        Static Method that gets video name from given URL.

        Args:
            url(str): URL of Youtube video

        Raises:
            RuntimeError: Cannot create Youtube class object

        Returns:
            video_name: Title of the video
        """

        try:
            yt = YouTube(url)
        except:
            raise RuntimeError("Cannot create Youtube class object!")

        video_name = yt.title
        return video_name

    @staticmethod
    def path_to_downloaded_file():
        """
        Static Method that returns path, where will be downloaded file.
        If needed it creates ~/Downloads/YTMP3

        Returns:
            new_path: path which is ~/Downloads/YTMP3
        """
        main = os.path.expanduser('~')
        path = os.path.join(main, 'Downloads')
        new_path = path + r'/YTMP3'

        if not os.path.exists(new_path):
            os.makedirs(new_path)

        return new_path

    def set_url(self, text):
        """
        Set class url attribute with parameter.
        Setter method.

        Args:
            text(str): url to set
        """
        self.url = text

    @staticmethod
    def check_progress(stream = None, chunk = None, file_handle = None, remaining=None):
        """
        Static method for checking progress of downloaded file.
        """
        percent = (100*(file_size-remaining))/file_size
        print("Downloaded {:00.0f}%".format(percent))

        os.system('cls' if os.name == 'nt' else 'clear')
    
    def download_video(self, path, name):
        """
        The most important method - downloads MP4 file from class attribute url.

        Args:
            path(str): path, where the file be downloaded
            name(str): title of the video

        Raises:
            RuntimeError: Cannot create Youtube class object
        """
        
        try:
            video = YouTube(self.url, on_progress_callback=self.check_progress)
        except:
            raise RuntimeError("Cannot create Youtube class object!")

        print("File will be downloaded to: {}".format(path))
        video_type = video.streams.filter(progressive=True, file_extension="mp4").last()

        global file_size
        file_size = video_type.filesize

        video_type.download(path, name)


