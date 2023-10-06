#создай приложение для запоминания информацииrom PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
# главное окно: 
app = QApplication([])
my_win = QWidget() 
my_win.setWindowTitle('Лотерея') 
my_win.move(100, 100) 
my_win.resize(400, 200) 
text = QLabel('Какой национальности не существует?')
answer =QPushButton('Ответить')
RadioGroupBox = QGroupBox('Варианты ответов')

rbtn_1 = QRadioButton('Энцы')
rbtn_2 = QRadioButton('Смурфы')
rbtn_3 = QRadioButton('Чулымцы')
rbtn_4 = QRadioButton('Алеуты')

layout_ans1 =QHBoxLayout()
layout_ans2 =QHBoxLayout()
layout_ans3 =QHBoxLayout()

layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)
layout_ans3.addLayout(layout_ans2)
layout_ans3.addLayout(layout_ans3)

main_line_2.addWiget(text, alinment = Qt.AlignCenter)
main_line_4.addWiget(answer, stretch = 2)
line_ans2,addWidget(answer_1, alignment = Qt.AlignCenter)
line_ans2,addWidget(answer_2, alignment = Qt.AlignCenter)
line_ans3,addWidget(answer_3, alignment = Qt.AlignCenter)
line_ans3,addWidget(answer_4, alignment = Qt.AlignCenter)




RadioGroupBox.setLayout(layout_ans1)
my_win.show()
app.exec_()