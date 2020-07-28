import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(400,100,450,400)
        self.setWindowTitle("Table Widget!")
        self.UI()

    def UI(self):
        vbox=QVBoxLayout()
        self.table=QTableWidget()
        self.table.setRowCount(2)
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderItem(0,QTableWidgetItem("Firstname"))
        self.table.setHorizontalHeaderItem(1,QTableWidgetItem("Lastname"))
        self.table.setHorizontalHeaderItem(2,QTableWidgetItem("Address"))
        # self.table.horizontalHeader().hide()
        # self.table.verticalHeader().hide()
        self.table.setItem(0,0,QTableWidgetItem('blackheart'))
        self.table.setItem(0,1,QTableWidgetItem('km'))
        self.table.setItem(0,2,QTableWidgetItem('021'))
        self.table.setItem(1,0,QTableWidgetItem('mojaad'))
        self.table.setItem(1,1,QTableWidgetItem('--'))
        self.table.setItem(1,2,QTableWidgetItem('031'))
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table.doubleClicked.connect(self.doubleV)
        btn=QPushButton("Get")
        vbox.addWidget(self.table)
        vbox.addWidget(btn)
        btn.clicked.connect(self.getV)
        self.setLayout(vbox)
        self.show()

    def doubleV(self):
        for item in self.table.selectedItems():
            print(item.text(),item.row(),item.column())

    def getV(self):
        for item in self.table.selectedItems():
            print(item.text(),item.row(),item.column())
    
def main():
    App = QApplication(sys.argv)
    Window = window()
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()