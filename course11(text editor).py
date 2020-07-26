import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont

font=QFont('Times',14)

class window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(100,100,400,300)
        self.setWindowTitle("Text Editor...!!")
        self.UI()

    def UI(self):
        self.editor=QTextEdit(self)
        self.editor.move(50,50)
        self.editor.setAcceptRichText(False)
        button=QPushButton('CLICK HERE!',self)
        button.setFont(font)
        button.move(200,250)
        button.clicked.connect(self.getV)
        self.show()

    def getV(self):
        value=self.editor.toPlainText()
        print(value)

def main():
    App = QApplication(sys.argv)
    Window = window()
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()