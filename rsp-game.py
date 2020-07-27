import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui     import QFont,QPixmap
from PyQt5.QtCore    import QTimer
from random          import randint

score  = QFont("Times",14)
button = QFont("Arial",12)
computerscore = 0
userscore    = 0

class window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(400,100,450,400)
        self.setWindowTitle("RSP-GAME!")
        self.UI()

    def UI(self):
        self.computerscoretext=QLabel("Computer Score :  ",self)
        self.userscoretext=QLabel("  User  Score  :  ",self)
        self.computerscoretext.move(30,20)
        self.userscoretext.move(270,20)
        self.computerscoretext.setFont(score)
        self.userscoretext.setFont(score)

        self.computerside=QLabel(self)
        self.computerside.setPixmap(QPixmap('image/rock.png'))
        self.computerside.move(20,100)
        self.vs=QLabel(self)
        self.vs.setPixmap(QPixmap('image/game.png'))
        self.vs.move(210,150)
        self.userside=QLabel(self)
        self.userside.setPixmap(QPixmap('image/rock.png'))
        self.userside.move(300,100)

        self.startbutton=QPushButton('Start',self)
        self.startbutton.setFont(button)
        self.startbutton.move(140,250)
        self.startbutton.clicked.connect(self.startgame)
        self.stopbutton=QPushButton('Stop',self)
        self.stopbutton.setFont(button)
        self.stopbutton.move(240,250)
        self.stopbutton.clicked.connect(self.stopgame)
        self.exitbutton=QPushButton('Exit',self)
        self.exitbutton.setFont(button)
        self.exitbutton.move(190,280)
        self.exitbutton.clicked.connect(self.exitgame)

        self.timer=QTimer(self)
        self.timer.setInterval(90)
        self.timer.timeout.connect(self.playgame)

        self.show()


    def playgame(self):
        self.rndcomputer=randint(1,3)
        self.rnduser=randint(1,3)

        if self.rndcomputer==1:
            self.computerside.setPixmap(QPixmap('image/paper.png'))
        elif self.rndcomputer==2:
            self.computerside.setPixmap(QPixmap('image/rock.png'))
        else:
            self.computerside.setPixmap(QPixmap('image/scissors.png'))

        if self.rnduser==1:
            self.userside.setPixmap(QPixmap('image/paper.png'))
        elif self.rnduser==2:
            self.userside.setPixmap(QPixmap('image/rock.png'))
        else:
            self.userside.setPixmap(QPixmap('image/scissors.png'))


    def exitgame(self):
        mbox=QMessageBox.question(self,'Warning!','Are you sure to exit?',QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel,QMessageBox.No)
        if mbox==QMessageBox.Yes:
            sys.exit()
        else :
            pass


    def startgame(self):
        self.timer.start()


    def stopgame(self):
        self.timer.stop()
        global computerscore
        global userscore
        if self.rnduser == self.rndcomputer :
            mbox=QMessageBox.information(self,'Information!',"Draw Game!")
        elif self.rnduser == 1:
            if self.rndcomputer == 2:
                mbox=QMessageBox.information(self,'Information!',"YOU win!")
                userscore += 1
                self.userscoretext.setText('  User  Score :{} '.format(userscore))
            elif self.rndcomputer == 3:
                mbox=QMessageBox.information(self,'Information!',"COMPUTER wins!")
                computerscore += 1
                self.computerscoretext.setText('Computer Score :{} '.format(computerscore))
        elif self.rnduser == 2:
            if self.rndcomputer == 1:
                mbox=QMessageBox.information(self,'Information!',"COMPUTER wins!")
                computerscore += 1
                self.computerscoretext.setText('Computer Score :{} '.format(computerscore))
            elif self.rndcomputer == 3:
                mbox=QMessageBox.information(self,'Information!',"YOU win!")
                userscore += 1
                self.userscoretext.setText('  User  Score :{} '.format(userscore))
        elif self.rnduser == 3:
            if self.rndcomputer == 1:
                mbox=QMessageBox.information(self,'Information!',"YOU win!")
                userscore += 1
                self.userscoretext.setText('  User  Score :{} '.format(userscore))
            elif self.rndcomputer == 2:
                mbox=QMessageBox.information(self,'Information!',"COMPUTER wins!")
                computerscore += 1
                self.computerscoretext.setText('Computer Score :{} '.format(computerscore))

        if computerscore == 3 :
            mbox=QMessageBox.information(self,'End!','GAME OVER!')
            computerscore = 0
            userscore = 0
            self.computerscoretext.setText('Computer Score :{} '.format(computerscore))
            self.userscoretext.setText('  User  Score :{} '.format(userscore))
        elif userscore == 3 :
            mbox=QMessageBox.information(self,'End!','CONGRATS!')
            computerscore = 0
            userscore = 0
            self.computerscoretext.setText('Computer Score :{} '.format(computerscore))
            self.userscoretext.setText('  User  Score :{} '.format(userscore))


def main():
    App = QApplication(sys.argv)
    Window = window()
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()