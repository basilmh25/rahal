import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg
import sys
import user as data
import person
import cars
import car

class state_page(qtw.QTabWidget):
    def __init__(self, parent) :
        super().__init__(parent)
        self.parent=parent
        self.setGeometry(100,200,1600,950)
        self.setStyleSheet("background-image:url(source/car state.png)")
        
        self.back_button=qtw.QPushButton(self)
        self.back_button.setStyleSheet("background-image:url(source/back); border-radius: 16")
        self.back_button.setGeometry(1404,24,171,80)
        self.back_button.clicked.connect(self.back_def)
        self.car_index=0
        self.carss = cars.get_data_car()
        self.parent.rent_page.car_generate(self.carss)

        self.fontbox = qtg.QFont()
        self.fontbox.setFamily("Roboto")
        self.fontbox.setPointSize(30)
        self.fontbox.setBold(True)

        self.count_days=qtw.QLineEdit(self)
        self.count_days.setGeometry(678,806,152,82)
        self.count_days.setStyleSheet("color:black;background:white;border-radius: 16")
        self.count_days.setFont(self.fontbox)

        self.rent_button=qtw.QPushButton(self)
        self.rent_button.setGeometry(991,806,260,82)
        self.rent_button.setStyleSheet("background-image:url(source/rent state.png);;border-radius: 16")
        self.arrt=[]
        for x in range(14):
            temp=qtw.QLabel(self)
            temp.setFont(self.fontbox)
            temp.setText("hello")
            temp.setStyleSheet("color:#0855ff;background:white")
            self.arrt.append(temp)
        self.arrt[0].setGeometry(25,125,562,73)
        self.arrt[1].setGeometry(1093,135,167,56)
        self.arrt[2].setGeometry(218,203,250,41)
        self.arrt[3].setGeometry(164,250,250,41)
        self.arrt[4].setGeometry(265,294,250,41)
        self.arrt[5].setGeometry(216,340,250,41)
        self.arrt[6].setGeometry(290,386,250,41)
        self.arrt[7].setGeometry(290,430,250,41)
        self.arrt[8].setGeometry(281,477,250,41)
        self.arrt[9].setGeometry(281,522,250,41)
        self.arrt[10].setGeometry(278,566,250,41)
        self.arrt[11].setGeometry(170,611,250,41)
        self.arrt[12].setGeometry(255,655,250,41)
        self.arrt[13].setGeometry(233,699,250,41)

            
    def refresh(self,llist):
        for xx in range(14):
            self.arrt[xx].setText(llist[xx])
        

    def back_def(self):
        self.parent.setCurrentWidget(self.parent.rent_page)

