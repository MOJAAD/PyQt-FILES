import sys
from PyQt5.QtWidgets import *

class window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(100,100,400,400)
        self.setWindowTitle('cheking for buttons...')
        self.UI()

    def UI(self):
        self.text=QLabel('My first button!',self)
        enterbutton=QPushButton('Enter!',self)
        exitbutton=QPushButton('Exit!',self)
        self.text.move(100,50)
        enterbutton.move(50,80)
        exitbutton.move(150,80)
        enterbutton.clicked.connect(self.enterfunc)
        exitbutton.clicked.connect(self.exitfunc)
        self.show()

    def enterfunc(self):
        self.text.setText('you clicked enter button !')
        self.text.resize(160,20)
    def exitfunc(self):
        self.text.setText('you clicked exit button !')
        self.text.resize(160,20)  
def main():
    App=QApplication(sys.argv)
    Window=window()
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()