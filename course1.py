import sys
from PyQt5.QtWidgets import *

class window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(150,150,400,450)
        self.setWindowTitle("this is my first window!!")

        self.show()

App=QApplication(sys.argv)
window=window()
sys.exit(App.exec_())
