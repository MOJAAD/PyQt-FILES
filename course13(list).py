import sys
from PyQt5.QtWidgets import *

class window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(100,100,400,400)
        self.setWindowTitle("list widget...!!")
        self.UI()

    def UI(self):
        self.line=QLineEdit(self)
        self.line.move(50,20)
        self.list1=QListWidget(self)
        self.list1.move(50,50)

        button1=QPushButton('Add',self)
        button1.move(320,50)
        button1.clicked.connect(self.add)
        
        button2=QPushButton('Delete',self)
        button2.move(320,80)
        button2.clicked.connect(self.delete)
        
        button3=QPushButton('Go Item',self)
        button3.move(320,110)
        button3.clicked.connect(self.goitem)
    
        button4=QPushButton('Delete All',self)
        button4.move(320,140)
        button4.clicked.connect(self.deleteall)
        
        self.show()

    def add(self):
        self.adding=self.line.text()
        self.list1.addItem(self.adding)
        self.line.setText("")
    def delete(self):
        self.id=self.list1.currentRow()
        print(self.id)
        self.list1.takeItem(self.id)
    def goitem(self):
        self.id=self.list1.currentRow()
        print(self.id)
    def deleteall(self):
        self.list1.clear()
    
def main():
    App = QApplication(sys.argv)
    Window = window()
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()