import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap

class window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(100,100,400,300)
        self.setWindowTitle("imaging...!!")
        self.UI()

    def UI(self):
        self.image = QLabel(self)
        self.image.setPixmap(QPixmap('image/images.png'))
        self.image.move(50,50)
        showbutton=QPushButton("Show",self)
        showbutton.move(120,250)
        removebutton=QPushButton("Remove",self)
        removebutton.move(200,250)
        showbutton.clicked.connect(self.showfunc)
        removebutton.clicked.connect(self.removefunc)
        self.show()

    def removefunc(self):
        self.image.close()
    def showfunc(self):
        self.image.show()

def main():
    App = QApplication(sys.argv)
    Window = window()
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()