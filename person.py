import pandas as pd

class Person:

    def __init__(self):
        self.first_name = None
        self.last_name = None
        self.email = None
        self.password = None
        self.phone = None
        self.current_car = None
        self.past_car = None

    def set_first_name(self, fname):
        self.first_name = fname

    def set_last_name(self, lname):
        self.last_name = lname

    def set_email(self, email):
        self.email = email

    def set_phone(self, phone):
        self.phone = phone

    def set_current_car(self, c_car):
        self.current_car = c_car

    def set_past_car(self, p_car):
        self.past_car = p_car

    def set_password(self,password):
        self.Pass=password


    def get_frist_name(self):
        return self.first_name
    def get_last_name(self):
        return self.last_name
    def get_email(self):
        return self.email
    def get_phone(self):
        return self.phone
    def get_current_car(self):
        return self.current_car
    def get_password(self):
        return self.password