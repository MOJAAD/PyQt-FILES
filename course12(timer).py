import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QTimer

class window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(100,100,400,300)
        self.setWindowTitle("Timer widget...!!")
        self.UI()

    def UI(self):
        self.colorlabel=QLabel(self)
        self.colorlabel.resize(200,200)
        self.colorlabel.move(55,50)
        self.colorlabel.setStyleSheet("background-color:red")
        #######################################################
        button1=QPushButton('Start!',self)
        button1.move(52,250)
        button1.clicked.connect(self.getV)
        button2=QPushButton('Stop!',self)
        button2.move(180,250)
        button2.clicked.connect(self.getV2)
        #######################################################
        self.timer=QTimer()
        self.timer.setInterval(1000)
        self.value=0
        self.timer.timeout.connect(self.changing)
        self.show()

    def changing(self):
        if self.value==0:
            self.colorlabel.setStyleSheet("background-color:yellow")
            self.value=1
        else:
            self.colorlabel.setStyleSheet("background-color:green")
            self.value=0
    def getV(self):
        self.timer.start()
    def getV2(self):
        self.timer.stop()

def main():
    App = QApplication(sys.argv)
    Window = window()
    Window.getV()
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()