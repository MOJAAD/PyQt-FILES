import sys
from PyQt5.QtWidgets import *

class window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(100,100,300,300)
        self.setWindowTitle("textbox!!!")
        self.UI()

    def UI(self):
        self.textbox1=QLineEdit(self)
        self.textbox1.setPlaceholderText('enter username')
        self.textbox1.move(100,50)
        self.textbox2=QLineEdit(self)
        self.textbox2.setPlaceholderText('enter password')
        self.textbox2.setEchoMode(QLineEdit.Password)
        self.textbox2.move(100,80)
        enterbutton=QPushButton('Enter',self)
        enterbutton.move(130,110)
        enterbutton.clicked.connect(self.getV)
        self.show()

    def getV(self):
        self.username=self.textbox1.text()
        self.password=self.textbox2.text()
        print('The user name is:',self.username,'\nThe password is:',self.password)
        self.setWindowTitle('user: '+self.username+'|pass: '+self.password)

def main():
    App = QApplication(sys.argv)
    Window = window()
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()