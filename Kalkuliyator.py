from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, QLineEdit, QTextEdit)
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt
from time import sleep
import sys

st = ""


def os():
    global st
    st = ""
    kiritish.clear()


def jami():
    global st
    expression = st
    try:
        result = eval(expression.replace('÷', '/'))
        kiritish.setText(str(result))
    except Exception as e:
        kiritish.setText("error")


def f_nol():
    AC.setText("C")
    global st
    st += '0'
    kiritish.setText(st)


def f_bir():
    global st
    AC.setText("C")
    st += '1'
    kiritish.setText(st)


def f_ikki():
    global st
    AC.setText("C")
    st += '2'
    kiritish.setText(st)


def f_uch():
    global st
    st += '3'
    AC.setText("C")
    kiritish.setText(st)


def f_tort():
    global st
    AC.setText("C")
    st += '4'
    kiritish.setText(st)


def f_besh():
    AC.setText("C")
    global st
    st += '5'
    kiritish.setText(st)


def f_olti():
    AC.setText("C")
    global st
    st += '6'
    kiritish.setText(st)


def f_yetti():
    AC.setText("C")
    global st
    st += '7'
    kiritish.setText(st)


def f_sakkiz():
    AC.setText("C")
    global st
    st += '8'
    kiritish.setText(st)


def f_toqqiz():
    AC.setText("C")
    global st
    st += '9'
    kiritish.setText(st)


def f_foiz():
    AC.setText("C")
    global st
    st += '%'
    kiritish.setText(st)


def manfiy():
    global st
    if st in '+' or '-' or '*' or '%' or '÷':
        st = '' + st
    else:
        st = '-' + st
    kiritish.setText(st)


a = QFont()
a.setPixelSize(45)
a.setFamily("Arial")
app = QApplication(sys.argv)
win = QWidget()

q = QFont()
q.setPixelSize(50)

kiritish = QLineEdit(win)
kiritish.move(20, 100)
kiritish.setPlaceholderText(st)
kiritish.setFont(q)
kiritish.setStyleSheet("color: white; border: 3 solid white; border-radius: 10")
kiritish.setAlignment(Qt.AlignRight)

kiritish.setFixedWidth(405)


def All_Qaytar():
    teng.setStyleSheet("color:white; background-color: #faa907; border-radius: 48px")
    plus.setStyleSheet("color:white; background-color: #faa907; border-radius: 48px")
    minus.setStyleSheet("color:white; background-color: #faa907; border-radius: 48px")
    kopaytiruv.setStyleSheet("color:white; background-color: #faa907; border-radius: 48px")
    bolish.setStyleSheet("color: white; background-color: #faa907; border-radius: 48px")


def teng_ozgartir():
    All_Qaytar()
    teng.setStyleSheet("color: #faa907; background-color: white; border-radius: 48px")


def plus_ozgartir():
    global st
    st += '+'
    kiritish.setText(st)
    All_Qaytar()
    plus.setStyleSheet("color: #faa907; background-color: white; border-radius: 48px")


def minus_ozgartir():
    All_Qaytar()
    minus.setStyleSheet("color: #faa907; background-color: white; border-radius: 48px")
    global st
    st += '-'
    kiritish.setText(st)


def kop_ozgartir():
    global st
    st += '*'
    kiritish.setText(st)
    All_Qaytar()
    kopaytiruv.setStyleSheet("color: #faa907; background-color: white; border-radius: 48px")


def bolish_ozgartir():
    global st
    st += '÷'
    kiritish.setText(st)
    All_Qaytar()
    bolish.setStyleSheet("color: #faa907; background-color: white; border-radius: 48px")


def f_belgi():
    global st
    st += '.'
    kiritish.setText(st)


b = QFont()
b.setPixelSize(60)
b.setFamily("Arial")

win.setStyleSheet("background-color: black")
win.setWindowTitle("Calculator")
win.setWindowIcon(QIcon("pyqt5//pyqt5//image.png"))
win.setGeometry(1000, 300, 450, 700)

nol = QPushButton("0       ", win)
nol.move(5, 600)
nol.setStyleSheet("color:white; background-color: #2b2e33; border-radius: 48px; QPushButton : ")
nol.setFixedSize(200, 96)
nol.setFont(a)
nol.clicked.connect(f_nol)
nol.overrideWindowFlags(nol.windowFlags())
nol.setCursor(Qt.PointingHandCursor)

belgi = QPushButton(",", win)
belgi.setStyleSheet("color:white; background-color: #2b2e33; border-radius: 48px")
belgi.setFont(a)
belgi.setFixedSize(96, 96)
belgi.move(215, 600)
belgi.setCursor(Qt.PointingHandCursor)
belgi.clicked.connect(f_belgi)

teng = QPushButton("=", win)
teng.setStyleSheet("color:white; background-color: #faa907; border-radius: 48px")
teng.setFont(a)
teng.setFixedSize(96, 96)
teng.move(330, 600)
teng.setCursor(Qt.PointingHandCursor)
teng.clicked.connect(teng_ozgartir)
teng.clicked.connect(jami)

bir = QPushButton("1", win)
bir.setStyleSheet("color:white; background-color: #2b2e33; border-radius: 48px")
bir.setFont(a)
bir.setFixedSize(96, 96)
bir.move(5, 495)
bir.setCursor(Qt.PointingHandCursor)
bir.clicked.connect(f_bir)

