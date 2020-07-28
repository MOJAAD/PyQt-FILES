import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon

class window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(400,100,450,400)
        self.setWindowTitle("Menu Widget!")
        self.UI()

    def UI(self):
        menubar=self.menuBar()
        file=menubar.addMenu('File')
        view=menubar.addMenu('View')
        code=menubar.addMenu('Code')
        helpe=menubar.addMenu('Help')

        new=QAction("New Project",self)
        new.setShortcut("ctrl+0")
        new.setIcon(QIcon("image/empty.png"))
        opene=QAction("Open Project",self)
        opene.setShortcut("ctrl+1")
        opene.setIcon(QIcon('image/folder.png'))
        savee=QAction("Save Project",self)
        savee.setShortcut("ctrl+2")
        savee.setIcon(QIcon('image/save.png'))
        exit=QAction("Exit",self)
        exit.setShortcut("ctrl+3")
        exit.setIcon(QIcon('image/exit.png'))
        exit.triggered.connect(self.exitfcn)
        file.addActions([new,opene,savee,exit])


        self.show()

    def exitfcn(self):
        mbox=QMessageBox.information(self,'Warning!','Are you sure?',QMessageBox.Yes|QMessageBox.No,QMessageBox.No)
        if mbox==QMessageBox.Yes:
            sys.exit()
    
def main():
    App = QApplication(sys.argv)
    Window = window()
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()