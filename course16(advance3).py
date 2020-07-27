import sys
from PyQt5.QtWidgets import *

class window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(400,100,450,400)
        self.setWindowTitle("Vertical and Horizontal box!")
        self.UI()

    def UI(self):
        mainbox=QVBoxLayout()
        explainbox=QHBoxLayout()
        buttombox=QHBoxLayout()
        mainbox.addLayout(explainbox)
        mainbox.addLayout(buttombox)

        chbox=QCheckBox()
        rbbox=QRadioButton()
        combox=QComboBox()
        btnbox1=QPushButton()
        btnbox2=QPushButton()
        explainbox.setContentsMargins(15,10,10,10) #left,top,right,buttom
        explainbox.addWidget(chbox)
        explainbox.addWidget(rbbox)
        explainbox.addWidget(combox)
        buttombox.setContentsMargins(150,10,100,100)
        buttombox.addWidget(btnbox1)
        buttombox.addWidget(btnbox2)

        self.setLayout(mainbox)
        
        self.show()



def main():
    App = QApplication(sys.argv)
    Window = window()
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()