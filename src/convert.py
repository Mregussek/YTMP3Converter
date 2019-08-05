"""

Written by Mateusz Rzeczyca.
Self-taught software developer
03.02.2019

"""

import moviepy.editor as mp
import os
import shutil


class Converter(object):
    """
    Base class for converting file from MP4 to MP3.

    Attributes:
        audio_name(str): contains MP3 file name
    """
    def __init__(self):
        self.audio_name = "None"

    def set_audio_name(self, text):
        """
        Set class audio_name attribute with parameter.
        Setter method.

        Args:
            text(str): audio name to set
        """
        self.audio_name = text

    @staticmethod
    def delete_mp4(path, name):
        """
        After completed conversion I want to delete unnecessary MP4 file.

        Args:
            path(str): contains path to directory of file
            name(str): title of the video
        
        Raises:
            RuntimeError: only when cannot delete correctly mp4 file
        """

        video_file = path + r'/{}.mp4'.format(name)

        if os.path.exists(video_file):
            try:
                os.remove(video_file)
            except:
                raise RuntimeError("Cannot delete file with os.remove()!")

        if os.path.exists(video_file):
            try:
                os.unlink(video_file)
            except:
                raise RuntimeError("Cannot delete file with os.unlink()!")

        print("Deleting completed!")

    def convert_mp4_to_mp3(self, path, name):
        """
        Converts MP4 video file to MP3 file.

        Args:
            path(str): contains path to directory of file
            name(str): title of the video

        Raises:
            RuntimeError: cannot create VideoFileClip class object
            RuntimeError: cannot convert file
        """

        video_path = path + r'/{}.mp4'.format(name)

        try:
            video_file = mp.VideoFileClip(video_path)
        except:
            raise RuntimeError("Cannot create VideoFileClip class object!")

        print("Started Converting")
        audio_file = self.audio_name + ".mp3"
        try:
            video_file.audio.write_audiofile(audio_file)
        except:
            raise RuntimeError("Cannot convert MP4 to MP3!")

        print("Convert completed")

    def move_audio(self, path):
        """
        Changes path of MP3 File

        Args:
            path(str): correct path
        
        Raises:
            RuntimeError: cannot move file
        """
        audio_file = self.audio_name + ".mp3"

        try:
            shutil.move(audio_file, path)
        except:
            raise RuntimeError("Cannot move file!")

        print("Completed!")
