import sys
from PyQt5.QtWidgets import *

class window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(100,100,400,300)
        self.setWindowTitle("Radio Buttons...!!")
        self.UI()

    def UI(self):
        self.username=QLineEdit(self)
        self.username.setPlaceholderText('enter username')
        self.username.move(150,20)
        self.password=QLineEdit(self)
        self.password.setPlaceholderText('enter password')
        self.password.setEchoMode(QLineEdit.Password)
        self.password.move(150,40)
        self.male=QRadioButton("Male",self)
        self.male.move(150,60)
        self.male.setChecked(True)
        self.female=QRadioButton('Female',self)
        self.female.move(200,60)
        button=QPushButton('save',self)
        button.move(160,100)
        button.clicked.connect(self.getV)
        self.show()

    def getV(self):
        self.name=self.username.text()
        self.passw=self.password.text()
        if self.male.isChecked():
            print(self.name+' '+self.passw+' you are male')
        else:
            print(self.name+' '+self.passw+' you are female')
def main():
    App = QApplication(sys.argv)
    Window = window()
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()