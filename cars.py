import sqlite3 
import car
con=sqlite3.connect("DataBase.db")
cursor = con.cursor()

cursor.execute(""" 
        CREATE TABLE IF NOT EXISTS Car (
        car_id INTEGER PRIMARY KEY AUTOINCREMENT,  
        Model TEXT NOT NULL UNIQUE,                       
        Made TEXT NOT NULL,               
        Year_Car INTEGER NOT NULL,     
        Price INTEGER ,                   
        Engine_size FLOAT ,              
        Horsepower INTEGER ,              
        Fuel_Capacity FLOAT ,            
        Drivetrain TEXT ,                 
        Top_Speed FLOAT ,                 
        Acceleration FLOAT ,              
        Num_Doors INTEGER ,         
        Num_Seats INTEGER ,         
        Gearbox_Type TEXT ,               
        Safety_Rating INTEGER ,           
        Satisfy_Rating INTEGER ,          
        Hental_History BOOLEAN,                  
        Tenant_Count INTEGER,                     
        Rental_Status BOOLEAN ,           
        Rental_To DATE,                        
        Features TEXT                         
        )
    """)

con.commit()
con.close()
# con.commit()
# con.close()



#Add The Data In The Table  ->None It means NO Peroble If Not Add  
def Add_Car(Model, Made, Year_Car, Engine_size=None, Horsepower=None, Top_Speed=None, 
            Acceleration=None, Num_Doors=None,Num_Seats=None, Fuel_Capacity=None, Drivetrain=None, 
            Gearbox_Type=None,Safety_Rating=None, Satisfy_Rating=None,Hental_History=None, Tenant_Count=None, 
            Rental_Status=None, Rental_To=None, Price=None, Features=None):

    if not Model or not Made or not Year_Car:
        print("Error:The Model or manufacture or year_manufacture isn't exist")
        return

    list_of_numbers=[Engine_size, Horsepower, Top_Speed, Acceleration, Num_Doors,Num_Seats,Fuel_Capacity,Safety_Rating, Satisfy_Rating, Price]
    for number in list_of_numbers:
        if number is not None and number<0:
            print(f"Error The value of {number} is negative")
            return

    Engine_size = Engine_size if Engine_size is not None else 0.0
    Horsepower = Horsepower if Horsepower is not None else 0
    Top_Speed = Top_Speed if Top_Speed is not None else 0.0
    Acceleration = Acceleration if Acceleration is not None else 0.0
    Num_Doors = Num_Doors if Num_Doors is not None else 4
    Num_Seats =Num_Seats if Num_Seats is not None else 5
    Fuel_Capacity = Fuel_Capacity if Fuel_Capacity is not None else 0.0
    Safety_Rating =Safety_Rating if Safety_Rating is not None else 0
    Satisfy_Rating = Satisfy_Rating if Satisfy_Rating is not None else 0
    Price = Price if Price is not None else 0
    Tenant_Count = Tenant_Count if Tenant_Count is not None else 0
    Hental_History=Hental_History if Hental_History is not None else True
    Rental_Status=Rental_Status if Rental_Status is not None else True
    Features=Features if Features is not None else ''
    Drivetrain=Drivetrain if Drivetrain is not None else''
    Rental_To=Rental_To if Rental_To is not None else ''
    Gearbox_Type=Gearbox_Type if Gearbox_Type is not None else ''


    with sqlite3.connect("DataBase.db") as con:
        cursor = con.cursor()
        try:
            cursor.execute("""
                INSERT INTO Car (
                Model, Made, Year_Car, Engine_size, Horsepower, Top_Speed, Acceleration,
                Num_Doors,Num_Seats, Fuel_Capacity, Drivetrain, Gearbox_Type,Safety_Rating,
                Satisfy_Rating,Hental_History, Tenant_Count, Rental_Status, Rental_To, Price, Features
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ? ,? ,?)""",
                (Model, Made, Year_Car, Engine_size, Horsepower, Top_Speed, Acceleration,
                Num_Doors,Num_Seats, Fuel_Capacity, Drivetrain, Gearbox_Type,Safety_Rating,
                Satisfy_Rating,Hental_History, Tenant_Count, Rental_Status, Rental_To, Price, Features))
            con.commit()

        except sqlite3.Error as e:
            print(f"Error: The car Add is fail becouse {e} ")


#Delete The Car
def Delete_Car(Model):
    with sqlite3.connect("DataBase.db") as con:
        cursor = con.cursor()
        cursor.execute("SELECT *FROM Car WHERE Model = ?", (Model,))
        car=cursor.fetchall()
        if not car :
            print(f"No car found with Model {Model} to delete.")
            return
        try:  
            cursor.execute("Delete From Car where Model= ? ",(Model,))
            print(f"The row of Model :{Model} is deleted successfully")
            con.commit()
        except sqlite3.Error as e:
            print (f"No Car deleted becouse {e}")



#update all
def Update_all(Model,name_column,new_value):

    with sqlite3.connect("DataBase.db") as con:
        cursor = con.cursor()
        All_Coulmns=[ "Model", "Made", "Year_Car", "Engine_size", "Horsepower", 
                        "Top_Speed", "Acceleration", "Num_Doors", "number_of_seats", "Fuel_Capacity",
                        "Drivetrain", "Gearbox_Type", "safety_rating", "Satisfy_Rating", "rental_history",
                        "Tenant_Count", "Rental_Status", "Rental_To", "Price", "Features"]


        if name_column not in All_Coulmns:
            print(f"The {name_column} is not exist in All_Columns ")
            return
        elif new_value==None:
            print(f"Error: The  new_value for {name_column} can not be {new_value} ")
            return
        else:      
            try:
                cursor.execute(f"UPDATE Car SET {name_column} = ? WHERE Model = ? ", (new_value,Model)) 
                print(f"The value of coulmn {name_column} was successfully update")
            except sqlite3.Error as e:
                print(f"Error: The update fail becouse {e} ")



def get_data_car():
    with sqlite3.connect("DataBase.db") as con:
        list_frame = []
        cursor = con.cursor()
        d = cursor.execute("SELECT * FROM Car")
        data = d.fetchall()
        
        for a in data:
            temp = car.car()
            temp.Set_Model(a[1])
            temp.Set_Made(a[2])
            temp.Set_Year_Car(a[3])
            temp.Set_Price(a[4])
            temp.Set_Engine_Size(a[5])
            temp.Set_Horsepower(a[6])
            temp.Set_Fuel_Capacity(a[7])
            temp.Set_Drivetrain(a[8])
            temp.Set_Top_Speed(a[9])
            temp.Set_Acceleration(a[10])
            temp.Set_Num_Doors(a[11])
            temp.Set_Num_Seats(a[12])
            temp.Set_Gearbox_Type(a[13])
            temp.Set_Safety_Rating(a[14])
            temp.Set_Satisfy_Rating(a[15])
            temp.Set_Rental_History(a[16])
            temp.Set_Tenant_Count(a[17])
            temp.Set_Rental_Status(a[18])
            temp.Set_Rental_To(a[19])
            temp.Set_Features(a[20])

            list_frame.append(temp)
        
        return list_frame

