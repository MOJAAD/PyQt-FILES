import sys
from PyQt5.QtWidgets import *

class window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(300,300,600,600)
        self.setWindowTitle("RSP-GAME!")
        self.UI()

    def UI(self):
        



        self.show()

def main():
    App = QApplication(sys.argv)
    Window = window()
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()