from PyQt5.QtCore import Qt
import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg
import sys
import user as data

class signup(qtw.QTabWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent=parent
        self.setGeometry(100,200,800,800)
        self.setStyleSheet("background-image:url(source/signup_page.png)")
        
        self.fontbox = qtg.QFont()
        self.fontbox.setFamily("Roboto")
        self.fontbox.setPointSize(14)
        self.fontbox.setBold(True)
        
        self.fname_box=qtw.QLineEdit(self)
        self.fname_box.setGeometry(53,231,318,54)
        self.fname_box.setStyleSheet("background:#f6f6f6;color:#000000; border-radius:16")
        self.fname_box.setFont(self.fontbox)

        self.lname_box=qtw.QLineEdit(self)
        self.lname_box.setGeometry(432,231,318,54)
        self.lname_box.setStyleSheet("background:#f6f6f6;color:#000000; border-radius:16")
        self.lname_box.setFont(self.fontbox)
        
        self.email_box=qtw.QLineEdit(self)
        self.email_box.setGeometry(53,317,318,54)
        self.email_box.setStyleSheet("background:#f6f6f6;color:#000000; border-radius:16")
        self.email_box.setFont(self.fontbox)
        
        self.phone_box=qtw.QLineEdit(self)
        self.phone_box.setGeometry(432,317,318,54)
        self.phone_box.setStyleSheet("background:#f6f6f6;color:#000000; border-radius:16")
        self.phone_box.setFont(self.fontbox)
        
        self.pass_box=qtw.QLineEdit(self)
        self.pass_box.setGeometry(53,403,318,54)
        self.pass_box.setStyleSheet("background:#f6f6f6;color:#000000; border-radius:16")
        self.pass_box.setFont(self.fontbox)
        
        self.cpass_box=qtw.QLineEdit(self)
        self.cpass_box.setGeometry(432,403,318,54)
        self.cpass_box.setStyleSheet("background:#f6f6f6;color:#000000; border-radius:16")
        self.cpass_box.setFont(self.fontbox)

        self.register = qtw.QPushButton(self)
        self.register.setGeometry(275,506,250,54)
        self.register.setText("register")
        self.register.setStyleSheet("background:#0855ff;color:white;border-radius:16")
        self.register.setFont(self.fontbox)
        self.register.clicked.connect(self.register_def)
        
        self.font_login = qtg.QFont()
        self.font_login.setFamily("Roboto")
        self.font_login.setPointSize(12)
        
        self.login_button = qtw.QPushButton(self)
        self.login_button.setGeometry(479,564,40,21)
        self.login_button.setText("login")
        self.login_button.setFont(self.font_login)
        self.login_button.setStyleSheet("background:white;color:#0855ff;border-radius:16")
        self.login_button.clicked.connect(self.login_def)

        self.wrong_message=qtw.QLabel(self)
        self.wrong_message.move(60,159)
        self.wrong_message.setFont(self.fontbox)

    def login_def(self):
        self.parent.resize(800,600)
        self.parent.setCurrentWidget(self.parent.login_page)
        
    def register_def(self):
        fname=self.fname_box.text()
        lname=self.lname_box.text()
        email=self.email_box.text()
        phone=self.phone_box.text()
        password=self.pass_box.text()
        cpassword=self.cpass_box.text()

        self.parent.resize(1600,950)
        self.parent.setCurrentWidget(self.parent.home_page)
    
    def m_wrong(self,text):
        self.wrong_message.setText(text)