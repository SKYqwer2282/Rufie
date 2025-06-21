from instr import *
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QVBoxLayout)
from PyQt5.QtCore import Qt

class FinalWin(QWidget):
    def __init__(self, exp):
        super().__init__()
        self.exp = exp
        self.index = self.calculate_index()  
        self.initUI()
        self.set_appear()
        self.show()
        
    def calculate_index(self):
        
        return (4 * (int(self.exp.t1) + int(self.exp.t2) + int(self.exp.t3)) - 200) / 10
        
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
        
    def get_result_text(self):
    # Для возраста 15 лет и старше
        if self.exp.age >= 15:
            if self.index >= 15:
                return txt_res1  # Низкий
            elif 11 <= self.index < 15:
                return txt_res2  # Удовлетворительный
            elif 6 <= self.index < 11:
                return txt_res3  # Средний
            elif 0.5 <= self.index < 6:
                return txt_res4  # Выше среднего
            else:
                return txt_res5  # Высокий
        
        # Для возраста 13-14 лет
        elif 13 <= self.exp.age <= 14:
            if self.index >= 16.5:
                return txt_res1  # Низкий
            elif 12.5 <= self.index < 16.5:
                return txt_res2  # Удовлетворительный
            elif 7.5 <= self.index < 12.5:
                return txt_res3  # Средний
            elif 2 <= self.index < 7.5:
                return txt_res4  # Выше среднего
            else:
                return txt_res5  # Высокий
        
        # Для возраста 11-12 лет
        elif 11 <= self.exp.age <= 12:
            if self.index >= 18:
                return txt_res1  # Низкий
            elif 14 <= self.index < 18:
                return txt_res2  # Удовлетворительный
            elif 9 <= self.index < 14:
                return txt_res3  # Средний
            elif 3.5 <= self.index < 9:
                return txt_res4  # Выше среднего
            else:
                return txt_res5  # Высокий
        
        # Для возраста 9-10 лет
        elif 9 <= self.exp.age <= 10:
            if self.index >= 19.5:
                return txt_res1  # Низкий
            elif 15.5 <= self.index < 19.5:
                return txt_res2  # Удовлетворительный
            elif 10.5 <= self.index < 15.5:
                return txt_res3  # Средний
            elif 5 <= self.index < 10.5:
                return txt_res4  # Выше среднего
            else:
                return txt_res5  # Высокий
        
        # Для возраста 7-8 лет
        elif 7 <= self.exp.age <= 8:
            if self.index >= 21:
                return txt_res1  # Низкий
            elif 17 <= self.index < 21:
                return txt_res2  # Удовлетворительный
            elif 12 <= self.index < 17:
                return txt_res3  # Средний
            elif 6.5 <= self.index < 12:
                return txt_res4  # Выше среднего
            else:
                return txt_res5  # Высокий
    
    # Для других возрастов (если вдруг введен возраст меньше 7)
        else:
            return "Возраст не соответствует допустимому диапазону (7+ лет)"
        
    def initUI(self):
        self.work_index = QLabel(txt_index + str(round(self.index, 2)))
        self.work_heart = QLabel(txt_workheart + self.get_result_text())
        
        self.line = QVBoxLayout()
        self.line.addWidget(self.work_index, alignment=Qt.AlignCenter)
        self.line.addWidget(self.work_heart, alignment=Qt.AlignCenter)
        
        self.setLayout(self.line)
