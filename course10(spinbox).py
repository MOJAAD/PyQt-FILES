import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont

font=QFont('Times',12)

class window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(100,100,400,300)
        self.setWindowTitle("Message Box...!!")
        self.UI()

    def UI(self):
        self.spinbox=QSpinBox(self)
        self.spinbox.setFont(font)
        self.spinbox.move(100,50)
        # self.spinbox.minimum(10)
        # self.spinbox.maximum(100)
        self.spinbox.setRange(10,100)
        # self.spinbox.setPrefix("$")
        self.spinbox.setSuffix(" Cm")
        self.spinbox.setSingleStep(2)
        #self.spinbox.valueChanged.connect(self.getV)
        button=QPushButton('CLICK HERE!',self)
        button.setFont(font)
        button.move(100,130)
        button.clicked.connect(self.getV)
        self.show()

    def getV(self):
        value=self.spinbox.value()
        print(value)

def main():
    App = QApplication(sys.argv)
    Window = window()
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()