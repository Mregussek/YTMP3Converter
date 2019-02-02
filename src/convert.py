# for converting mp4 to mp3
import moviepy.editor as mp

# to erase '.mp4' files from current folder
import os

# to move file to download directory
import shutil

class converter(object):
    def _init__(self):
        self.audioName = "None"

    def setAudioName(self, text):
        self.audioName = text

    def deleteMp4(self, path):
        videoFile = path + r'\a.mp4'

        if os.path.exists(videoFile):
            try:
                os.remove(videoFile)
            except:
                print("Deleting denied!")

        if os.path.exists(videoFile):
            try:
                os.unlink(videoFile)
            except:
                print("Deleting denied!")
        else:
            print("Deleting completed!")
            return

    def convertVideo(self, path):
        # get the video
        videoPath = path + r'\a.mp4'
        videoFile = mp.VideoFileClip(videoPath)

        print("Started Converting")

        audioFile = self.audioName + ".mp3"
        videoFile.audio.write_audiofile(audioFile)

        print("Convert completed")

    def moveAudio(self, path):
        audioFile = self.audioName + ".mp3"

        try:
            shutil.move(audioFile, path)

            print("Completed!")
        except:
            print("Moving denied!")