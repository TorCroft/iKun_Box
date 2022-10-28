from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from .Ui_video_player import Video_MainWindow
from PyQt5.QtCore import QUrl
from .VideoWidget import VideoWidget


class VideoWindow(Video_MainWindow, QMainWindow):
    def __init__(self):
        super(Video_MainWindow, self).__init__()
        self.setupUi(self)
        self.sld_video_pressed=False
        self.videoFullScreen = False
        
        self.videoFullScreenWidget = VideoWidget()   
        self.player = QMediaPlayer()
        self.player.setVideoOutput(self.wgt_video) 
        self.btn_play.clicked.connect(self.pause_event)      
        self.player.positionChanged.connect(self.changeSlide)
        self.videoFullScreenWidget.doubleClickedItem.connect(self.videoDoubleClicked)
        self.wgt_video.doubleClickedItem.connect(self.videoDoubleClicked)
        self.sld_video.setTracking(False)
        self.sld_video.sliderReleased.connect(self.releaseSlider)
        self.sld_video.sliderPressed.connect(self.pressSlider)
        self.sld_video.sliderMoved.connect(self.moveSlider)
        self.sld_video.ClickedValue.connect(self.clickedSlider)
        self.sld_audio.valueChanged.connect(self.volumeChange)

    def volumeChange(self, position):
        volume= round(position/self.sld_audio.maximum()*100)
        self.player.setVolume(volume)
        self.lab_audio.setText("volume:"+str(volume)+"%")

    def clickedSlider(self, position):
        if self.player.duration() > 0:
            video_position = int((position / 100) * self.player.duration())
            self.player.setPosition(video_position)
            self.lab_video.setText("%.2f%%" % position)
        else:
            self.sld_video.setValue(0)

    def moveSlider(self, position):
        self.sld_video_pressed = True
        if self.player.duration() > 0:
            video_position = int((position / 100) * self.player.duration())
            self.player.setPosition(video_position)
            self.lab_video.setText("%.2f%%" % position)

    def pressSlider(self):
        self.sld_video_pressed = True

    def releaseSlider(self):
        self.sld_video_pressed = False

    def changeSlide(self, position):
        if not self.sld_video_pressed:
            self.vidoeLength = self.player.duration()+0.1
            self.sld_video.setValue(round((position/self.vidoeLength)*100))
            self.lab_video.setText("%.2f%%" % ((position/self.vidoeLength)*100))

    def pause_event(self):
        '''If player.state is 1, it means video is on play. If it is 2, then the video will be paused.'''
        if self.player.state() == 2:
            self.player.play()
            self.btn_play.setText('Pause')
        elif self.player.state() == 1:
            self.player.pause()
            self.btn_play.setText('Play')
    
    @property
    def play_status(self):
        return True if self.player.state() == 1 else False

    def play_event(self, video_path: str):
        self.player.setMedia(QMediaContent(QUrl.fromLocalFile(video_path)))
        self.player.play()

    def videoDoubleClicked(self):
        if self.player.duration() > 0:
            if self.videoFullScreen:
                self.player.setVideoOutput(self.wgt_video)
                self.videoFullScreenWidget.hide()
                self.videoFullScreen = False
            else:
                self.videoFullScreenWidget.show()
                self.player.setVideoOutput(self.videoFullScreenWidget)
                self.videoFullScreenWidget.setFullScreen(1)
                self.videoFullScreen = True

    def closeEvent(self, event) -> None:
        self.player.stop()
        self.btn_play.setText('Pause')
        return

