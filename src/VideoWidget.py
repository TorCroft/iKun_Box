from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtCore import pyqtSignal


class VideoWidget(QVideoWidget):
    doubleClickedItem = pyqtSignal(str)

    def __init__(self, parent=None):
        super(QVideoWidget, self).__init__(parent)


    def mouseDoubleClickEvent(self, QMouseEvent):
        self.doubleClickedItem.emit("double clicked")


