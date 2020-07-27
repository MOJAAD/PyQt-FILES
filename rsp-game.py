import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui  import QFont,QPixmap

score  = QFont("Times",14)
button = QFont("Arial",12)

class window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(400,100,600,400)
        self.setWindowTitle("RSP-GAME!")
        self.UI()

    def UI(self):
        self.computerscore=QLabel("Computer Score : ",self)
        self.userscore=QLabel("  User  Score  : ",self)
        self.computerscore.move(30,20)
        self.userscore.move(300,20)
        self.computerscore.setFont(score)
        self.userscore.setFont(score)

        self.computerside=QLabel(self)
        self.computerside.setPixmap(QPixmap('image/rock.png'))
        self.computerside.move(20,100)
        self.vs=QLabel(self)
        self.vs.setPixmap(QPixmap('image/game.png'))
        self.vs.move(210,150)
        self.userside=QLabel(self)
        self.userside.setPixmap(QPixmap('image/rock.png'))
        self.userside.move(300,100)

        self.show()

def main():
    App = QApplication(sys.argv)
    Window = window()
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()