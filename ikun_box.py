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
        self.pushButton_1.clicked.connect(lambda: self.run('鸡'))
        self.pushButton_2.clicked.connect(lambda: self.run('你'))
        self.pushButton_3.clicked.connect(lambda: self.run('太'))
        self.pushButton_4.clicked.connect(lambda: self.run('美'))
        self.pushButton_5.clicked.connect(lambda: self.run('鸡你太美短'))
        self.pushButton_6.clicked.connect(lambda: self.run('鸡你实在太美'))
        self.pushButton_7.clicked.connect(lambda: self.run('你干嘛哎吆'))
        self.pushButton_8.clicked.connect(lambda: self.run('你干嘛'))
        self.pushButton_9.clicked.connect(lambda: self.run('你_1'))
        self.pushButton_10.clicked.connect(lambda: self.run('干'))
        self.pushButton_11.clicked.connect(lambda: self.run('嘛'))
        self.pushButton_12.clicked.connect(lambda: self.run('哇哈哈'))
        self.pushButton_13.clicked.connect(lambda: self.run('哎吆'))
        self.pushButton_14.clicked.connect(lambda: self.run('你干嘛倒放'))
        self.pushButton_15.clicked.connect(lambda: self.run('鸡叫'))
        self.pushButton_16.clicked.connect(lambda: self.run('全民制作人'))
        self.pushButton_17.clicked.connect(lambda: self.run('我是'))
        self.pushButton_18.clicked.connect(lambda: self.run('时长两年半'))
        self.pushButton_19.clicked.connect(lambda: self.run('蔡徐坤'))
        self.pushButton_20.clicked.connect(lambda: self.run('喜欢'))
        self.pushButton_21.clicked.connect(lambda: self.run('唱'))
        self.pushButton_22.clicked.connect(lambda: self.run('跳'))
        self.pushButton_23.clicked.connect(lambda: self.run('rap'))
        self.pushButton_24.clicked.connect(lambda: self.run('篮球'))
        self.pushButton_25.clicked.connect(lambda: self.run('music'))
        self.pushButton_26.clicked.connect(lambda: self.run('全民full'))
        self.pushButton_27.clicked.connect(lambda: self.run('干嘛'))
        self.pushButton_28.clicked.connect(lambda: self.run('啊'))
        self.pushButton_29.clicked.connect(lambda: self.run('哈哈'))
        self.pushButton_30.clicked.connect(lambda: self.run('厉不厉害你坤哥'))
        self.pushButton_31.clicked.connect(lambda: self.run('英文名'))
        self.pushButton_32.clicked.connect(lambda: self.run('kun'))
        self.pushButton_33.clicked.connect(lambda: self.run('厉不厉害'))
        self.pushButton_34.clicked.connect(lambda: self.run('你坤哥'))
        self.pushButton_35.clicked.connect(lambda: self.run('个人练习坤'))
        self.pushButton_36.clicked.connect(lambda: self.run('笑死'))
        self.pushButton_37.clicked.connect(lambda: self.run('我特别厉害'))
        self.pushButton_38.clicked.connect(lambda: self.run('特别厉害'))
        self.pushButton_39.clicked.connect(lambda: self.run('大家好'))
        self.pushButton_40.clicked.connect(lambda: self.run('两年半'))
        self.pushButton_41.clicked.connect(lambda: self.run('你@干嘛'))

    def init_page2_pushbuttons(self):
        self.pushButton_p2_1.clicked.connect(lambda: self.run('三国鸡'))
        self.pushButton_p2_2.clicked.connect(lambda: self.run('仙剑鸡'))
        self.pushButton_p2_3.clicked.connect(lambda: self.run('化鸡飞'))
        self.pushButton_p2_4.clicked.connect(lambda: self.play_video('赛尔鸡'))
        self.pushButton_p2_5.clicked.connect(lambda: self.play_video('鸡出没'))
        self.pushButton_p2_6.clicked.connect(lambda: self.run('卡点鸡'))
        self.pushButton_p2_7.clicked.connect(lambda: self.run('印度鸡'))
        self.pushButton_p2_8.clicked.connect(lambda: self.run('大悲鸡'))
        self.pushButton_p2_9.clicked.connect(lambda: self.run('小母鸡'))
        self.pushButton_p2_10.clicked.connect(lambda: self.run('新年鸡'))
        self.pushButton_p2_11.clicked.connect(lambda: self.run('新闻鸡'))
        self.pushButton_p2_12.clicked.connect(lambda: self.run('果宝鸡'))
        self.pushButton_p2_13.clicked.connect(lambda: self.run('欢喜鸡'))
        self.pushButton_p2_14.clicked.connect(lambda: self.run('耶耶鸡'))
        self.pushButton_p2_15.clicked.connect(lambda: self.run('葫芦鸡'))
        self.pushButton_p2_16.clicked.connect(lambda: self.run('青蛙鸡'))
        self.pushButton_p2_17.clicked.connect(lambda: self.run('狂放鸡'))
        self.pushButton_p2_18.clicked.connect(lambda: self.play_video('鸡战'))
        self.pushButton_p2_19.clicked.connect(lambda: self.run('鸡你太美长'))
        self.pushButton_p2_20.clicked.connect(lambda: self.run('谢谢鸡'))
        self.pushButton_p2_21.clicked.connect(lambda: self.play_video('仙剑鸡侠传'))
        self.pushButton_p2_22.clicked.connect(lambda: self.play_video('本草鸡目视频'))
        self.pushButton_p2_23.clicked.connect(lambda: self.play_video('千年鸡'))
        self.pushButton_p2_24.clicked.connect(lambda: self.run('植物鸡'))
        self.pushButton_p2_25.clicked.connect(lambda: self.run('江南鸡'))
        self.pushButton_p2_26.clicked.connect(lambda: self.run('落入鸡尘'))
        self.pushButton_p2_27.clicked.connect(lambda: self.run('西游鸡'))
        self.pushButton_p2_28.clicked.connect(lambda: self.play_video('终鸡猎手'))
        self.pushButton_p2_29.clicked.connect(lambda: self.play_video('骑鸡再现'))
        
    def init_page3_pushbuttons(self):
        self.pushButton_p3_1.clicked.connect(lambda: self.run('告诉你们'))
        self.pushButton_p3_2.clicked.connect(lambda: self.run('如果再黑'))
        self.pushButton_p3_3.clicked.connect(lambda: self.run('小心我'))
        self.pushButton_p3_4.clicked.connect(lambda: self.run('花点money'))
        self.pushButton_p3_5.clicked.connect(lambda: self.run('把你们都'))
        self.pushButton_p3_6.clicked.connect(lambda: self.run('告上法庭'))
        self.pushButton_p3_7.clicked.connect(lambda: self.run('犯法了'))
        self.pushButton_p3_8.clicked.connect(lambda: self.run('用他人的'))
        self.pushButton_p3_9.clicked.connect(lambda: self.run('照片改成'))
        self.pushButton_p3_10.clicked.connect(lambda: self.run('公鸡母鸡'))
        self.pushButton_p3_11.clicked.connect(lambda: self.run('还有母猪'))
        self.pushButton_p3_12.clicked.connect(lambda: self.run('荔枝'))
        self.pushButton_p3_13.clicked.connect(lambda: self.run('你让我拿什么'))
        self.pushButton_p3_14.clicked.connect(lambda: self.run('还要我怎么荔枝'))
        self.pushButton_p3_15.clicked.connect(lambda: self.run('荔枝啊'))
        self.pushButton_p3_16.clicked.connect(lambda: self.run('荔枝全'))
        self.pushButton_p3_17.clicked.connect(lambda: self.run('连招'))
        self.pushButton_p3_18.clicked.connect(lambda: self.run('ikun真情流露'))
        self.pushButton_p3_19.clicked.connect(lambda: self.run('语录1'))
        self.pushButton_p3_20.clicked.connect(lambda: self.run('语录2'))
        self.pushButton_p3_21.clicked.connect(lambda: self.run('语录3'))
        self.pushButton_p3_22.clicked.connect(lambda: self.run('语录4'))
        self.pushButton_p3_23.clicked.connect(lambda: self.run('语录5'))
        self.pushButton_p3_24.clicked.connect(lambda: self.run('语录6'))
        self.pushButton_p3_25.clicked.connect(lambda: self.run('语录7'))
        self.pushButton_p3_26.clicked.connect(lambda: self.run('语录8'))
        self.pushButton_p3_27.clicked.connect(lambda: self.run('语录9'))
        self.pushButton_p3_28.clicked.connect(lambda: self.run('语录10'))
        self.pushButton_p3_29.clicked.connect(lambda: self.run('语录11'))
        self.pushButton_p3_30.clicked.connect(lambda: self.run('语录12'))
        self.pushButton_p3_31.clicked.connect(lambda: self.run('语录13'))
        self.pushButton_p3_32.clicked.connect(lambda: self.run('语录14'))
        self.pushButton_p3_33.clicked.connect(lambda: self.run('荔枝拿什么荔枝'))
        self.pushButton_p3_34.clicked.connect(lambda: self.run('娱乐圈的规矩'))

    def init_page4_pushbuttons(self):
        self.pushButton_p4_1.clicked.connect(lambda: self.play_video('暴揍三浦'))
        self.pushButton_p4_2.clicked.connect(lambda: self.play_video('暴揍美国人'))
        self.pushButton_p4_3.clicked.connect(lambda: self.play_video('暴揍雷神'))
        self.pushButton_p4_4.clicked.connect(lambda: self.play_video('暴揍灭霸'))
        self.pushButton_p4_5.clicked.connect(lambda: self.play_video('终鸡杀人王'))
        self.pushButton_p4_6.clicked.connect(lambda: self.play_video('鸡元甲'))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ikun_box = iKun_Box()
    ikun_box.show()
    video = VideoWindow()
    sys.exit(app.exec_())
