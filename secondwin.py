from instr import *
from PyQt5.QtCore import Qt, QTimer, QTime
from PyQt5.QtWidgets import (QApplication,QWidget,QLabel,QPushButton,QVBoxLayout,QHBoxLayout,QLineEdit)
from PyQt5.QtGui import QFont
from FinalWin import *
class Experiment():
    def __init__(self,age,test1,test2,test3):
        self.age=age
        self.t1=test1
        self.t2=test2
        self.t3=test3
class TestWin(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.connects()
        self.set_appear()
        self.show()
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width,win_height)
        self.move(win_x,win_y)
    def initUI(self):
        self.but1=QPushButton(txt_b1)
        self.but2=QPushButton(txt_b2)
        self.but3=QPushButton(txt_b3)
        self.but4=QPushButton(txt_b4)
        self.textname=QLabel(txt_name)
        self.age=QLabel(txt_age)
        self.textinstur1=QLabel(txt_test1)
        self.textinstur2=QLabel(txt_test2)
        self.textinstur3=QLabel(txt_test3)
        self.timere=QLabel(txt_timer)
        self.surname=QLineEdit(txt_surname)
        self.test1=QLineEdit(txt_t01)
        self.test2=QLineEdit(txt_t02)
        self.test3=QLineEdit(txt_t03)
        self.test4=QLineEdit(txt_t04)
        self.lineh=QHBoxLayout()
        self.liner=QVBoxLayout()
        self.linel=QVBoxLayout()
        self.liner.addWidget(self.timere,alignment=Qt.AlignCenter)
        self.linel.addWidget(self.textname,alignment=Qt.AlignLeft)
        self.linel.addWidget(self.surname,alignment=Qt.AlignLeft)
        self.linel.addWidget(self.age,alignment=Qt.AlignLeft)
        self.linel.addWidget(self.test1,alignment=Qt.AlignLeft)
        self.linel.addWidget(self.textinstur1,alignment=Qt.AlignLeft)
        self.linel.addWidget(self.but1,alignment=Qt.AlignLeft)
        self.linel.addWidget(self.test2,alignment=Qt.AlignLeft)
        self.linel.addWidget(self.textinstur2,alignment=Qt.AlignLeft)
        self.linel.addWidget(self.but2,alignment=Qt.AlignLeft)
        self.linel.addWidget(self.textinstur3,alignment=Qt.AlignLeft)
        self.linel.addWidget(self.but3,alignment=Qt.AlignLeft)
        self.linel.addWidget(self.test3,alignment=Qt.AlignLeft)
        self.linel.addWidget(self.test4,alignment=Qt.AlignLeft)
        self.linel.addWidget(self.but4,alignment=Qt.AlignRight)
        self.lineh.addLayout(self.linel)
        self.lineh.addLayout(self.liner)
        self.setLayout(self.lineh)
    def next_click(self):
        self.hide()
        
        self.exp = Experiment(
            age=int(self.test1.text()),  
            test1=self.test2.text(),    
            test2=self.test3.text(),    
            test3=self.test4.text()    
        )
        self.tw = FinalWin(self.exp)  
    def results(self):
        self.index=(4*(int(self.exp.t1)+int(self.exp.t2)+int(self.exp.t3))-200)/10
    def timer_test(self):
        global time
        time=QTime(0,0,15)
        self.timer=QTimer()
        self.timer.timeout.connect(self.timer1Event)
        self.timer.start(1000)
    def timer1Event(self):
        global time
        time=time.addSecs(-1)
        self.timere.setText(time.toString("hh:mm:ss"))
        self.timere.setFont(QFont('Times',36,QFont.Bold))
        self.timere.setStyleSheet('color: rgb(0,0,0)')
        if time.toString("hh:mm:ss")=='00:00:00':
            self.timer.stop()
    def timer_sits(self):
        global time
        time=QTime(0,0,30)
        self.timer=QTimer()
        self.timer.timeout.connect(self.timer2Event)
        self.timer.start(1500)
    def timer2Event(self):
        global time
        time = time.addSecs(-1) 
        self.timere.setText(time.toString("hh:mm:ss")[6:8]) 
        self.timere.setStyleSheet("color: rgb(0,0,0)") 
        self.timere.setFont(QFont("Times", 36, QFont.Bold)) 
        if time.toString("hh:mm:ss") == "00:00:00": 
            self.timer.stop()
    def timer_final(self):
        global time
        time=QTime(0,1,0)
        self.timer=QTimer()
        self.timer.timeout.connect(self.timer3Event)
        self.timer.start(1000)
    def timer3Event(self):
        global time
        time = time.addSecs(-1)
        self.timere.setText(time.toString("hh:mm:ss"))
        seconds = int(time.toString("hh:mm:ss")[6:8])  
        if seconds >= 45 or seconds <= 15:
            self.timere.setStyleSheet("color: rgb(0, 255, 0)") 
        else:
            self.timere.setStyleSheet("color: rgb(0, 0, 0)")    
        self.timere.setFont(QFont("Times", 36, QFont.Bold))
        if time.toString("hh:mm:ss") == "00:00:00":
            self.timer.stop()
    def connects(self):
        self.but4.clicked.connect(self.next_click)
        self.but1.clicked.connect(self.timer_test)
        self.but2.clicked.connect(self.timer_sits)
        self.but3.clicked.connect(self.timer_final)
    

