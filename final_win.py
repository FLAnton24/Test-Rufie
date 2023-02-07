# напиши здесь код третьего экрана приложения
# напиши здесь код основного приложения и первого экрана
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication , QWidget,
    QHBoxLayout, QVBoxLayout,
    QGroupBox, QRadioButton,
    QPushButton, QLabel, QListWidget, QLineEdit)

from import*
my.app.py
from instr import*
class MainWin(QWidget):
    

class FinalWin(QWIdget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUT()
        self.show
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
    def initUT(self):
        self.workh_text = QLabel(txt_workheart)
        self.index_text = QLabel(txt_index)
        self.layout_line = QVBoxLayout()
        self.layout_line.addWidget(self.index_text, alignment = Qt.AlignCenter)
        self.layout_line.addWidget(self.wokh_text, alignment = Qt.AlignCenter)
        self.setLayout(self.layout_line)
