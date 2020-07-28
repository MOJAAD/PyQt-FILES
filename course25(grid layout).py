import sys
from PyQt5.QtWidgets import *

class window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(400,100,450,400)
        self.setWindowTitle("Grid Layout!")
        self.UI()

    def UI(self):
        self.gridlayout=QGridLayout()
        # btn1=QPushButton("BUTTON1",self)
        # btn2=QPushButton("BUTTON2",self)
        # btn3=QPushButton("BUTTON3",self)
        # btn4=QPushButton("BUTTON4",self)
        # self.gridlayout.addWidget(btn1,0,0)
        # self.gridlayout.addWidget(btn2,0,1)
        # self.gridlayout.addWidget(btn3,1,0)
        # self.gridlayout.addWidget(btn4,1,1)
        for i in range(0,3):
            for j in range(0,3):
                btn=QPushButton("Button {}{} ".format(i,j))
                self.gridlayout.addWidget(btn,i,j)
                btn.clicked.connect(self.clickme)


        self.setLayout(self.gridlayout)
        self.show()

    def clickme(self):
        buttonid=self.sender().text()
        #print(buttonid)
        print("you click {}".format(buttonid))


def main():
    App = QApplication(sys.argv)
    Window = window()
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()