import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

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

        tbar=self.addToolBar("toolbar1")
        tbar.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        newtb=QAction(QIcon('image/empty.png'),"New Project",self)
        opentb=QAction(QIcon('image/folder.png'),"Open Project",self)
        savetb=QAction(QIcon('image/save.png'),"Save Projcet",self)
        tbar.addActions([newtb,savetb,opentb])
        tbar.actionTriggered.connect(self.btnfcn)
        self.combo=QComboBox()
        self.combo.addItems(['black','white','green','red','blue'])
        tbar.addWidget(self.combo)
        self.show()

    def btnfcn(self,button):
        if button.text()=="New Project":
            print("you clicked new!")
        elif button.text()=="Open Project":
            print("you clicked open!")
        elif button.text()=="Save Projcet":
            print("you clicked save!")

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