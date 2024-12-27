from datetime import datetime
class car:
    def _init_(self):
        # self.Car_Id=None
        self.Model = None
        self.Price = None
        self.Top_Speed = None
        self.Engine_size = None
        self.Num_Doors = None
        self.Num_Seats = None
        self.Horsepower = None
        self.Fuel_Capacity = None
        self.Drivetrain = None
        self.Safety_Rating = None
        self.Satisfy_Rating = None
        self.Acceleration = None
        self.Features = None
        self.Year_Car = None
        self.Tenant_Count = None
        self.Gearbox_Type = None
        self.Rental_History = None
        self.Rental_Status = None
        self.Rental_To = None
        self.Made = None


    # def Set_Car_Id (self, Car_Id):
    #     self.Car_Id = Car_Id

    # def Get_Car_Id(self):
    #     return self.Car_Id

    def Set_Engine_Size(self, engine_size):
            self.Engine_size = float(engine_size)

    def Get_Engine_Size(self):
        return self.Engine_size
    
    def Set_Num_Doors(self, num_doors):
            self.Num_Doors = num_doors

    def Get_Num_Doors(self):
        return self.Num_Doors

    def Set_Num_Seats(self, num_seats):
            self.Num_Seats = num_seats

    def Get_Num_Seats(self):
        return self.Num_Seats

    def Set_Top_Speed(self, top_speed):
            self.Top_Speed = top_speed

    def Get_Top_Speed(self):
        return self.Top_Speed

    def Set_Horsepower(self, horsepower):
            self.Horsepower = horsepower

    def Get_Horsepower(self):
        return self.Horsepower

    def Set_Fuel_Capacity(self, fuel_capacity):
            self.Fuel_Capacity = fuel_capacity

    def Get_Fuel_Capacity(self):
        return self.Fuel_Capacity

    def Set_Drivetrain(self, drivetrain):
            self.Drivetrain = drivetrain.upper()

    def Get_Drivetrain(self):
        return self.Drivetrain
    
    def Set_Safety_Rating(self, safety_rating):
            self.Safety_Rating = safety_rating

    def Get_Safety_Rating(self):
        return self.Safety_Rating

    def Set_Satisfy_Rating(self, satisfy_rating):
            self.Satisfy_Rating = satisfy_rating

    def Get_Satisfy_Rating(self):
        return self.Satisfy_Rating

    def Set_Rental_History(self, rental_history):
            self.Rental_History = rental_history

    def Get_Rental_History(self):
        return self.Rental_History
    
    def Set_Tenant_Count(self, tenant_count):
            self.Tenant_Count = tenant_count

    def Get_Tenant_Count(self):
        return self.Tenant_Count
    
    def Set_Gearbox_Type(self, gearbox_type):
            self.Gearbox_Type = gearbox_type.strip()

    def Get_Gearbox_Type(self):
        return self.Gearbox_Type
    
    def Set_Acceleration(self, acceleration):
            self.Acceleration = float(acceleration)

    def Get_Acceleration(self):
        return self.Acceleration
    
    def Set_Features(self, features):
            self.Features = features

    def Get_Features(self):
        return self.Features

    def Set_Rental_Status(self, rental_status):
            self.Rental_Status = rental_status

    def Get_Rental_Status(self):
        return self.Rental_Status
    
    def Set_Rental_To(self, rental_to):
            self.Rental_To = rental_to

    def Get_Rental_To(self):
        return self.Rental_To

    def Set_Price(self, price):
            self.Price = price

    def Get_Price(self):
        return self.Price

    def Set_Model(self, model):
            self.Model = model

    def Get_Model(self):
        return self.Model

    def Set_Made(self, made):
            self.Made = made

    def Get_Made(self):
        return self.Made

    def Set_Year_Car(self, year_car):
            self.Year_Car = year_car

    def Get_Year_Car(self):
        return self.Year_Car
    
    def Set_All(self, engine_size=None, num_doors=None, num_seats=None, top_speed=None, horsepower=None,
            fuel_capacity=None, drivetrain=None, safety_rating=None, satisfy_rating=None, rental_history=None,
            tenant_count=None, gearbox_type=None, acceleration=None, features=None, rental_status=None,
            rental_to=None, price=None, model=None, made=None, year_car=None):
        self.Set_Engine_Size(engine_size)
        self.Set_Num_Doors(num_doors)
        self.Set_Num_Seats(num_seats)
        self.Set_Top_Speed(top_speed)
        self.Set_Horsepower(horsepower)
        self.Set_Fuel_Capacity(fuel_capacity)
        self.Set_Drivetrain(drivetrain)
        self.Set_Safety_Rating(safety_rating)
        self.Set_Satisfy_Rating(satisfy_rating)
        self.Set_Rental_History(rental_history)
        self.Set_Tenant_Count(tenant_count)
        self.Set_Gearbox_Type(gearbox_type)
        self.Set_Acceleration(acceleration)
        self.Set_Features(features)
        self.Set_Rental_Status(rental_status)
        self.Set_Rental_To(rental_to)
        self.Set_Price(price)
        self.Set_Model(model)
        self.Set_Made(made)
        self.Set_Year_Car(year_car)
        
    def Get_All(self):
        return {
        "Engine_size": self.Get_Engine_Size(),
        "Num_Doors": self.Get_Num_Doors(),
        "Num_Seats": self.Get_Num_Seats(),
        "Top_Speed": self.Get_Top_Speed(),
        "Horsepower": self.Get_Horsepower(),
        "Fuel_Capacity": self.Get_Fuel_Capacity(),
        "Drivetrain": self.Get_Drivetrain(),
        "Safety_Rating": self.Get_Safety_Rating(),
        "Satisfy_Rating": self.Get_Satisfy_Rating(),
        "Hental_History": self.Get_Rental_History(),
        "Tenant_Count": self.Get_Tenant_Count(),
        "Gearbox_Type": self.Get_Gearbox_Type(),
        "Acceleration": self.Get_Acceleration(),
        "Features": self.Get_Features(),
        "Rental_Status": self.Get_Rental_Status(),
        "Rental_To": self.Get_Rental_To(),
        "Price": self.Get_Price(),
        "Model": self.Get_Model(),
        "Made": self.Get_Made(),
        "Year_Car": self.Get_Year_Car()
    }
    @staticmethod
    def get_all_data_car(self):
        a = []
        
        a.append(f"{self.Get_Made()} {self.Get_Model()}")
        a.append(f"{self.Get_Year_Car()}")
        a.append(f"{self.Get_Top_Speed()}")
        a.append(f"{self.Get_Num_Doors()}")
        a.append(f"{self.Get_Fuel_Capacity()}")
        a.append(f"{self.Get_Drivetrain()}")
        a.append(f"{self.Get_Satisfy_Rating()}")
        a.append(f"{self.Get_Tenant_Count()}")
        a.append(f"{self.Get_Gearbox_Type()}")
        a.append(f"{self.Get_Acceleration()}")
        a.append(f"{self.Get_Horsepower()}")
        a.append(f"{self.Get_Num_Seats()}")
        a.append(f"{self.Get_Engine_Size()}")
        a.append(f"{self.Get_Rental_To()}")
        
        return a