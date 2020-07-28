import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(400,100,450,400)
        self.setWindowTitle("Tab Widget!")
        self.UI()

    def UI(self):
        mainlayout=QVBoxLayout()
        self.tabs=QTabWidget()
        self.tab1=QWidget()
        self.tab2=QWidget()
        self.tab3=QWidget()
        self.tabs.addTab(self.tab1,"tab 1")
        self.tabs.addTab(self.tab2,"tab 2")
        self.tabs.addTab(self.tab3,"tab 3")

        vbox=QVBoxLayout()
        hbox=QHBoxLayout()
        self.txt=QLabel('hello python')
        self.btn1=QPushButton("click1")
        self.btn1.clicked.connect(self.getV)
        self.btn2=QPushButton("click2")
        vbox.addWidget(self.txt)
        vbox.addWidget(self.btn1)
        hbox.addWidget(self.btn2)
        self.tab1.setLayout(vbox)
        self.tab2.setLayout(hbox)

        mainlayout.addWidget(self.tabs)
        self.setLayout(mainlayout)
        self.show()

    def getV(self):
        self.txt.setText("ACTIVATED!")
    
def main():
    App = QApplication(sys.argv)
    Window = window()
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()