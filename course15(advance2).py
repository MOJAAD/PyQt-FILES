import sys
from PyQt5.QtWidgets import *

class window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(400,100,450,400)
        self.setWindowTitle("Vertical box!")
        self.UI()

    def UI(self):
        vbox=QVBoxLayout()
        btn1=QPushButton("add",self)
        btn2=QPushButton("delete")
        btn3=QPushButton("exit")
        vbox.addStretch()
        vbox.addWidget(btn1)
        vbox.addWidget(btn2)
        vbox.addWidget(btn3)
        vbox.addStretch()
        self.setLayout(vbox)
        self.show()



def main():
    App = QApplication(sys.argv)
    Window = window()
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()