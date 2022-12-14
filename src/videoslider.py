from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtWidgets import QSlider

class VideoSlider(QSlider):
    ClickedValue = pyqtSignal(int)

    def __init__(self, father):
        super().__init__(Qt.Horizontal, father)

    def mousePressEvent(self, QMouseEvent):     #单击事件
        super().mousePressEvent(QMouseEvent)
        value = QMouseEvent.localPos().x()
        value = round(value/self.width()*self.maximum())  # 根据鼠标点击的位置和slider的长度算出百分比
        self.ClickedValue.emit(value)
