"""

Written by Mateusz Rzeczyca.
Self-taught software developer
03.02.2019

"""

from .search import Searcher
from .download import Downloader
from .convert import Converter
import os
import time


def clear_screen():
    """ Clears terminal screen. """
    os.system('cls' if os.name == 'nt' else 'clear')


class Youtube(Searcher, Downloader, Converter):
    """
     Base class for operating downloader.
     Inherits from Searcher, Downloader and Converter.
    """
    def __init__(self):
        Searcher.__init__(self)
        Downloader.__init__(self)
        Converter.__init__(self)

    def menu(self):
        """
        After running menu will show up on the terminal to decide what you want to do.
        """
        clear_screen()
        print("1. Paste Youtube URL")
        print("2. Find from title")
        print("3. Download Video")
        print("4. Exit")
        decision = input("> ")

        if decision == '1':
            self.paste_url_option()
        elif decision == '2':
            self.through_title()
        elif decision == '3':
            self.just_video()
        elif decision == '4':
            exit(0)
        else:
            self.menu()

    def paste_url_option(self):
        """
        Menu option to operate on Youtube URL (paste it, then download video and convert it to MP3 file).

        Raises:
            RuntimeError: URL is not from Youtube
        """
        
        clear_screen()
        print("Paste URL: ")
        url = input("> ")

        if "youtube" not in url:
            raise RuntimeError("This is not Youtube URL")

        name = self.get_video_name(url)

        url_name = {0: url,
                    1: name}

        self.start_processing(url_name)

    def through_title(self):
        """
        Menu option to search for correct video from the title, select the one and then download.
        """

        clear_screen()
        print("Write down the title: ")
        text = input("> ")

        self.set_text_to_search(text)
        urls = self.look_for_urls()
        url = self.choose_right_url(urls)

        self.start_processing(url)

    def just_video(self):
        """
        Menu option to download just mp4 file from the Youtube URL.

        Raises:
            RuntimeError: URL is not from Youtube
        """

        clear_screen()
        print("Paste URL: ")
        url = input("> ")

        if "youtube" not in url:
            raise RuntimeError("This is not Youtube URL")

        name = self.get_video_name(url)

        url_name = {0: url,
                    1: name}

        self.set_url(url_name[0])
        path = self.path_to_downloaded_file()
        self.download_video(path, url_name[1])

    def start_processing(self, url):
        """
        Starts proccessing given URL and title of video.
        Downloads it, converts from MP4 to MP3.

        Args:
            url(dict of int: str): It has to have 2 elements, url[0] = youtube_url and url[1] = video_name
        
        Raises:
            TypeError: url is not dictionary
            RuntimeError: URL is not from Youtube
        """

        if not isinstance(url, dict):
            raise TypeError("Given parameter is not dictionary!")

        if "youtube" not in url[0]:
            raise RuntimeError("This is not Youtube URL")

        self.set_url(url[0])
        path = self.path_to_downloaded_file()
        self.download_video(path, url[1])

        self.set_audio_name(url[1])
        self.convert_mp4_to_mp3(path, url[1])
        self.move_audio(path)
        self.delete_mp4(path, url[1])

        time.sleep(2)
        self.menu()

    def choose_right_url(self, list_of_urls):
        """
        Giving user ability to decide which video should be downloaded.

        Args:
            list_of_urls(list): Stores URLs of every video

        Raises:
            RuntimeError: When url in the list is not from youtube
            TypeError: list_of_urls is not a list
            ValueError: when user inputs index and it is not int value
            IndexError: when user wrote correct index but it does not fit the list

        Returns:
            url_name(dict of int: str): Has 2 elements, url[0] = youtube_url and url[1] = video_name
        """

        list_of_names = []

        if not isinstance(list_of_urls, list):
            raise TypeError("Given parameter is not list!")

        for url in list_of_urls:
            if "youtube" not in url:
                raise RuntimeError("This is not Youtube URL")
            name = self.get_video_name(url)
            list_of_names.append(name)

        meter = 1
        clear_screen()
        for name in list_of_names:
            print('{}. {}'.format(meter, name))
            meter += 1

        print("Choose the index: ")
        index = input('> ')

        try:
            int_index = int(index)
        except ValueError:
            raise ValueError("Given index is not a number!")

        if index - 1 > len(list_of_names):
            raise IndexError("Given index does not fit in this list!")

        url_name = {0: list_of_urls[int(index) - 1],
                    1: list_of_names[int(index) - 1]}

        return url_name
