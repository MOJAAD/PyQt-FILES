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
        self.setGeometry(300,100,750,500)
        self.setWindowTitle("Employees App")
        self.UI()
        self.show()

    def getemployee(self):
        query="SELECT id,firstname,lastname FROM employees"
        employees=cur.execute(query).fetchall()
        for employee in employees:
            self.employeelist.addItem(str(employee[0])+' ) '+employee[1]+"  "+employee[2])

    def showfirst(self):
        query="SELECT * FROM employees ORDER BY ROWID ASC LIMIT 1"
        employee=cur.execute(query).fetchone()
        if employee is not None:
            image=QLabel()
            image.setPixmap(QPixmap("images/"+employee[5]))
            firstname=QLabel(employee[1])
            lastname=QLabel(employee[2])
            phone=QLabel(employee[3])
            email=QLabel(employee[4])
            address=QLabel(employee[6])
            self.leftlayout.setVerticalSpacing(20)
            self.leftlayout.addRow("",image)
            self.leftlayout.addRow("First Name    : ",firstname)
            self.leftlayout.addRow("Last  Name    : ",lastname)
            self.leftlayout.addRow("Phone number  : ",phone)
            self.leftlayout.addRow("Email Address : ",email)
            self.leftlayout.addRow("Address       : ",address)
        else:
            pass

    def showchoosen(self):
        for i in reversed(range(self.leftlayout.count())):
            widget=self.leftlayout.takeAt(i).widget()
            if widget is not None:
                widget.deleteLater()
        employee=self.employeelist.currentItem().text()
        id=employee.split(" ) ")[0]
        query="SELECT * FROM employees WHERE id=?"
        employee=cur.execute(query,(id,)).fetchone() #single item tuple=(1,)
        image=QLabel()
        image.setPixmap(QPixmap("images/"+employee[5]))
        firstname=QLabel(employee[1])
        lastname=QLabel(employee[2])
        phone=QLabel(employee[3])
        email=QLabel(employee[4])
        address=QLabel(employee[6])
        self.leftlayout.setVerticalSpacing(20)
        self.leftlayout.addRow("",image)
        self.leftlayout.addRow("First Name    : ",firstname)
        self.leftlayout.addRow("Last  Name    : ",lastname)
        self.leftlayout.addRow("Phone number  : ",phone)
        self.leftlayout.addRow("Email Address : ",email)
        self.leftlayout.addRow("Address       : ",address)


    def UI(self):
        self.maindesigned()
        self.Layouts()
        self.getemployee()
        self.showfirst()

    def maindesigned(self):
        self.setStyleSheet("font-size:12pt")
        self.employeelist=QListWidget()
        self.employeelist.itemClicked.connect(self.showchoosen)
        self.newbtn=QPushButton("New",self)
        self.newbtn.clicked.connect(self.addemployee)
        self.deletebtn=QPushButton("Delete",self)
        self.deletebtn.clicked.connect(self.deleteemploye)
        self.updatebtn=QPushButton("Update",self)
        self.updatebtn.clicked.connect(self.updateemploye)

    def updateemploye(self):
        if self.employeelist.selectedItems():
            employee=self.employeelist.currentItem().text()
            id=employee.split(" ) ")[0]
            self.updatewindow=UpdateEmployee()
            self.close()
        else:
            QMessageBox.information(self,'Warning','Please select somone!')
        
    def deleteemploye(self):
        if self.employeelist.selectedItems():
            employee=self.employeelist.currentItem().text()
            id=employee.split(" ) ")[0]
            mbox=QMessageBox.question(self,"Warning!","Are you want to delete?",QMessageBox.Yes|QMessageBox.No,QMessageBox.No)
            if mbox==QMessageBox.Yes:
                try:
                    query="DELETE FROM employees WHERE id=?"
                    cur.execute(query,(id,))
                    con.commit()
                    QMessageBox.information(self,'Info...','Delete Successfully!')
                    self.close()
                    self.main=window()
                except:
                    QMessageBox.information(self,'Info...','Deleteing is Not Successfully!')
        else:
            QMessageBox.information(self,'Warning','Please select somone!')

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

class UpdateEmployee(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(400,100,350,500)
        self.setWindowTitle("Add Employees")
        self.UI()
        self.show()

    def UI(self):
        pass

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
            self.imgadd.setPixmap(QPixmap('images/{}'.format(defultimg)))



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