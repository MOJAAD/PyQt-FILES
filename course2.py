import sys
from PyQt5.QtWidgets import *

class window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(100,100,300,300)
        self.setWindowTitle("this is my second window!!")
        self.UI()

    def UI(self):
        text1=QLabel("\n\n\n\t\tHello user!",self)
        self.show()

def main():
    App = QApplication(sys.argv)
    Window = window()
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()