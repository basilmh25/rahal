import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg
import sys
import user as data
import person

class window(qtw.QTabWidget):
    def __init__(self,parent):
        super().__init__(parent)
        self.setWindowTitle("rahal")
        self.setGeometry(100,200,800,600)
        self.parent=parent
        self.setStyleSheet("background-image:url(source/login_page.png)")
        

        self.font_log = qtg.QFont()
        self.font_log.setFamily("Roboto")
        self.font_log.setPointSize(16)
        self.font_log.setBold(True)
        self.user_box=qtw.QLineEdit(self)
        self.user_box.setGeometry(440,201,318,54)
        self.user_box.setPlaceholderText("  Email")
        self.user_box.setStyleSheet("background:#f6f6f6;color:#000000; border-radius:15")
        self.user_box.setFont(self.font_log)
        
        self.font_la = qtg.QFont()
        self.font_la.setFamily("Roboto")
        self.font_la.setPointSize(12)
        self.font_la.setBold(True)
        self.la=qtw.QLabel(self)
        self.la.setGeometry(456,170,285,18)
        self.la.setFont(self.font_la)
        self.la.setStyleSheet("color:red;background:white")

        self.pass_box=qtw.QLineEdit(self)
        self.pass_box.setPlaceholderText("  password")
        self.pass_box.setFont(self.font_log)
        self.pass_box.setGeometry(440 ,285 ,318 ,54 )
        self.pass_box.setStyleSheet("background:#f6f6f6;color:#000000; border-radius:15")
        self.pass_box.setEchoMode(qtw.QLineEdit.Password)

        self.login_button=qtw.QPushButton(self)
        self.login_button.setGeometry(474,362,249,54)
        self.login_button.setStyleSheet("background:#0855ff;color:white; border-radius: 25")
        self.login_button.setText("Log in")
        self.login_button.setFont(self.font_log)     
        self.login_button.clicked.connect(self.log_def)

        self.font_signup = qtg.QFont()
        self.font_signup.setFamily("Roboto")
        self.font_signup.setPointSize(12)

        self.signup_button = qtw.QPushButton(self)
        self.signup_button.setGeometry(663,420,53,23)
        self.signup_button.setText("signup")
        self.signup_button.setFont(self.font_signup)
        self.signup_button.clicked.connect(self.signup_def)
        self.signup_button.setStyleSheet("background:white;color:#0855ff;border-radius: 25")
    def log_def(self):
        user=self.user_box.text()
        bass=self.pass_box.text()  
        if data.Log_in(user,bass):
            self.parent.resize(1600,950)
            self.parent.setCurrentWidget(self.parent.home_page)
            list = data.get_data_user(user)
            # obj = person.Person(list[0], list[1], list[2], list[3], list[4], list[5], list[6])
            self.parent.cmail.set_first_name(list[0])
            self.parent.home_page.hiname.setText(list[0])
            self.parent.cmail.set_last_name(list[1])
            self.parent.cmail.set_email(list[2])
            self.parent.cmail.set_password(list[3])
            self.parent.cmail.set_phone(list[4])
            self.parent.cmail.set_current_car(list[5])
            self.parent.cmail.set_past_car(list[6])
            self.parent.account_page.fname_lab.setText(self.parent.cmail.get_frist_name())
            self.parent.account_page.lname_lab.setText(self.parent.cmail.get_last_name())
            self.parent.account_page.email_lab.setText(self.parent.cmail.get_email())
            self.parent.account_page.phone_lab.setText(self.parent.cmail.get_phone())
            self.parent.account_page.pass_lab.setText(self.parent.cmail.get_password())

        else:
            self.la.setText("sorry we don't recognize this account")
                    
    def signup_def(self):
        self.parent.resize(800,800)
        self.parent.setCurrentWidget(self.parent.signup_page)