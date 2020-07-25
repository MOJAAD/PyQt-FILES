import sys
from PyQt5.QtWidgets import *

class window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(100,100,400,300)
        self.setWindowTitle("combobox...!!")
        self.UI()

    def UI(self):
        self.combo=QComboBox(self)
        self.combo.move(170,20)
        save=QPushButton('Save',self)
        save.move(170,40)
        save.clicked.connect(self.savefunc)
        self.combo.addItems(['C','C#','Python','Matlab','Js'])
        list1=['a','b','c','d','e','f','g','h','i','j','k','l']
        for name in list1:
            self.combo.addItem(name)
        for number in range(1,50):
            self.combo.addItem(str(number))
        self.show()

    def savefunc(self):
        value=self.combo.currentText()
        print(value)

def main():
    App = QApplication(sys.argv)
    Window = window()
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()