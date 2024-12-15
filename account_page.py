import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg
import sys
import user as data
import person
class account_page(qtw.QTabWidget):
    def __init__(self, parent) :
        super().__init__(parent)
        self.parent=parent
        self.setGeometry(100,200,1600,950)
        self.setStyleSheet("background-image:url(source/account_page.png)")
        
        self.back_button=qtw.QPushButton(self)
        self.back_button.setStyleSheet("background-image:url(source/back); border-radius: 16")
        self.back_button.setGeometry(1404,24,171,80)
        self.back_button.clicked.connect(self.back_def)
        
        self.delete_button=qtw.QPushButton(self)
        self.delete_button.setStyleSheet("background-image:url(source/delete); border-radius: 16")
        self.delete_button.setGeometry(668,685,373,80)
        self.delete_button.clicked.connect(self.delete_def)
        
        self.edit_button=qtw.QPushButton(self)
        self.edit_button.setStyleSheet("background-image:url(source/edit); border-radius: 16")
        self.edit_button.setGeometry(169,685,171,80)
        self.edit_button.clicked.connect(self.edit_def)
        
        self.save_button=qtw.QPushButton(self)
        self.save_button.setStyleSheet("background-image:url(source/save); border-radius: 16")
        self.save_button.setGeometry(169,685,171,80)
        self.save_button.clicked.connect(self.save_def)
        self.save_button.setVisible(False)

        self.fontbox = qtg.QFont()
        self.fontbox.setFamily("Roboto")
        self.fontbox.setPointSize(30)
        self.fontbox.setBold(True)
        
        self.fname_lab=qtw.QLabel(self)
        self.fname_lab.setGeometry(103,176,428,78)
        self.fname_lab.setFont(self.fontbox)
        self.fname_lab.setStyleSheet("background:white;color:#0855ff;")
        
        self.fname_box=qtw.QLineEdit(self)
        self.fname_box.setGeometry(103,176,428,78)
        self.fname_box.setFont(self.fontbox)
        self.fname_box.setStyleSheet("background:#f6f6f6;color:#000000; border-radius:16")
        
        self.lname_lab=qtw.QLabel(self)
        self.lname_lab.setGeometry(613,176,428,73)
        self.lname_lab.setFont(self.fontbox)
        self.lname_lab.setStyleSheet("background:white;color:#0855ff;")
        
        self.lname_box=qtw.QLineEdit(self)
        self.lname_box.setGeometry(613,176,428,73)
        self.lname_box.setFont(self.fontbox)
        self.lname_box.setStyleSheet("background:#f6f6f6;color:#000000; border-radius:16")
        
        self.email_lab=qtw.QLabel(self)
        self.email_lab.setGeometry(103,291,428,73)
        self.email_lab.setFont(self.fontbox)
        self.email_lab.setStyleSheet("background:white;color:#0855ff;")
        
        self.email_box=qtw.QLineEdit(self)
        self.email_box.setGeometry(103,291,428,73)
        self.email_box.setFont(self.fontbox)
        self.email_box.setStyleSheet("background:#f6f6f6;color:#000000; border-radius:16")
        
        self.phone_lab=qtw.QLabel(self)
        self.phone_lab.setGeometry(613,291,428,73)
        self.phone_lab.setFont(self.fontbox)
        self.phone_lab.setStyleSheet("background:white;color:#0855ff;")
        
        self.phone_box=qtw.QLineEdit(self)
        self.phone_box.setGeometry(613,291,428,73)
        self.phone_box.setFont(self.fontbox)
        self.phone_box.setStyleSheet("background:#f6f6f6;color:#000000; border-radius:16")
        
        self.pass_lab=qtw.QLabel(self)
        self.pass_lab.setGeometry(103,407,428,73)
        self.pass_lab.setFont(self.fontbox)
        self.pass_lab.setStyleSheet("background:white;color:#0855ff;")
       
        self.pass_box=qtw.QLineEdit(self)
        self.pass_box.setGeometry(103,407,428,73)
        self.pass_box.setFont(self.fontbox)
        self.pass_box.setStyleSheet("background:#f6f6f6;color:#000000; border-radius:16")

        self.fname_lab.setText(self.parent.cmail.get_frist_name())
        self.lname_lab.setText(self.parent.cmail.get_last_name())
        self.email_lab.setText(self.parent.cmail.get_email())
        self.phone_lab.setText(self.parent.cmail.get_phone())
        self.pass_lab.setText(self.parent.cmail.get_password())

        self.fname_box.setVisible(False)
        self.lname_box.setVisible(False)
        self.email_box.setVisible(False)
        self.phone_box.setVisible(False)
        self.pass_box.setVisible(False)
    def back_def(self):
        self.parent.setCurrentWidget(self.parent.home_page)
    
    def delete_def(self):
        self.parent.resize(800,600)
        self.parent.setCurrentWidget(self.parent.login_page)
    
    def edit_def(self):
        self.fname_box.setVisible(True)
        self.lname_box.setVisible(True)
        self.email_box.setVisible(True)
        self.phone_box.setVisible(True)
        self.pass_box.setVisible(True)
        self.fname_box.setText(self.fname_lab.text())
        self.lname_box.setText(self.lname_lab.text())
        self.email_box.setText(self.email_lab.text())
        self.phone_box.setText(self.phone_lab.text())
        self.pass_box.setText(self.pass_lab.text())
        self.save_button.setVisible(True)
        
    def save_def(self):
        self.fname_box.setVisible(False)
        self.lname_box.setVisible(False)
        self.email_box.setVisible(False)
        self.phone_box.setVisible(False)
        self.pass_box.setVisible(False)
        self.save_button.setVisible(False)
        self.fname_lab.setText(self.fname_box.text())
        self.lname_lab.setText(self.lname_box.text())
        self.email_lab.setText(self.email_box.text())
        self.phone_lab.setText(self.phone_box.text())
        self.pass_lab.setText(self.pass_box.text())
