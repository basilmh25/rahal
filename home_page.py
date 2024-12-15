import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg
import sys
import user as data
import person

class home_page(qtw.QTabWidget):
    def __init__(self, parent) :
        super().__init__(parent)
        self.parent=parent
        self.setGeometry(100,200,1600,950)
        self.setStyleSheet("background-image:url(source/home_page.png)")
        self.rentcar_button=qtw.QPushButton(self)
        self.rentcar_button.setGeometry(507,459,182,91)
        self.rentcar_button.setStyleSheet("background-image:url(source/rent car); border-radius: 19")
        
        self.mycar_button=qtw.QPushButton(self)
        self.mycar_button.setGeometry(507,626,182,91)
        self.mycar_button.setStyleSheet("background-image:url(source/my car); border-radius: 19")
        self.mycar_button.clicked.connect(self.mycar_def)

        self.account_button=qtw.QPushButton(self)
        self.account_button.setGeometry(910,459,182,91)
        self.account_button.setStyleSheet("background-image:url(source/account); border-radius: 19")
        self.account_button.clicked.connect(self.account_def)
        
        self.logut_button=qtw.QPushButton(self)
        self.logut_button.setGeometry(912,627,182,91)
        self.logut_button.setStyleSheet("background-image:url(source/logout); border-radius: 19")
        self.logut_button.clicked.connect(self.logout_def)

        self.fontbox = qtg.QFont()
        self.fontbox.setFamily("Roboto")
        self.fontbox.setPointSize(120)
        self.fontbox.setBold(True)

        self.hiname=qtw.QLabel(self)
        self.hiname.setText(self.parent.cmail.get_frist_name())
        print(self.parent.cmail.get_frist_name())
        self.hiname.setGeometry(529,66,831,137)
        self.hiname.setFont(self.fontbox)
        self.hiname.setStyleSheet("background:white;color:#0855ff")

    def logout_def(self):
        self.parent.resize(800,600)
        self.parent.setCurrentWidget(self.parent.login_page)
    
    def account_def(self):
        self.parent.setCurrentWidget(self.parent.account_page)

    def mycar_def(self):
        self.parent.setCurrentWidget(self.parent.no_car)

