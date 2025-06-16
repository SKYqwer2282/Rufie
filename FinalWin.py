from instr import *
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication,QWidget,QLabel,QPushButton,QVBoxLayout,QHBoxLayout)
class FinalWin(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.set_appear()
        self.show()
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width,win_height)
        self.move(win_x,win_y)
    def initUI(self):
        self.index=QLabel(txt_index)
        self.heart=QLabel(txt_workheart)
        self.line=QVBoxLayout()
        self.line.addWidget(self.index,alignment=Qt.AlignCenter)
        self.line.addWidget(self.heart,alignment=Qt.AlignCenter)
        self.setLayout(self.line)
    
