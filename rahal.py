import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg
import sys
import log_in_page
import sign_up_page
import home_page
import account_page
import nocar_page
import person
import rent_page
import statecar
import cars
import statecar2

class app(qtw.QStackedWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("rahal")
        self.setGeometry(100,200,800,600)
        self.cmail=person.Person()
        #pages
        self.login_page = log_in_page.window(self)
        self.signup_page=sign_up_page.signup(self)
        self.home_page= home_page.home_page(self)
        self.account_page= account_page.account_page(self)
        self.no_car=nocar_page.nocar_page(self)
        self.rent_page=rent_page.rent_page(self)
        self.state_page=statecar.state_page(self)
        self.state_page2=statecar2.state_page(self)
        # self.carss = cars.get_data_car()
        

        self.addWidget(self.login_page)
        self.addWidget(self.signup_page)
        self.addWidget(self.home_page)
        self.addWidget(self.account_page)
        self.addWidget(self.no_car)
        self.addWidget(self.rent_page)
        self.addWidget(self.state_page)
        self.addWidget(self.state_page2)
        self.setCurrentWidget(self.login_page)

        

exe=qtw.QApplication(sys.argv)
rahal_app=app()
rahal_app.show()
sys.exit(exe.exec_())
        