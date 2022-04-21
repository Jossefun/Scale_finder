#from curses.textpad import Textbox
import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import center
import scale_finder 


from PyQt5.QtWidgets import (
    QApplication,
    QLabel,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
    QGridLayout,
    QSizePolicy,
) 



class Mywindow(QMainWindow):
    def __init__(self):
        super(Mywindow, self).__init__()

        self.setGeometry(300,300,350,350)
        self.setWindowTitle("Scale Finder")
        self.initUI()


    def initUI(self):
       
         #resize(length, hight)
         #move(right left, up down)
         
        #Record Button
        self.recButton = QtWidgets.QPushButton(self)
        self.recButton.setText("Record Your Note")
        #self.recButton.clicked.connect(self.clicked)
        self.recButton.move(20,20)

        #Enter Note Label
        self.enterlabel = QtWidgets.QLabel(self)
        self.enterlabel.setText("Or Enter Note Here:")
        self.enterlabel.move(169,20)

        #Note input Text
        self.notetextbox = QLineEdit(self)
        self.notetextbox.move(277,27)
        self.notetextbox.resize(50,20)
        
        self.chooseScale = QtWidgets.QLabel(self)
        self.chooseScale.setText("Choose Your Scale:")
        self.chooseScale.move(20,70)
        
        
        #Choose tizita major Buttons
        self.tizMajB = QtWidgets.QPushButton(self)
        self.tizMajB.setText("Tizita Major")
        self.tizMajB.clicked.connect(self.TizMajScale)
        self.tizMajB.move(20,110)
        self.tizMajB.resize(70,25)
        
        #Choose tizita minor Buttons
        self.tizMinB = QtWidgets.QPushButton(self)
        self.tizMinB.setText("Tizita Minor")
        self.tizMinB.clicked.connect(self.TizMinScale)
        self.tizMinB.move(100,110)
        self.tizMinB.resize(70,25)
        
        #Choose Bati major Buttons
        self.batiMajB = QtWidgets.QPushButton(self)
        self.batiMajB.setText("Bati Major")
        self.batiMajB.clicked.connect(self.BatiMajScale)
        self.batiMajB.move(180,110)
        self.batiMajB.resize(70,25)
        
        #Choose Bati minor Buttons
        self.batiMinB = QtWidgets.QPushButton(self)
        self.batiMinB.setText("Bati Minor")
        self.batiMinB.clicked.connect(self.BatiMinScale)
        self.batiMinB.move(260,110)
        self.batiMinB.resize(70,25)
        
         #Choose Ambassel Buttons
        self.ambasselB = QtWidgets.QPushButton(self)
        self.ambasselB.setText("Ambassel")
        self.ambasselB.clicked.connect(self.AmbasselScale)
        self.ambasselB.move(20,145)
        self.ambasselB.resize(70,25)
        
         #Choose Anche Hoye Buttons
        self.ancheHoyeB = QtWidgets.QPushButton(self)
        self.ancheHoyeB.setText("Anche Hoye")
        self.ancheHoyeB.clicked.connect(self.AncheHoyeScale)
        self.ancheHoyeB.move(100,145)
        self.ancheHoyeB.resize(70,25)
        
         #Choose Major7 Buttons
        self.major7B = QtWidgets.QPushButton(self)
        self.major7B.setText("Major7")
        self.major7B.clicked.connect(self.Major7Scale)
        self.major7B.move(180,145)
        self.major7B.resize(70,25)
        
         #Choose Minor7 Buttons
        self.minor7B = QtWidgets.QPushButton(self)
        self.minor7B.setText("Minor7")
        self.minor7B.clicked.connect(self.Minor7Scale)
        self.minor7B.move(260,145)
        self.minor7B.resize(70,25)
        
        
        
        
        

        #Result Label
        self.resultLabel = QtWidgets.QLabel(self)
        self.resultLabel.setText("Your Scale is:")
        self.resultLabel.move(20,190)
        


        #Result TextBox
        self.resultTextbox = QLineEdit(self)
        self.resultTextbox.move(100,220)
        self.resultTextbox.resize(150,20) 
        
       
         
        #Style
        self.enterlabel.setStyleSheet(
            "font-size: 13px;"
            )
        # self.notetextbox.setStyleSheet(
        #     "border-style: soild;"
        #     "border-color: #E7C102;" 
        #  )
        self.chooseScale.setStyleSheet(
            "font-size: 12px;" 
            )
        self.resultLabel.setStyleSheet(
            "font-size: 14px;" 
            )
        self.recButton.setStyleSheet(
            "background: #E7C102"
        )
        self.tizMajB.setStyleSheet(
            "background: #E7C102"
        )
        self.tizMinB.setStyleSheet(
            "background: #E7C102"
        )
        self.batiMajB.setStyleSheet(
            "background: #E7C102"
        )
        self.batiMinB.setStyleSheet(
            "background: #E7C102"
        )
        self.ambasselB.setStyleSheet(
            "background: #E7C102"
        )
        self.ancheHoyeB.setStyleSheet(
            "background: #E7C102"
        )
        self.major7B.setStyleSheet(
            "background: #E7C102"
        )
        self.minor7B.setStyleSheet(
            "background: #E7C102"
        )
         
       
        
        


    # Buttons Clicked    
   
    def TizMajScale(self):
        textvalue = self.notetextbox.text()
        indexnote = scale_finder.FindIndex(textvalue)
        self.resultTextbox.setText(str(scale_finder.TizitaMajorscale(indexnote)))
        
    def TizMinScale(self):
        textvalue = self.notetextbox.text()
        indexnote = scale_finder.FindIndex(textvalue)
        self.resultTextbox.setText(str(scale_finder.TizitaMinorscale(indexnote)))    
        
    def BatiMajScale(self):
        textvalue = self.notetextbox.text()
        indexnote = scale_finder.FindIndex(textvalue)
        self.resultTextbox.setText(str(scale_finder.BatiMajorscale(indexnote))) 
        
    def BatiMinScale(self):
        textvalue = self.notetextbox.text()
        indexnote = scale_finder.FindIndex(textvalue)
        self.resultTextbox.setText(str(scale_finder.BatiMinorscale(indexnote)))       
           
    def AmbasselScale(self):
        textvalue = self.notetextbox.text()
        indexnote = scale_finder.FindIndex(textvalue)
        self.resultTextbox.setText(str(scale_finder.Ambasselscale(indexnote)))   
        
    def AncheHoyeScale(self):
        textvalue = self.notetextbox.text()
        indexnote = scale_finder.FindIndex(textvalue)
        self.resultTextbox.setText(str(scale_finder.AnchiHoyescale(indexnote)))       
        
    def Major7Scale(self):
        textvalue = self.notetextbox.text()
        indexnote = scale_finder.FindIndex(textvalue)
        self.resultTextbox.setText(str(scale_finder.Major7scale(indexnote)))   
        
    def Minor7Scale(self):
        textvalue = self.notetextbox.text()
        indexnote = scale_finder.FindIndex(textvalue)
        self.resultTextbox.setText(str(scale_finder.Minor7scale(indexnote)))           


def window():
    app = QApplication(sys.argv)
    win = Mywindow()
    win.setStyleSheet("background: #8CC21B")
    win.show()
    sys.exit(app.exec())




window()





