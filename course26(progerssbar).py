import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QTimer

count = 0

class window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(400,100,450,400)
        self.setWindowTitle("Progress Widget!")
        self.UI()

    def UI(self):
        vbox=QVBoxLayout()
        hbox=QHBoxLayout()
        self.progressbar=QProgressBar()
        btn1=QPushButton("Start",self)
        btn1.clicked.connect(self.startfcn)
        btn2=QPushButton("Stop",self)
        btn2.clicked.connect(self.stopfcn)
        self.timer=QTimer()
        self.timer.setInterval(100)
        self.timer.timeout.connect(self.runprog)
        vbox.addWidget(self.progressbar)
        vbox.addLayout(hbox)
        hbox.addWidget(btn1)
        hbox.addWidget(btn2)
        self.setLayout(vbox)
        self.show()

    def startfcn(self):
        self.timer.start()

    def stopfcn(self):
        self.timer.stop()

    def runprog(self):
        global count
        count +=1
        print(count)
        self.progressbar.setValue(count)
        if count==100:
            self.timer.stop()

def main():
    App = QApplication(sys.argv)
    Window = window()
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()