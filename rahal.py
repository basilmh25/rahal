import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg
import sys
import log_in_page
import sign_up_page
import home_page

class app(qtw.QStackedWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("rahal")
        self.setGeometry(100,200,800,600)
        #pages
        self.login_page = log_in_page.window(self)
        self.signup_page=sign_up_page.signup(self)
        self.home_page= home_page.home_page(self)
        self.addWidget(self.login_page)
        self.addWidget(self.signup_page)
        self.addWidget(self.home_page)
        self.setCurrentWidget(self.login_page)
        

exe=qtw.QApplication(sys.argv)
rahal_app=app()
rahal_app.show()
sys.exit(exe.exec_())
        