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
        button=QPushButton('CLICK HERE!',self)
        button.setFont(font)
        button.move(160,100)
        button.clicked.connect(self.messagebox)
        self.show()

    def messagebox(self):
        # mbox=QMessageBox.question(self,'Warning!','Are you sure to exit?',QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel,QMessageBox.No)
        # if mbox==QMessageBox.Yes:
        #     sys.exit()
        # else :
        #     pass
        mbox=QMessageBox.information(self,'Information','You did it dude!')

def main():
    App = QApplication(sys.argv)
    Window = window()
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()