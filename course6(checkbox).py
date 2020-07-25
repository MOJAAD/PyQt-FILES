import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap

class window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(100,100,400,300)
        self.setWindowTitle("checkboxes...!!")
        self.UI()

    def UI(self):
        self.username=QLineEdit(self)
        self.username.setPlaceholderText('enter username')
        self.username.move(150,20)
        self.password=QLineEdit(self)
        self.password.setPlaceholderText('enter password')
        self.password.move(150,40)
        self.remember=QCheckBox('Remember Me!',self)
        self.remember.move(150,60)
        subbutton=QPushButton('Submit',self)
        subbutton.move(200,80)
        subbutton.clicked.connect(self.submit)
        self.show()

    def submit(self):
        if (self.remember.isChecked()):
            print('OK i remember '+self.username+' and '+self.password)
        else:
            print('OK i dont remember!')

def main():
    App = QApplication(sys.argv)
    Window = window()
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()