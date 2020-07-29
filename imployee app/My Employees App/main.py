from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap,QFont
import sys,os
import sqlite3
from PIL import Image


con = sqlite3.connect('employees.db')
cur = con.cursor()
defaultImg="person.png"
person_id=None
class Main(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My Employees")
        self.setGeometry(450,150,750,600)
        self.UI()
        self.show()


    def UI(self):
        self.mainDesign()
        self.layouts()
        self.getEmployees()
        self.displayFirstRecord()

    def mainDesign(self):
        self.setStyleSheet("font-size:14pt;font-family:Arial Bold;")
        self.employeeList=QListWidget()
        self.employeeList.itemClicked.connect(self.singleClick)
        self.btnNew=QPushButton("New")
        self.btnNew.clicked.connect(self.addEmployee)
        self.btnUpdate=QPushButton("Update")
        self.btnUpdate.clicked.connect(self.updateEmployee)
        self.btnDelete=QPushButton("Delete")
        self.btnDelete.clicked.connect(self.deleteEmployee)

    def layouts(self):
        ###################Layouts###############
        self.mainLayout=QHBoxLayout()
        self.leftLayout=QFormLayout()
        self.rightMainLayout=QVBoxLayout()
        self.rightTopLayout=QHBoxLayout()
        self.rightBottomLayout=QHBoxLayout()
        #####################Adding child layouts to main layout###########
        self.rightMainLayout.addLayout(self.rightTopLayout)
        self.rightMainLayout.addLayout(self.rightBottomLayout)
        self.mainLayout.addLayout(self.leftLayout,40)
        self.mainLayout.addLayout(self.rightMainLayout,60)
        ###################adding wigdets to layouts#################
        self.rightTopLayout.addWidget(self.employeeList)
        self.rightBottomLayout.addWidget(self.btnNew)
        self.rightBottomLayout.addWidget(self.btnUpdate)
        self.rightBottomLayout.addWidget(self.btnDelete)
        ##############setting main window layout#####################
        self.setLayout(self.mainLayout)

    def addEmployee(self):
        self.newEmployee=AddEmployee()
        self.close()
    def getEmployees(self):
        query="SELECT id,name,surname FROM employees"
        employees=cur.execute(query).fetchall()
        for employee in employees:
            self.employeeList.addItem(str(employee[0])+"-"+employee[1]+" "+employee[2] )

    def displayFirstRecord(self):
        query="SELECT * FROM employees ORDER BY ROWID ASC LIMIT 1"
        employee=cur.execute(query).fetchone()
        img=QLabel()
        img.setPixmap(QPixmap("images/"+employee[5]))
        name=QLabel(employee[1])
        surname=QLabel(employee[2])
        phone=QLabel(employee[3])
        email=QLabel(employee[4])
        address=QLabel(employee[6])
        self.leftLayout.setVerticalSpacing(20)
        self.leftLayout.addRow("",img)
        self.leftLayout.addRow("Name: ",name)
        self.leftLayout.addRow("Surname :",surname)
        self.leftLayout.addRow("Phone :",phone)
        self.leftLayout.addRow("Email :",email)
        self.leftLayout.addRow("Address:",address)

    def singleClick(self):
        for i in reversed(range(self.leftLayout.count())):
            widget=self.leftLayout.takeAt(i).widget()

            if widget is not None:
                widget.deleteLater()

        employee=self.employeeList.currentItem().text()
        id=employee.split("-")[0]
        query=("SELECT * FROM employees WHERE id=?")
        person=cur.execute(query,(id,)).fetchone()#single item tuple=(1,)
        img = QLabel()
        img.setPixmap(QPixmap("images/" + person[5]))
        name = QLabel(person[1])
        surname = QLabel(person[2])
        phone = QLabel(person[3])
        email = QLabel(person[4])
        address = QLabel(person[6])
        self.leftLayout.setVerticalSpacing(20)
        self.leftLayout.addRow("", img)
        self.leftLayout.addRow("Name: ", name)
        self.leftLayout.addRow("Surname :", surname)
        self.leftLayout.addRow("Phone :", phone)
        self.leftLayout.addRow("Email :", email)
        self.leftLayout.addRow("Address:", address)

    def deleteEmployee(self):
        if self.employeeList.selectedItems():
            person=self.employeeList.currentItem().text()
            id = person.split("-")[0]
            mbox=QMessageBox.question(self,"Warning","Are you sure to delete this person?",QMessageBox.Yes|QMessageBox.No,QMessageBox.No)
            if mbox == QMessageBox.Yes:
                try:
                    query="DELETE FROM employees WHERE id=?"
                    cur.execute(query,(id,))
                    con.commit()
                    QMessageBox.information(self,"Info!!!","Person has been deleted")
                    self.close()
                    self.main=Main()

                except:
                    QMessageBox.information(self,"Warning!!!","Person has not been deleted")


        else:
            QMessageBox.information(self, "Warning!!!", "Please select a person to delete")


    def updateEmployee(self):
        global person_id
        if self.employeeList.selectedItems():
            person = self.employeeList.currentItem().text()
            person_id=person.split("-")[0]
            self.updateWindow=UpdateEmployee()
            self.close()

        else:
            QMessageBox.information(self, "Warning!!!", "Please select a person to update")



class UpdateEmployee(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Update Employee")
        self.setGeometry(450,150,350,600)
        self.UI()
        self.show()

    def UI(self):

        self.getPerson()
        self.mainDesign()
        self.layouts()

    def closeEvent(self, event):
        self.main = Main()

    def getPerson(self):
        global person_id
        query="SELECT * FROM employees WHERE id=?"
        employee=cur.execute(query,(person_id,)).fetchone()
        print(employee)
        self.name=employee[1]
        self.surname=employee[2]
        self.phone=employee[3]
        self.email=employee[4]
        self.image=employee[5]
        self.address=employee[6]

    def mainDesign(self):
        ################Top Layout widgets#######################
        self.setStyleSheet("background-color:white;font-size:14pt;font-family:Times")
        self.title = QLabel("Update Person")
        self.title.setStyleSheet('font-size: 24pt;font-family:Arial Bold;')
        self.imgAdd = QLabel()
        self.imgAdd.setPixmap(QPixmap("images/{}".format(self.image)))
        ###################Bottom Layout Widgets#####################
        self.nameLbl = QLabel("Name :")
        self.nameEntry = QLineEdit()
        self.nameEntry.setText(self.name)
        self.surnameLbl = QLabel("Surname :")
        self.surnameEntry = QLineEdit()
        self.surnameEntry.setText(self.surname)
        self.phoneLbl = QLabel("Phone :")
        self.phoneEntry = QLineEdit()
        self.phoneEntry.setText(self.phone)
        self.emailLbl = QLabel("Email :")
        self.emailEntry = QLineEdit()
        self.emailEntry.setText(self.email)
        self.imgLbl = QLabel("Picture: ")
        self.imgButton = QPushButton("Browse")
        self.imgButton.setStyleSheet("background-color:orange;font-size:10pt")
        self.imgButton.clicked.connect(self.uploadImage)
        self.addressLbl = QLabel("Address: ")
        self.addressEditor = QTextEdit()
        self.addressEditor.setText(self.address)
        self.addButton = QPushButton("Update")
        self.addButton.setStyleSheet("background-color:orange;font-size:10pt")
        self.addButton.clicked.connect(self.updateEmployee)

    def layouts(self):
        ##################creating main layouts##########
        self.mainLayout = QVBoxLayout()
        self.topLayout = QVBoxLayout()
        self.bottomLayout = QFormLayout()

        ##########adding child layouts to main layout##############
        self.mainLayout.addLayout(self.topLayout)
        self.mainLayout.addLayout(self.bottomLayout)

        ##################adding wigdets to layouts##############
        ##############top layout################
        self.topLayout.addStretch()
        self.topLayout.addWidget(self.title)
        self.topLayout.addWidget(self.imgAdd)
        self.topLayout.addStretch()
        self.topLayout.setContentsMargins(110, 20, 10, 30)  # left,top,right,bottom
        ###########bottom layout#################
        self.bottomLayout.addRow(self.nameLbl, self.nameEntry)
        self.bottomLayout.addRow(self.surnameLbl, self.surnameEntry)
        self.bottomLayout.addRow(self.phoneLbl, self.phoneEntry)
        self.bottomLayout.addRow(self.emailLbl, self.emailEntry)
        self.bottomLayout.addRow(self.imgLbl, self.imgButton)
        self.bottomLayout.addRow(self.addressLbl, self.addressEditor)
        self.bottomLayout.addRow("", self.addButton)

        ###########setting main layout for window##################
        self.setLayout(self.mainLayout)


    def uploadImage(self):
        global defaultImg
        size =(128,128)
        self.fileName,ok =QFileDialog.getOpenFileName(self,'Upload Image','','Image Files (*.jpg *.png)')

        if ok:

            defaultImg=os.path.basename(self.fileName)
            img=Image.open(self.fileName)
            img=img.resize(size)
            img.save("images/{}".format(defaultImg))



    def updateEmployee(self):
        global defaultImg
        global person_id
        name=self.nameEntry.text()
        surname=self.surnameEntry.text()
        phone=self.phoneEntry.text()
        email=self.emailEntry.text()
        img=defaultImg
        address=self.addressEditor.toPlainText()
        if (name and surname and phone !=""):
            try:
                query="UPDATE employees set name =?, surname=?, phone=?,email=?,img=?,address=? WHERE id=?"
                cur.execute(query,(name,surname,phone,email,img,address,person_id))
                con.commit()
                QMessageBox.information(self,"Success","Person has been updated")
                self.close()
                self.main=Main()
            except:
                QMessageBox.information(self, "Warning", "Person has not been updated")

        else:
            QMessageBox.information(self, "Warning", "Fields can not be empty")



class AddEmployee(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Add Employees")
        self.setGeometry(450,150,350,600)
        self.UI()
        self.show()

    def UI(self):
        self.mainDesign()
        self.layouts()

    def closeEvent(self, event):
        self.main=Main()

    def mainDesign(self):
        ################Top Layout widgets#######################
        self.setStyleSheet("background-color:white;font-size:14pt;font-family:Times")
        self.title=QLabel("Add Person")
        self.title.setStyleSheet('font-size: 24pt;font-family:Arial Bold;')
        self.imgAdd=QLabel()
        self.imgAdd.setPixmap(QPixmap("icons/person.png"))
        ###################Bottom Layout Widgets#####################
        self.nameLbl=QLabel("Name :")
        self.nameEntry=QLineEdit()
        self.nameEntry.setPlaceholderText("Enter Employee Name")
        self.surnameLbl = QLabel("Surname :")
        self.surnameEntry = QLineEdit()
        self.surnameEntry.setPlaceholderText("Enter Employee Surname")
        self.phoneLbl = QLabel("Phone :")
        self.phoneEntry = QLineEdit()
        self.phoneEntry.setPlaceholderText("Enter Employee Phone Number")
        self.emailLbl = QLabel("Email :")
        self.emailEntry = QLineEdit()
        self.emailEntry.setPlaceholderText("Enter Employee Email")
        self.imgLbl=QLabel("Picture: ")
        self.imgButton=QPushButton("Browse")
        self.imgButton.setStyleSheet("background-color:orange;font-size:10pt")
        self.imgButton.clicked.connect(self.uploadImage)
        self.addressLbl=QLabel("Address: ")
        self.addressEditor=QTextEdit()
        self.addButton=QPushButton("Add")
        self.addButton.setStyleSheet("background-color:orange;font-size:10pt")
        self.addButton.clicked.connect(self.addEmployee)

    def layouts(self):
        ##################creating main layouts##########
        self.mainLayout=QVBoxLayout()
        self.topLayout=QVBoxLayout()
        self.bottomLayout=QFormLayout()

        ##########adding child layouts to main layout##############
        self.mainLayout.addLayout(self.topLayout)
        self.mainLayout.addLayout(self.bottomLayout)

        ##################adding wigdets to layouts##############
                ##############top layout################
        self.topLayout.addStretch()
        self.topLayout.addWidget(self.title)
        self.topLayout.addWidget(self.imgAdd)
        self.topLayout.addStretch()
        self.topLayout.setContentsMargins(110,20,10,30) #left,top,right,bottom
                ###########bottom layout#################
        self.bottomLayout.addRow(self.nameLbl,self.nameEntry)
        self.bottomLayout.addRow(self.surnameLbl,self.surnameEntry)
        self.bottomLayout.addRow(self.phoneLbl,self.phoneEntry)
        self.bottomLayout.addRow(self.emailLbl,self.emailEntry)
        self.bottomLayout.addRow(self.imgLbl,self.imgButton)
        self.bottomLayout.addRow(self.addressLbl,self.addressEditor)
        self.bottomLayout.addRow("",self.addButton)

        ###########setting main layout for window##################
        self.setLayout(self.mainLayout)

    def uploadImage(self):
        global defaultImg
        size =(128,128)
        self.fileName,ok =QFileDialog.getOpenFileName(self,'Upload Image','','Image Files (*.jpg *.png)')

        if ok:

            defaultImg=os.path.basename(self.fileName)
            img=Image.open(self.fileName)
            img=img.resize(size)
            img.save("images/{}".format(defaultImg))



    def addEmployee(self):
        global defaultImg
        name=self.nameEntry.text()
        surname=self.surnameEntry.text()
        phone=self.phoneEntry.text()
        email=self.emailEntry.text()
        img=defaultImg
        address=self.addressEditor.toPlainText()
        if (name and surname and phone !=""):
            try:
                query="INSERT INTO employees (name,surname,phone,email,img,address) VALUES(?,?,?,?,?,?)"
                cur.execute(query,(name,surname,phone,email,img,address))
                con.commit()
                QMessageBox.information(self,"Success","Person has been added")
                self.close()
                self.main=Main()
            except:
                QMessageBox.information(self, "Warning", "Person has not been added")

        else:
            QMessageBox.information(self, "Warning", "Fields can not be empty")



def main():
    APP=QApplication(sys.argv)
    window=Main()
    sys.exit(APP.exec_())
if __name__ == '__main__':
    main()