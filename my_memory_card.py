#создай приложение для запоминания информации
from PyQt5.QtCore import Qt 
from PyQt5.QtWidgets import (
    QApplication, QWidget, QPushButton, QLabel, \
    QVBoxLayout, QRadioButton, QHBoxLayout, QGroupBox, QButtonGroup
)
from random import shuffle, randint

class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

question_list = []
question_list.append(Question('Что лучше против танка','faustpatron', 'MP-40', 'STG-44', 'MG-42'))
question_list.append(Question('Вопрос 2', 'Вариант 1', 'Вариант 2', 'Вариант 3', 'Вариант 4'))
question_list.append(Question('Вопрос 3', 'Вариант 1', 'Вариант 2', 'Вариант 3', 'Вариант 4'))
question_list.append(Question('Вопрос 4', 'Вариант 1', 'Вариант 2', 'Вариант 3', 'Вариант 4'))
question_list.append(Question('Вопрос 5', 'Вариант 1', 'Вариант 2', 'Вариант 3', 'Вариант 4'))
app = QApplication([])
window = QWidget()

window.setWindowTitle('Memory Card')
window.resize(400, 400)

'''Интерфейс'''
question = QLabel('Что лучше')
btn_ok = QPushButton('Ответить')
RadioGroupBox = QGroupBox("Варианты ответов")
rbtn_1 = QRadioButton('MP-40')
rbtn_2 = QRadioButton('STG-44')
rbtn_3 = QRadioButton('MG-42')
rbtn_4 = QRadioButton('faustpatron')

RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()

layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RadioGroupBox.setLayout(layout_ans1)

AnsGroupBox = QGroupBox('Результат текста')
lb_Result = QLabel('Правильно/Неправильно')
lb_Correct = QLabel('Ответ будет тут!')

layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)

layout_ans1 = QHBoxLayout()
layout_ans2 = QHBoxLayout()
layout_ans3 = QHBoxLayout()

layout_ans1.addWidget(question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_ans2.addWidget(RadioGroupBox)
layout_ans2.addWidget(AnsGroupBox)
AnsGroupBox.hide()

layout_ans3.addStretch(1)
layout_ans3.addWidget(btn_ok, stretch=2)
layout_ans3.addStretch(1)

layout_card = QVBoxLayout()
layout_card.addLayout(layout_ans1, stretch=2)
layout_card.addLayout(layout_ans2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_ans3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5)

window.setLayout(layout_card)

'''Функции'''

def show_question():
    AnsGroupBox.hide()
    RadioGroupBox.show()
    btn_ok.setText('Ответить')
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)


def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_ok.setText('Следующий вопрос')


answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]
def ask(q):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    question.setText(q.question)
    lb_Correct.setText(q.right_answer)
    show_question()

def show_correct(res):
    lb_Result.setText(res)
    show_result()

def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно!')
        window.score += 1
        print('Статистика\n-Всего вопросов: ', window.total, '\n-Правильных ответо: ', window.score)
        print('Рейтинг: ', (window.score/window.total*100), '%')
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Неправильно!')
            print('Рейтинг: ', (window.score/window.total*100), '%')

def next_question():
    cur_question = randint(0, len(question_list)-1)
    window.total += 1
    print('Статистика\n-Всего вопросов: ', window.total, '\n-Правильных ответо: ', window.score)
    q = question_list[cur_question]
    ask(q)

def click_OK():
    if btn_ok.text() == 'Ответить':
        check_answer()
    else:
        next_question()

btn_ok.clicked.connect(click_OK)
window.score = 0
window.total = 0
next_question()
window.show()
app.exec_()