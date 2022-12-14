from src.Ui_ikun_box import Ui_MainWindow
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication, QMainWindow, qApp
from src.video_player import VideoWindow
from src.audio_player import audio
import sys


class iKun_Box(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(iKun_Box, self).__init__()
        self.setupUi(self)
        self.timer = QTimer()
        self.audio_load = False
        self.pauseButton.clicked.connect(self.pause_event)
        self.stopButton.clicked.connect(self.stop_event)
        self.init_page1_pushbuttons()
        self.init_page2_pushbuttons()
        self.init_page3_pushbuttons()
        self.init_page4_pushbuttons()

    def closeEvent(self, event):
        """Shuts down application on close."""
        sys.stdout = sys.__stdout__
        super().closeEvent(event)

    def run(self, audio_name):
        self.audio_load = True
        if self.pauseButton.text != 'Pause':
            self.pauseButton.setText('Pause')
        self.progressBar.setValue(0)
        audio.play(audio_name)
        if audio.length > 2.0:
            self.set_timer(audio.length * 10)
        else:
            self.audio_load = False
            self.progressBar.hide()

    def set_timer(self, time):
        if self.timer.isActive():
            self.progressBar.setValue(0)
            self.timer.stop()
        self.progressBar.show()
        self.timer.start(int(time))
        self.timer.timeout.connect(self.update_progress_bar)

    def update_progress_bar(self):
        if int(audio.pos / audio.length * 1000) == 0:
            self.timer.stop()
            self.progressBar.hide()
        self.progressBar.setValue(int(audio.pos / audio.length * 100))

    def pause_event(self ,pause_cmd: bool = False):
        if self.timer.isActive() or pause_cmd:
            self.timer.stop()
            self.pauseButton.setText('Unpause')
            return audio.pause()
        elif self.audio_load:
            try:
                self.set_timer(audio.length * 10)
                self.pauseButton.setText('Pause')
                return audio.unpause()
            except:
                pass
        else:
            self.pauseButton.setText('Pause')

    def stop_event(self):
        self.audio_load = False
        self.progressBar.hide()
        self.timer.stop()
        audio.stop_playing()
        if self.pauseButton.text != 'Pause':
            self.pauseButton.setText('Pause')

    def play_video(self, video_name):
        self.pause_event(pause_cmd=True)
        if not video.play_status:
            video.play_event(audio.get_media(video_name))
            video.show()
        else:
            video.close()

    def set_button_text(self, text):
        '''Set specific text on the focused button'''
        btn = qApp.focusWidget()
        if btn is not None:
            btn.setText(text)

    def init_page1_pushbuttons(self):
        self.pushButton_1.clicked.connect(lambda: self.run('???'))
        self.pushButton_2.clicked.connect(lambda: self.run('???'))
        self.pushButton_3.clicked.connect(lambda: self.run('???'))
        self.pushButton_4.clicked.connect(lambda: self.run('???'))
        self.pushButton_5.clicked.connect(lambda: self.run('???????????????'))
        self.pushButton_6.clicked.connect(lambda: self.run('??????????????????'))
        self.pushButton_7.clicked.connect(lambda: self.run('???????????????'))
        self.pushButton_8.clicked.connect(lambda: self.run('?????????'))
        self.pushButton_9.clicked.connect(lambda: self.run('???_1'))
        self.pushButton_10.clicked.connect(lambda: self.run('???'))
        self.pushButton_11.clicked.connect(lambda: self.run('???'))
        self.pushButton_12.clicked.connect(lambda: self.run('?????????'))
        self.pushButton_13.clicked.connect(lambda: self.run('??????'))
        self.pushButton_14.clicked.connect(lambda: self.run('???????????????'))
        self.pushButton_15.clicked.connect(lambda: self.run('??????'))
        self.pushButton_16.clicked.connect(lambda: self.run('???????????????'))
        self.pushButton_17.clicked.connect(lambda: self.run('??????'))
        self.pushButton_18.clicked.connect(lambda: self.run('???????????????'))
        self.pushButton_19.clicked.connect(lambda: self.run('?????????'))
        self.pushButton_20.clicked.connect(lambda: self.run('??????'))
        self.pushButton_21.clicked.connect(lambda: self.run('???'))
        self.pushButton_22.clicked.connect(lambda: self.run('???'))
        self.pushButton_23.clicked.connect(lambda: self.run('rap'))
        self.pushButton_24.clicked.connect(lambda: self.run('??????'))
        self.pushButton_25.clicked.connect(lambda: self.run('music'))
        self.pushButton_26.clicked.connect(lambda: self.run('??????full'))
        self.pushButton_27.clicked.connect(lambda: self.run('??????'))
        self.pushButton_28.clicked.connect(lambda: self.run('???'))
        self.pushButton_29.clicked.connect(lambda: self.run('??????'))
        self.pushButton_30.clicked.connect(lambda: self.run('?????????????????????'))
        self.pushButton_31.clicked.connect(lambda: self.run('?????????'))
        self.pushButton_32.clicked.connect(lambda: self.run('kun'))
        self.pushButton_33.clicked.connect(lambda: self.run('????????????'))
        self.pushButton_34.clicked.connect(lambda: self.run('?????????'))
        self.pushButton_35.clicked.connect(lambda: self.run('???????????????'))
        self.pushButton_36.clicked.connect(lambda: self.run('??????'))
        self.pushButton_37.clicked.connect(lambda: self.run('???????????????'))
        self.pushButton_38.clicked.connect(lambda: self.run('????????????'))
        self.pushButton_39.clicked.connect(lambda: self.run('?????????'))
        self.pushButton_40.clicked.connect(lambda: self.run('?????????'))
        self.pushButton_41.clicked.connect(lambda: self.run('???@??????'))

    def init_page2_pushbuttons(self):
        self.pushButton_p2_1.clicked.connect(lambda: self.run('?????????'))
        self.pushButton_p2_2.clicked.connect(lambda: self.run('?????????'))
        self.pushButton_p2_3.clicked.connect(lambda: self.run('?????????'))
        self.pushButton_p2_4.clicked.connect(lambda: self.play_video('?????????'))
        self.pushButton_p2_5.clicked.connect(lambda: self.play_video('?????????'))
        self.pushButton_p2_6.clicked.connect(lambda: self.run('?????????'))
        self.pushButton_p2_7.clicked.connect(lambda: self.run('?????????'))
        self.pushButton_p2_8.clicked.connect(lambda: self.run('?????????'))
        self.pushButton_p2_9.clicked.connect(lambda: self.run('?????????'))
        self.pushButton_p2_10.clicked.connect(lambda: self.run('?????????'))
        self.pushButton_p2_11.clicked.connect(lambda: self.run('?????????'))
        self.pushButton_p2_12.clicked.connect(lambda: self.run('?????????'))
        self.pushButton_p2_13.clicked.connect(lambda: self.run('?????????'))
        self.pushButton_p2_14.clicked.connect(lambda: self.run('?????????'))
        self.pushButton_p2_15.clicked.connect(lambda: self.run('?????????'))
        self.pushButton_p2_16.clicked.connect(lambda: self.run('?????????'))
        self.pushButton_p2_17.clicked.connect(lambda: self.run('?????????'))
        self.pushButton_p2_18.clicked.connect(lambda: self.play_video('??????'))
        self.pushButton_p2_19.clicked.connect(lambda: self.run('???????????????'))
        self.pushButton_p2_20.clicked.connect(lambda: self.run('?????????'))
        self.pushButton_p2_21.clicked.connect(lambda: self.play_video('???????????????'))
        self.pushButton_p2_22.clicked.connect(lambda: self.play_video('??????????????????'))
        self.pushButton_p2_23.clicked.connect(lambda: self.play_video('?????????'))
        self.pushButton_p2_24.clicked.connect(lambda: self.run('?????????'))
        self.pushButton_p2_25.clicked.connect(lambda: self.run('?????????'))
        self.pushButton_p2_26.clicked.connect(lambda: self.run('????????????'))
        self.pushButton_p2_27.clicked.connect(lambda: self.run('?????????'))
        self.pushButton_p2_28.clicked.connect(lambda: self.play_video('????????????'))
        self.pushButton_p2_29.clicked.connect(lambda: self.play_video('????????????'))
        
    def init_page3_pushbuttons(self):
        self.pushButton_p3_1.clicked.connect(lambda: self.run('????????????'))
        self.pushButton_p3_2.clicked.connect(lambda: self.run('????????????'))
        self.pushButton_p3_3.clicked.connect(lambda: self.run('?????????'))
        self.pushButton_p3_4.clicked.connect(lambda: self.run('??????money'))
        self.pushButton_p3_5.clicked.connect(lambda: self.run('????????????'))
        self.pushButton_p3_6.clicked.connect(lambda: self.run('????????????'))
        self.pushButton_p3_7.clicked.connect(lambda: self.run('?????????'))
        self.pushButton_p3_8.clicked.connect(lambda: self.run('????????????'))
        self.pushButton_p3_9.clicked.connect(lambda: self.run('????????????'))
        self.pushButton_p3_10.clicked.connect(lambda: self.run('????????????'))
        self.pushButton_p3_11.clicked.connect(lambda: self.run('????????????'))
        self.pushButton_p3_12.clicked.connect(lambda: self.run('??????'))
        self.pushButton_p3_13.clicked.connect(lambda: self.run('??????????????????'))
        self.pushButton_p3_14.clicked.connect(lambda: self.run('?????????????????????'))
        self.pushButton_p3_15.clicked.connect(lambda: self.run('?????????'))
        self.pushButton_p3_16.clicked.connect(lambda: self.run('?????????'))
        self.pushButton_p3_17.clicked.connect(lambda: self.run('??????'))
        self.pushButton_p3_18.clicked.connect(lambda: self.run('ikun????????????'))
        self.pushButton_p3_19.clicked.connect(lambda: self.run('??????1'))
        self.pushButton_p3_20.clicked.connect(lambda: self.run('??????2'))
        self.pushButton_p3_21.clicked.connect(lambda: self.run('??????3'))
        self.pushButton_p3_22.clicked.connect(lambda: self.run('??????4'))
        self.pushButton_p3_23.clicked.connect(lambda: self.run('??????5'))
        self.pushButton_p3_24.clicked.connect(lambda: self.run('??????6'))
        self.pushButton_p3_25.clicked.connect(lambda: self.run('??????7'))
        self.pushButton_p3_26.clicked.connect(lambda: self.run('??????8'))
        self.pushButton_p3_27.clicked.connect(lambda: self.run('??????9'))
        self.pushButton_p3_28.clicked.connect(lambda: self.run('??????10'))
        self.pushButton_p3_29.clicked.connect(lambda: self.run('??????11'))
        self.pushButton_p3_30.clicked.connect(lambda: self.run('??????12'))
        self.pushButton_p3_31.clicked.connect(lambda: self.run('??????13'))
        self.pushButton_p3_32.clicked.connect(lambda: self.run('??????14'))
        self.pushButton_p3_33.clicked.connect(lambda: self.run('?????????????????????'))
        self.pushButton_p3_34.clicked.connect(lambda: self.run('??????????????????'))

    def init_page4_pushbuttons(self):
        self.pushButton_p4_1.clicked.connect(lambda: self.play_video('????????????'))
        self.pushButton_p4_2.clicked.connect(lambda: self.play_video('???????????????'))
        self.pushButton_p4_3.clicked.connect(lambda: self.play_video('????????????'))
        self.pushButton_p4_4.clicked.connect(lambda: self.play_video('????????????'))
        self.pushButton_p4_5.clicked.connect(lambda: self.play_video('???????????????'))
        self.pushButton_p4_6.clicked.connect(lambda: self.play_video('?????????'))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ikun_box = iKun_Box()
    ikun_box.show()
    video = VideoWindow()
    sys.exit(app.exec_())