ikki = QPushButton("2", win)
ikki.setStyleSheet("color:white; background-color: #2b2e33; border-radius: 48px")
ikki.setFont(a)
ikki.setFixedSize(96, 96)
ikki.move(110, 495)
ikki.setCursor(Qt.PointingHandCursor)
ikki.clicked.connect(f_ikki)

uch = QPushButton("3", win)
uch.setStyleSheet("color:white; background-color: #2b2e33; border-radius: 48px")
uch.setFont(a)
uch.setFixedSize(96, 96)
uch.move(215, 495)
uch.setCursor(Qt.PointingHandCursor)
uch.clicked.connect(f_uch)

plus = QPushButton("+", win)
plus.setStyleSheet("color:white; background-color: #faa907; border-radius: 48px")
plus.setFont(a)
plus.setFixedSize(96, 96)
plus.move(330, 495)
plus.setCursor(Qt.PointingHandCursor)
plus.clicked.connect(plus_ozgartir)

tort = QPushButton("4", win)
tort.setStyleSheet("color:white; background-color: #2b2e33; border-radius: 48px")
tort.setFont(a)
tort.setFixedSize(96, 96)
tort.move(5, 390)
tort.setCursor(Qt.PointingHandCursor)
tort.clicked.connect(f_tort)

besh = QPushButton("5", win)
besh.setStyleSheet("color:white; background-color: #2b2e33; border-radius: 48px")
besh.setFont(a)
besh.setFixedSize(96, 96)
besh.move(110, 390)
besh.setCursor(Qt.PointingHandCursor)
besh.clicked.connect(f_besh)

olti = QPushButton("6", win)
olti.setStyleSheet("color:white; background-color: #2b2e33; border-radius: 48px")
olti.setFont(a)
olti.setFixedSize(96, 96)
olti.move(215, 390)
olti.setCursor(Qt.PointingHandCursor)
olti.clicked.connect(f_olti)

minus = QPushButton("-", win)
minus.setStyleSheet("color:white; background-color: #faa907; border-radius: 48px")
minus.setFont(a)
minus.setFixedSize(96, 96)
minus.move(330, 390)
minus.setCursor(Qt.PointingHandCursor)
minus.clicked.connect(minus_ozgartir)

yetti = QPushButton("7", win)
yetti.setStyleSheet("color:white; background-color: #2b2e33; border-radius: 48px")
yetti.setFont(a)
yetti.setFixedSize(96, 96)
yetti.move(5, 284)
yetti.setCursor(Qt.PointingHandCursor)
yetti.clicked.connect(f_yetti)

sakkiz = QPushButton("8", win)
sakkiz.setStyleSheet("color:white; background-color: #2b2e33; border-radius: 48px")
sakkiz.setFont(a)
sakkiz.setFixedSize(96, 96)
sakkiz.move(110, 284)
sakkiz.setCursor(Qt.PointingHandCursor)
sakkiz.clicked.connect(f_sakkiz)

toqqiz = QPushButton("9", win)
toqqiz.setStyleSheet("color:white; background-color: #2b2e33; border-radius: 48px")
toqqiz.setFont(a)
toqqiz.setFixedSize(96, 96)
toqqiz.move(215, 284)
toqqiz.setCursor(Qt.PointingHandCursor)
toqqiz.clicked.connect(f_toqqiz)

kopaytiruv = QPushButton("×", win)
kopaytiruv.setStyleSheet("color:white; background-color: #faa907; border-radius: 48px")
kopaytiruv.setFont(a)
kopaytiruv.setFixedSize(96, 96)
kopaytiruv.move(330, 284)
kopaytiruv.setCursor(Qt.PointingHandCursor)
kopaytiruv.clicked.connect(kop_ozgartir)

AC = QPushButton("AC", win)
AC.setStyleSheet("color:white; background-color: #2b2e33; border-radius: 48px")
AC.setFont(a)
AC.setFixedSize(96, 96)
AC.move(5, 180)
AC.setCursor(Qt.PointingHandCursor)
AC.clicked.connect(os)

plus_minus = QPushButton("+/-", win)
plus_minus.setStyleSheet("color:white; background-color: #2b2e33; border-radius: 48px")
plus_minus.setFont(a)
plus_minus.setFixedSize(96, 96)
plus_minus.move(110, 180)
plus_minus.setCursor(Qt.PointingHandCursor)
plus_minus.clicked.connect(manfiy)

foiz = QPushButton("%", win)
foiz.setStyleSheet("color:white; background-color: #2b2e33; border-radius: 48px")
foiz.setFont(a)
foiz.setFixedSize(96, 96)
foiz.move(215, 180)
foiz.setCursor(Qt.PointingHandCursor)
foiz.clicked.connect(f_foiz)

bolish = QPushButton("÷", win)
bolish.setStyleSheet("color: white; background-color: #faa907; border-radius: 48px")
bolish.setFont(a)
bolish.setFixedSize(96, 96)
bolish.move(330, 180)
bolish.setCursor(Qt.PointingHandCursor)
bolish.clicked.connect(bolish_ozgartir)


def ozgartirish():
    button = win.sender()
    button.setStyleSheet('color: black; background-color: #7a7a78; border-radius: 45')


def qaytar():
    button = win.sender()
    button.setStyleSheet('color: white; background-color: #2b2e33; border-radius: 45')


lst = [nol, toqqiz, sakkiz, yetti, olti, besh, tort, uch, ikki, bir, belgi, AC, plus_minus, foiz]
for i in lst:
    i.pressed.connect(ozgartirish)
    i.released.connect(qaytar)

win.show()
sys.exit(app.exec_())
