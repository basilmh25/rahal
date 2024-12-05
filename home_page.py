import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg
import sys
import user as data

class home_page(qtw.QTabWidget):
    def __init__(self, parent) :
        super().__init__(parent)
        self.parent=parent
        self.setGeometry(100,200,1600,950)
        self.setStyleSheet("background-image:url(source/home_page.png)")
