from PyQt5.QtWidgets import*
from PyQt5.QtGui import*
from PyQt5.QtCore import*
import sys
import os
os.system("cls")
class dastur(QMainWindow):
    
    def __init__(self):
        QMainWindow.__init__(self)
        self.setMaximumSize(1000,800)
        self.setMinimumSize(1000,800)
        self.setFont(QFont("calibri",20))

        self.lebal=QLabel(self)
        self.lebal.setText("Ism: ")
        self.lebal.setGeometry(50,30,250,50)
        self.txt=QLineEdit(self)
        self.txt.setGeometry(283,30,350,50)

        self.lebal2=QLabel(self)
        self.lebal2.setText("Familya: ")
        self.lebal2.setGeometry(50,80,250,50)
        self.txt1=QLineEdit(self)
        self.txt1.setGeometry(283,80,350,50)

        self.dav=QLabel("Jins: ",self)
        self.dav.setGeometry(50,130,250,50)
        self.la=QComboBox(self)
        self.la.setGeometry(283,130,350,50)
        self.la.addItems(["Erkak","Ayol"])
        
        self.email=QLabel(self)
        self.email.setText("Email: ")
        self.email.setGeometry(50,180,250,50)
        self.txt3=QLineEdit(self)
        self.txt3.setGeometry(283,180,350,50)
        

        self.par=QLabel("Parol: ",self)
        self.par.setGeometry(50,230,250,50)
        self.parol=QLineEdit(self)
        self.parol.setMinimumHeight(8)
        self.parol.setGeometry(283,230,350,50)
        self.parol.setEchoMode(QLineEdit.Password)

        self.kor=QCheckBox(":ko'rish",self)
        self.kor.setFont(QFont("Times new Roman",11))
        self.kor.setStyleSheet("color:rgb(50,205,20);")
        self.kor.setGeometry(650,230,150,50)
        self.kor.stateChanged.connect(self.password)

        self.bat=QPushButton(self)
        self.bat.setText("Olg'a")
        self.bat.setGeometry(283,300,150,50)
        self.bat.setStyleSheet("""
        color: rgb("green");
        background-color: rgb(0,0,0);
        border-color: rgb("green);
        border-width: 3px;
        border-radius: 20px;
        border-style: outset;""")
        self.bat.clicked.connect(self.natija)
        
    def password(self):
        if self.kor.isChecked():
            self.parol.setEchoMode(QLineEdit.Normal)
        else:
            self.parol.setEchoMode(QLineEdit.Password)
        

    def natija(self):
        self.parol1="1234asdf"    
        if self.parol.text()==self.parol1:
            f=open("Natija ","a")
            f.write(f"Ismi :{self.txt.text()}\t")
            f.write(f"Familya :{self.txt1.text()}\t")
            f.write(f"Email:{self.txt3.text()}\t")
            f.write(f"Parol :{self.parol.text()}\n")

ap=QApplication(sys.argv)
loy=dastur()
loy.show()
sys.exit(ap.exec())      