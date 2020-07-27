import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(400,100,250,200)
        self.setWindowTitle("slider box!")
        self.UI()

    def UI(self):
        vbox=QVBoxLayout()
        self.slider=QSlider(Qt.Horizontal)
        self.slider.setMinimum(10)
        self.slider.setMaximum(100)
        self.slider.setTickPosition(QSlider.TicksAbove)
        # self.slider.setTickInterval(10)
        self.slider.valueChanged.connect(self.getV)
        self.text1=QLabel("0")
        self.text1.setAlignment(Qt.AlignCenter)
        self.text2=QLabel("Hello Python!")
        vbox.addStretch()
        vbox.addWidget(self.text1)
        vbox.addWidget(self.text2)
        vbox.addWidget(self.slider)
        self.setLayout(vbox)

        self.show()

    def getV(self):
        self.val=self.slider.value()
        #print(self.val)
        self.text1.setText(str(self.val))
        self.font=QFont("Times",self.val)
        self.text2.setFont(self.font)

def main():
    App = QApplication(sys.argv)
    Window = window()
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()