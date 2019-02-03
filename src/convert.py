"""

Written by Mateusz Rzeczyca.
Self-taught software developer
03.02.2019

"""

import moviepy.editor as mp
import os
import shutil


class Converter(object):
    def __init__(self):
        self.audio_name = "None"

    def set_audio_name(self, text):
        self.audio_name = text

    @staticmethod
    def delete_mp4(path):
        video_file = path + r'/a.mp4'

        if os.path.exists(video_file):
            try:
                os.remove(video_file)
            except:
                print("Deleting denied!")

        if os.path.exists(video_file):
            try:
                os.unlink(video_file)
            except:
                print("Deleting denied!")
        else:
            print("Deleting completed!")
            return

    def convert_mp4_to_mp3(self, path):
        video_path = path + r'/a.mp4'
        video_file = mp.VideoFileClip(video_path)

        print("Started Converting")
        audio_file = self.audio_name + ".mp3"
        video_file.audio.write_audiofile(audio_file)
        print("Convert completed")

    def move_audio(self, path):
        audio_file = self.audio_name + ".mp3"

        try:
            shutil.move(audio_file, path)

            print("Completed!")
        except:
            print("Moving denied!")
