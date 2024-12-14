from datetime import datetime
class car:
    def __init__(self):
        self.Engine_size = None
        self.Num_Doors = None
        self.Num_Seats = None
        self.Top_Speed = None
        self.Horsepower = None
        self.Fuel_Capacity = None
        self.Drivetrain = None
        self.Safety_Rating = None
        self.Satisfy_Rating = None
        self.Hental_History = None
        self.Tenant_Count = None
        self.Gearbox_Type = None
        self.Acceleration = None
        self.Features = None
        self.Rental_Status = None
        self.Rental_To = None
        self.Price = None
        self.Model = None
        self.Made = None
        self.Year_Car = None
        

    def Set_Engine_Size(self, engine_size):
        if isinstance(engine_size, (float, int)) and engine_size > 0:
            self.Engine_size = float(engine_size)
        else:
            raise ValueError("Engine size must be a positive float value.")
    def Get_Engine_Size(self):
        if self.Engine_size is None:
            return "Engine size is not set yet."
        return self.Engine_size
    
    def Set_Num_Doors(self, num_doors):
        if isinstance(num_doors, int) and num_doors > 0:
            self.Num_Doors = num_doors
        else:
            raise ValueError("Number of doors must be a positive integer.")
    def Get_Num_Doors(self):
        if self.Num_Doors is None:
            return "Numbers of doors is not set yet."
        return self.Num_Doors

    def Set_Num_Seats(self, num_seats):
        if isinstance(num_seats, int) and num_seats > 0:
            self.Num_Seats = num_seats
        else:
            raise ValueError("Number of seats must be a positive integer.")
    def Get_Num_Seats(self):
        if self.Num_Seats is None:
            return "Number of seats is not set yet."
        return self.Num_Seats

    def Set_Top_Speed(self, top_speed):
        if isinstance(top_speed, float) and top_speed > 0:
            self.Top_Speed = top_speed
        else:
            raise ValueError("Top speed must be a positive float value.")
    def Get_Top_Speed(self):
        if self.Top_Speed is None:
            return "Top speed is not set yet."
        return self.Top_Speed

    def Set_Horsepower(self, horsepower):
        if isinstance(horsepower, int) and horsepower > 0:
            self.Horsepower = horsepower
        else:
            raise ValueError("Horsepower must be a positive integer.")
    def Get_Horsepower(self):
        if self.Horsepower is None:
            return "Horsepower is not set yet."
        return self.Horsepower

    def Set_Fuel_Capacity(self, fuel_capacity):
        if isinstance(fuel_capacity, float) and fuel_capacity > 0:
            self.Fuel_Capacity = fuel_capacity
        else:
            raise ValueError("Fuel capacity must be a positive float value.")
    def Get_Fuel_Capacity(self):
        if self.Fuel_Capacity is None:
            return "Fuel capacity is not set yet."
        return self.Fuel_Capacity

    def Set_Drivetrain(self, drivetrain):
        valid_drivetrains = ["FWD", "RWD", "AWD", "4WD"]
        if isinstance(drivetrain, str) and drivetrain.upper() in valid_drivetrains:
            self.Drivetrain = drivetrain.upper()
        else:
            raise ValueError(f"Drivetrain must be one of the following: {', '.join(valid_drivetrains)}.")
    def Get_Drivetrain(self):
        if self.Drivetrain is None:
           return "Drivetrain is not set yet."
        return self.Drivetrain
    
    def Set_Safety_Rating(self, safety_rating):
        if isinstance(safety_rating, int) and 1 <= safety_rating <= 5:
            self.Safety_Rating = safety_rating
        else:
            raise ValueError("Safety rating must be an integer between 1 and 5.")
    def Get_Safety_Rating(self):
        if self.Safety_Rating is None:
            return "Safty_Rating is not set yet."
        return self.Safety_Rating

    def Set_Satisfy_Rating(self, satisfy_rating):
        if isinstance(satisfy_rating, int) and 1 <= satisfy_rating <= 5:
            self.Satisfy_Rating = satisfy_rating
        else:
            raise ValueError("Satisfy rating must be an integer between 1 and 5.")
    def Get_Satisfy_Rating(self):
        if self.Satisfy_Rating is None:
            return "Satisfy_Rating is not set yet."
        return self.Satisfy_Rating

    def Set_Rental_History(self, rental_history):
        if isinstance(rental_history, bool):
            self.Rental_History = rental_history
        else:
            raise ValueError("Rental history must be a boolean value (True or False).")
    def Get_Rental_History(self):
        if self.Rental_History is None:
            return "Rental_History is not set yet."
        return self.Rental_History
    
    def Set_Tenant_Count(self, tenant_count):
        if isinstance(tenant_count, int) and tenant_count >= 0:
            self.Tenant_Count = tenant_count
        else:
            raise ValueError("Tenant count must be a non-negative integer.")
    def Get_Tenant_Count(self):
        if self.Tenant_Count is None:
            return "Tenant_Count is not set yet."
        return self.Tenant_Count
    
    def Set_Gearbox_Type(self, gearbox_type):
        if isinstance(gearbox_type, str) and gearbox_type.strip():
            self.Gearbox_Type = gearbox_type.strip()
        else:
            raise ValueError("Gearbox type must be a non-empty string.")
    def Get_Gearbox_Type(self):
        if self.Gearbox_Type is None:
            return "Gearbox_Type is not set yet."
        return self.Gearbox_Type
    
    def Set_Acceleration(self, acceleration):
        if isinstance(acceleration, (float, int)) and acceleration > 0:
            self.Acceleration = float(acceleration)
        else:
            raise ValueError("Acceleration must be a positive number.")
    def Get_Acceleration(self):
        if self.Acceleration is None:
            return "Acceleration is not set yet."
        return self.Acceleration
    
    def Set_Features(self, features):
        if isinstance(features, list):
            self.Features = features
        else:
            raise ValueError("Features must be a list.")
    def Get_Features(self):
        if self.Features is None:
            return "Features is not set yet."
        return self.Features

    def Set_Rental_Status(self, rental_status):
        if isinstance(rental_status, bool):
            self.Rental_Status = rental_status
        else:
            raise ValueError("Rental status must be a boolean.")
    def Get_Rental_Status(self):
        if self.Rental_Status is None:
            return "Rental_Status is not set yet."
        return self.Rental_Status
    
    def Set_Rental_To(self, rental_to):
        if isinstance(rental_to, str):
            try:
                self.Rental_To = datetime.strptime(rental_to, '%Y-%m-%d').date()
            except ValueError:
                raise ValueError("Date must be in 'YYYY-MM-DD' format.")
        elif isinstance(rental_to, datetime):
            self.Rental_To = rental_to.date()
        else:
            raise ValueError("Rental To must be a string (YYYY-MM-DD) or a datetime object.")
    def Get_Rental_To(self):
        if self.Rental_To is None:
            return "Rental to is not set yet."
        return self.Rental_To

    def Set_Price(self, price):
        if isinstance(price, int) and price > 0:
            self.Price = price
        else:
            raise ValueError("Price must be a positive integer.")
    def Get_Price(self):
        if self.Price is None:
            return "Price is not set yet."
        return self.Price

    def Set_Model(self, model):
        if isinstance(model, str) and model.strip():
            self.Model = model
        else:
            raise ValueError("Model must be a non-empty string.")
    def Get_Model(self):
        if self.Model is None:
            return "Model is not set yet."
        return self.Model

    def Set_Made(self, made):
        if isinstance(made, str) and made.strip():
            self.Made = made
        else:
            raise ValueError("Manufacturer must be a non-empty string.")
    def Get_Made(self):
        if self.Made is None:
            return "The made is not set yet."
        return self.Made

    def Set_Year_Car(self, year_car):
        if isinstance(year_car, str) and len(year_car) == 4 and year_car.isdigit():
            self.Year_Car = year_car
        else:
            raise ValueError("Year must be a 4-digit string representing the year of manufacture.")
    def Get_Year_Car(self):
        if self.Year_Car is None:
            return "Year_Car is not set yet."
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

