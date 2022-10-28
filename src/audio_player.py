from pygame import mixer
from mutagen.mp3 import MP3
from PyQt5.QtCore import QUrl
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
import os


class Audio_Player(object):
    def __init__(self):
        self.file = None
        mixer.init()
        self.player = QMediaPlayer()
        self.sound = self.get_sound_list()

    def get_media(self, file_name) -> str:
        return self.sound[file_name]

    @staticmethod
    def get_sound_list():
        sound_dict = {}
        for i in os.listdir(os.path.join('resources', 'sounds')):
            for j in os.listdir(os.path.join('resources', 'sounds', i)):
                sound_dict[j.split('.')[0]] = os.path.join('resources', 'sounds', i, j)
        return sound_dict

    def get_pos(self):
        game_pos = mixer.music.get_pos()
        if game_pos == -1:
            return False
        return game_pos / 1000

    @property
    def pos(self):
        return self.get_pos()

    @property
    def length(self):
        '''Length of audio file.'''
        return MP3(self.file).info.length

    @property
    def status(self):
        return True if mixer.music.get_busy() == 1 else False

    def play(self,file_name):
        try:
            self.file = self.sound[file_name]
        except KeyError:
            print('No such music file.')
        else:
            mixer.music.load(self.file)
            mixer.music.play()
    
    @staticmethod
    def pause():
        return mixer.music.pause()

    @staticmethod
    def unpause():
        return mixer.music.unpause()

    @staticmethod
    def stop_playing():
        """Stop playing and release audio file."""
        mixer.music.stop()
        mixer.music.unload()



audio = Audio_Player()
