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
    os.system('cls' if os.name == 'nt' else 'clear')


class Youtube(Searcher, Downloader, Converter):
    def __init__(self):
        Searcher.__init__(self)
        Downloader.__init__(self)
        Converter.__init__(self)

    def menu(self):
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
        clear_screen()
        print("Paste URL: ")
        url = input("> ")
        name = self.get_video_name(url)

        url_name = {0: url,
                    1: name}

        self.start_processing(url_name)

    def through_title(self):
        clear_screen()
        print("Write down the title: ")
        text = input("> ")

        self.set_text_to_search(text)
        urls = self.look_for_urls()
        url = self.choose_right_url(urls)

        self.start_processing(url)

    def just_video(self):
        clear_screen()
        print("Paste URL: ")
        url = input("> ")
        name = self.get_video_name(url)

        url_name = {0: url,
                    1: name}

        self.set_url(url_name[0])
        path = self.path_to_downloaded_file()
        self.download_video(path, url_name[1])

    def start_processing(self, url):
        self.set_url(url[0])
        path = self.path_to_downloaded_file()
        self.download(path)

        self.set_audio_name(url[1])
        self.convert_mp4_to_mp3(path)
        self.move_audio(path)
        self.delete_mp4(path)

        time.sleep(2)
        self.menu()

    def choose_right_url(self, list_of_urls):
        list_of_names = []

        for url in list_of_urls:
            name = self.get_video_name(url)
            list_of_names.append(name)

        meter = 1
        clear_screen()
        for name in list_of_names:
            print('{}. {}'.format(meter, name))
            meter += 1

        print("Choose the index: ")
        index = input('> ')

        url_name = {0: list_of_urls[int(index) - 1],
                    1: list_of_names[int(index) - 1]}

        return url_name
