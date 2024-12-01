import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg
import sys

class window(qtw.QTabWidget):
    def __init__(self):
        super().__init__()
        # self.
        self.setWindowTitle("rahal")
        self.setGeometry(100,200,800,600)
        self.setStyleSheet("background-image:url(source/background_login.png)")
        

        self.font_log = qtg.QFont()
        self.font_log.setFamily("Roboto")
        self.font_log.setPointSize(16)
        self.font_log.setBold(True)
        self.user_box=qtw.QLineEdit(self)
        self.user_box.setGeometry(440,201,318,54)
        self.user_box.setPlaceholderText("user name")
        self.user_box.setStyleSheet("background:#eaeaea;color:#000000; border-radius:15")
        self.user_box.setFont(self.font_log)
        
        self.la=qtw.QLabel(self)
        self.la.setGeometry(537,472,85,37)
        self.la.setStyleSheet("color:green;background:white")
        self.la.setFont(self.font_log)

        self.pass_box=qtw.QLineEdit(self)
        self.pass_box.setPlaceholderText("password")
        self.pass_box.setFont(self.font_log)
        self.pass_box.setGeometry(440 ,285 ,318 ,54 )
        self.pass_box.setStyleSheet("background:#eaeaea;color:#000000; border-radius:15")

        self.login_button=qtw.QPushButton(self)
        self.login_button.setGeometry(482,362,233,54)
        self.login_button.setStyleSheet("background:#0855ff;color:white; border-radius: 25")
        self.login_button.setText("Log in")
        self.login_button.setFont(self.font_log)     
        self.login_button.clicked.connect(self.log_def)
    def log_def(self):
        self.la.setText("True")   
        

app =qtw.QApplication(sys.argv)
main = window()
main.show()
sys.exit(app.exec_())