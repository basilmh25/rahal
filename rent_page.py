import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg
import sys
import user as data
import person

class car_frame:
    def __init__(self,obj,textname,textpd,textrate,year):
        self.obj=obj
        self.textname=textname
        self.textpd=textpd
        self.textrate=textrate
        self.year=year
    def view(self):
        self.obj.setVisible(True)
        self.textname.setVisible(True)
        self.textpd.setVisible(True)
        self.textrate.setVisible(True)
        self.year.setVisible(True)
    def hide(self):
        self.obj.setVisible(False)
        self.textname.setVisible(True)
        self.textpd.setVisible(True)
        self.textrate.setVisible(True)
        self.year.setVisible(False)
        

class rent_page(qtw.QTabWidget):
    def __init__(self, parent) :
        super().__init__(parent)
        self.parent=parent
        self.setGeometry(100,200,1600,950)
        self.setStyleSheet("background-image:url(source/rent_page.png)")
        
        self.back_button=qtw.QPushButton(self)
        self.back_button.setStyleSheet("background-image:url(source/back); border-radius: 16")
        self.back_button.setGeometry(1404,24,171,80)
        self.back_button.clicked.connect(self.back_def)

        self.car_ind=0
        self.car_generate(0)
        self.frame_list[0].view()   
        self.frame_list[1].view()   
        self.frame_list[2].view()    

        self.next_b=qtw.QPushButton(self)
        self.next_b.setGeometry(614,832,82,65)
        self.next_b.setStyleSheet("background-image:url(source/next_button); border-radius: 15")
        self.next_b.clicked.connect(self.next_button)

        self.prv_b=qtw.QPushButton(self)
        self.prv_b.setGeometry(495,832,82,65)
        self.prv_b.setStyleSheet("background-image:url(source/prv_button); border-radius: 15")
        self.prv_b.clicked.connect(self.prv_button)

    def back_def(self):
        self.parent.setCurrentWidget(self.parent.home_page)
    def car_generate(self,listcar):
        # self.x_f=80
        # self.w_f=1031
        # self.h_f=184
        # self.y_f=201
        self.font_h = qtg.QFont()
        self.font_h.setFamily("Roboto")
        self.font_h.setPointSize(40)
        self.font_h.setBold(True)
        self.font_p = qtg.QFont()
        self.font_p.setFamily("Roboto")
        self.font_p.setPointSize(20)
        self.font_p.setBold(True)
        self.font_r = qtg.QFont()
        self.font_r.setFamily("Roboto")
        self.font_r.setPointSize(20)
        self.font_r.setBold(True)
        self.font_y = qtg.QFont()
        self.font_y.setFamily("Roboto")
        self.font_y.setPointSize(40)
        self.font_y.setBold(True)
        self.inc_y_f=216
        self.frame_list=[]
        for tt in range(3):#(len(listcar)):
            self.car_ind+=1
            temp =qtw.QLabel(self)
            temp.setStyleSheet("background-image:url(source/frame_car.png);border-radius:15")
            temp.setGeometry(80,201+self.inc_y_f*tt,1031,184)
            temp.setVisible(False)

            tempht=qtw.QLabel(self)
            tempht.setText("toyota crolla")
            tempht.setVisible(False)
            tempht.setGeometry(95,227+self.inc_y_f*tt,369,70)
            tempht.setFont(self.font_h)
            tempht.setStyleSheet("background:#0855ff;color:white")

            temphr=qtw.QLabel(self)
            temphr.setText('5.0')
            temphr.setVisible(False)
            temphr.setGeometry(482,328+self.inc_y_f*tt,42,42)
            temphr.setFont(self.font_r)
            temphr.setStyleSheet("background:#000000;color:white")
  
            temphp=qtw.QLabel(self)
            temphp.setText('70')
            temphp.setVisible(False)
            temphp.setGeometry(213,328+self.inc_y_f*tt,42,42)
            temphp.setFont(self.font_p)
            temphp.setStyleSheet("background:#000000;color:white")

            yeartemp=qtw.QLabel(self)
            yeartemp.setText("2020")
            yeartemp.setVisible(False)
            yeartemp.setGeometry(947,232+self.inc_y_f*tt,137,53)
            yeartemp.setFont(self.font_y)
            yeartemp.setStyleSheet("background:#0855ff;color:white")
            
            tempobj=car_frame(temp,tempht,temphp,temphr,yeartemp)
            self.frame_list.append(tempobj)
        for tt in range(3):
            temp =qtw.QPushButton(self)
            temp.setStyleSheet("background-image:url(source/rent_button.png);border-radius:15")
            temp.setGeometry(945,326+self.inc_y_f*tt,148,47)
            self.frame_list.append(temp)
            if(tt<len(self.frame_list)):
                self.setVisible(False)  
    def rent1(self,ind):
        pass
    def rent2(self,ind):
        pass
    def rent3(self,ind):
        pass
    def next_button(self):
        for x in range(3):
            if(self.car_ind<len(self.frame_list)):
                self.frame_list[self.car_ind-2].hide()
                self.frame_list[self.car_ind].view() 
                self.car_ind+=1

    def prv_button(self):
        for x in range(3):
            if(self.car_ind<len(self.frame_list)):
                self.frame_list[self.car_ind-2].view()
                self.frame_list[self.car_ind].hide()
                self.car_ind-=1
        