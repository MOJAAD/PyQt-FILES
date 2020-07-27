import sys
from PyQt5.QtWidgets import *

class window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(400,100,450,400)
        self.setWindowTitle("Horizontal box!")
        self.UI()

    def UI(self):
        hbox=QHBoxLayout()
        btn1=QPushButton("button1",self)
        btn2=QPushButton("button2")
        btn3=QPushButton("button3")
        hbox.addStretch()
        hbox.addWidget(btn1)
        hbox.addWidget(btn2)
        hbox.addWidget(btn3)
        hbox.addStretch()
        self.setLayout(hbox)
        self.show()



def main():
    App = QApplication(sys.argv)
    Window = window()
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()