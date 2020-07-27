import sys
from PyQt5.QtWidgets import *

class window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(400,100,250,200)
        self.setWindowTitle("Vertical and Horizontal box!")
        self.UI()

    def UI(self):
        formlayout=QFormLayout()
        #formlayout.setRowWrapPolicy(QFormLayout.WrapAllRows)
        name_txt=QLabel("Name: ",self)
        namebox=QHBoxLayout()
        namebox.addWidget(QLineEdit())
        namebox.addWidget(QLineEdit())
        pass_txt=QLabel("Password: ",self)
        pass_input=QLineEdit()
        hbox=QHBoxLayout() 
        hbox.addStretch()
        hbox.addWidget(QPushButton("Enter"))
        hbox.addWidget(QPushButton("Exit"))
        formlayout.addRow(name_txt,namebox)
        formlayout.addRow(pass_txt,pass_input)
        formlayout.addRow(QLabel("Country :"),QComboBox())
        formlayout.addRow(hbox)

        self.setLayout(formlayout)

        self.show()



def main():
    App = QApplication(sys.argv)
    Window = window()
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()