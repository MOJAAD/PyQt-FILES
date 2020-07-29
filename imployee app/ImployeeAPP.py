import sys,sqlite3,os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap,QFont
from PIL import Image

con = sqlite3.connect("employee.db")
cur = con.cursor()
defultimg="person.png"
class window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(400,100,550,500)
        self.setWindowTitle("Employees App")
        self.UI()
        self.show()

    def UI(self):
        self.maindesigned()
        self.Layouts()

    def maindesigned(self):
        self.employeelist=QListWidget()
        self.newbtn=QPushButton("New",self)
        self.newbtn.clicked.connect(self.addemployee)
        self.deletebtn=QPushButton("Delete",self)
        self.updatebtn=QPushButton("Update",self)


    def Layouts(self):
        self.mainlayout=QHBoxLayout()
        self.leftlayout=QFormLayout()
        self.rightmainlayout=QVBoxLayout()
        self.righttoplayout=QHBoxLayout()
        self.rightbuttomlayout=QHBoxLayout()

        self.rightmainlayout.addLayout(self.righttoplayout)
        self.rightmainlayout.addLayout(self.rightbuttomlayout)
        self.mainlayout.addLayout(self.leftlayout,50)
        self.mainlayout.addLayout(self.rightmainlayout,50)

        self.righttoplayout.addWidget(self.employeelist)
        self.rightbuttomlayout.addWidget(self.newbtn)
        self.rightbuttomlayout.addWidget(self.deletebtn)
        self.rightbuttomlayout.addWidget(self.updatebtn)

        self.setLayout(self.mainlayout)

    def addemployee(self):
        self.newemployee=Addemployee()
        self.close()



class Addemployee(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(400,100,350,500)
        self.setWindowTitle("Add Employees")
        self.UI()
        self.show()

    def UI(self):
        self.maindesign()
        self.layout()

    def maindesign(self):
        self.setStyleSheet("background-color:white;font-size:12pt;")
        self.title=QLabel("Add Person")
        self.title.setStyleSheet("font-size: 18pt;font-family:Arial Bold;")
        self.imgadd=QLabel()
        self.imgadd.setPixmap(QPixmap('icons/person.png'))

        self.firstnamelbl=QLabel("First Name:")
        self.fnbox=QLineEdit()
        self.fnbox.setPlaceholderText("Enter First Name here")
        self.lastnamelbl=QLabel("Last Name:")
        self.lnbox=QLineEdit()
        self.lnbox.setPlaceholderText("Enter Last Name here")
        self.phonelbl=QLabel("Phone:")
        self.phbox=QLineEdit()
        self.phbox.setPlaceholderText("Enter Phone Number here")
        self.emlbl=QLabel("E-mail:")
        self.ebox=QLineEdit()
        self.ebox.setPlaceholderText("Enter Email Address here")
        self.imglbl=QLabel("Picture:")
        self.imgbtn=QPushButton("Browse",self)
        self.imgbtn.clicked.connect(self.uploadimg)
        self.imgbtn.setStyleSheet("background-color:yellow;font-size:10pt;")
        self.addtext=QLabel("Address:")
        self.addtextbox=QTextEdit()
        self.addbox=QPushButton("ADD",self)
        self.addbox.setStyleSheet("background-color:orange;font-size:10pt;")
        self.addbox.clicked.connect(self.addemployee)
        
    def addemployee(self):
        global defultimg
        firstname=self.fnbox.text()
        lastname=self.lnbox.text()
        phone=self.phbox.text()
        email=self.ebox.text()
        address=self.addtextbox.toPlainText()
        image=defultimg
        if (firstname and lastname and phone !=""):
            try:
                query="INSERT INTO employees (firstname,lastname,phone,email,address,image) VALUES (?,?,?,?,?,?)"
                cur.execute(query,(firstname,lastname,phone,email,address,image)) 
                con.commit()
                QMessageBox.information(self,'Success','Person has been added!')
                self.close()
                self.main=window()
            except:
                QMessageBox.information(self,"warning","A fault is happen\nPlease try again")
        else:
            QMessageBox.information(self,"Warning!","Fields can not be empty!")

    def closeEvent(self,event):
        self.main=window()

    def uploadimg(self):
        size=(128,128)
        self.filename,ok=QFileDialog.getOpenFileName(self,"Upload Image...",'',"Image Files (*.jpg *.png)")
        if ok:
            global defultimg
            defultimg=os.path.basename(self.filename)
            img=Image.open(self.filename)
            img=img.resize(size)
            img.save('images/{}'.format(defultimg))



    def layout(self):
        self.mainlayout=QVBoxLayout()
        self.toplayout=QVBoxLayout()
        self.buttomlayout=QFormLayout()

        self.mainlayout.addLayout(self.toplayout)
        self.mainlayout.addLayout(self.buttomlayout)

        self.toplayout.addStretch()
        self.toplayout.addWidget(self.title)
        self.toplayout.addWidget(self.imgadd)
        self.toplayout.setContentsMargins(110,10,110,10)
        self.toplayout.addStretch()

        self.buttomlayout.addRow(self.firstnamelbl,self.fnbox)
        self.buttomlayout.addRow(self.lastnamelbl,self.lnbox)
        self.buttomlayout.addRow(self.phonelbl,self.phbox)
        self.buttomlayout.addRow(self.emlbl,self.ebox)
        self.buttomlayout.addRow(self.imglbl,self.imgbtn)
        self.buttomlayout.addRow(self.addtext,self.addtextbox)
        self.buttomlayout.addRow("",self.addbox)
        
        self.setLayout(self.mainlayout)

def main():
    App = QApplication(sys.argv)
    Window = window()
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()