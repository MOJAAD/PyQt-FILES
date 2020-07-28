import sys
from PyQt5.QtWidgets import *

class window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(400,100,450,400)
        self.setWindowTitle("File Dialogs!")
        self.UI()

    def UI(self):
        vbox=QVBoxLayout()
        hbox=QHBoxLayout()
        self.editor=QTextEdit()
        filebutton=QPushButton("open file",self)
        fontbutton=QPushButton("Change Font",self)
        colorbutton=QPushButton("Change Color",self)
        filebutton.clicked.connect(self.openfile)
        fontbutton.clicked.connect(self.changefont)
        colorbutton.clicked.connect(self.changecolor)
        vbox.addWidget(self.editor)
        vbox.addLayout(hbox)
        hbox.addStretch()
        hbox.addWidget(fontbutton)
        hbox.addWidget(filebutton)
        hbox.addWidget(colorbutton)
        hbox.addStretch()
        
        self.setLayout(vbox)
        self.show()

    def changefont(self):
        font,ok = QFontDialog.getFont()
        if ok:
            self.editor.setCurrentFont(font)

    def changecolor(self):
        color = QColorDialog.getColor()
        self.editor.setTextColor(color)

    def openfile(self):
        url = QFileDialog.getOpenFileName(self,"Open a file","","All Files(*);;*txt")
        urll=url[0]
        print(url)
        file=open(urll,'r')
        content=file.read()
        self.editor.setText(content)

    
def main():
    App = QApplication(sys.argv)
    Window = window()
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()