import sqlite3 
con=sqlite3.connect("Car_Database.dp")
cursor = con.cursor()

cursor.execute(""" 
        CREATE TABLE IF NOT EXISTS Cars (
        car_id INTEGER PRIMARY KEY AUTOINCREMENT, 
        model TEXT NOT NULL UNIQUE,                       
        manufacturer TEXT NOT NULL UNIQUE,               
        year_of_manufacture INTEGER NOT NULL,     
        engine_size FLOAT ,              
        horsepower INTEGER ,              
        top_speed FLOAT ,                 
        acceleration FLOAT ,              
        number_of_doors INTEGER ,         
        number_of_seats INTEGER ,         
        fuel_capacity FLOAT ,            
        drivetrain TEXT ,                 
        gearbox_type TEXT ,               
        safety_rating INTEGER ,           
        satisfy_rating INTEGER ,          
        rental_history BOOLEAN,                  
        tenant_count INTEGER,                     
        rental_status BOOLEAN ,           
        rental_until DATE,                        
        price INTEGER ,                   
        features TEXT, 
        satisfaction_rating INTEGER                                
       )
    """)


#Add The Data In The Table  ->None It means NO Peroble If Not Add  
def Add_Car(model, manufacturer, year_of_manufacture, engine_size=None, horsepower=None, top_speed=None, 
            acceleration=None, number_of_doors=None, number_of_seats=None, fuel_capacity=None, drivetrain=None, 
            gearbox_type=None, safety_rating=None, satisfy_rating=None, rental_history=None, tenant_count=None, 
            rental_status=None, rental_until=None, price=None, features=None, satisfaction_rating=None):
      
      if not model or not manufacturer or not year_of_manufacture:
          print("Error:The model or manufacture or year_manufacture isn't exist")
          return
      
      list_of_numbers=[engine_size, horsepower, top_speed, acceleration, number_of_doors, number_of_seats,fuel_capacity, safety_rating, satisfy_rating, price]
      for number in list_of_numbers:
          if number is not None and number<0:
              print(f"Error The value of {number} is negative")
              return
          
      engine_size = engine_size if engine_size is not None else 0.0
      horsepower = horsepower if horsepower is not None else 0
      top_speed = top_speed if top_speed is not None else 0.0
      acceleration = acceleration if acceleration is not None else 0.0
      number_of_doors = number_of_doors if number_of_doors is not None else 4
      number_of_seats = number_of_seats if number_of_seats is not None else 5
      fuel_capacity = fuel_capacity if fuel_capacity is not None else 0.0
      safety_rating = safety_rating if safety_rating is not None else 0
      satisfy_rating = satisfy_rating if satisfy_rating is not None else 0
      price = price if price is not None else 0
      tenant_count = tenant_count if tenant_count is not None else 0
      satisfaction_rating=satisfaction_rating if satisfaction_rating is not None else 0
      rental_history=rental_history if rental_history is not None else True
      rental_status=rental_status if rental_status is not None else True
      features=features if features is not None else ''
      drivetrain=drivetrain if drivetrain is not None else''
      rental_until=rental_until if rental_until is not None else ''
      gearbox_type=gearbox_type if gearbox_type is not None else ''


      with sqlite3.connect("Car_Database.dp") as con:
        cursor = con.cursor()
        try:
           cursor.execute("""
              INSERT INTO Cars (
                  model, manufacturer, year_of_manufacture, engine_size, horsepower, top_speed, acceleration,
                  number_of_doors, number_of_seats, fuel_capacity, drivetrain, gearbox_type, safety_rating,
                  satisfy_rating, rental_history, tenant_count, rental_status, rental_until, price, features, satisfaction_rating
                  ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ? ,? ,?)""",
                 (model, manufacturer, year_of_manufacture, engine_size, horsepower, top_speed, acceleration,
                  number_of_doors, number_of_seats, fuel_capacity, drivetrain, gearbox_type, safety_rating,
                  satisfy_rating, rental_history, tenant_count, rental_status, rental_until, price, features, satisfaction_rating))
        except sqlite3.Error as e:
            print(f"Error: The car Add is fail becouse {e} ")


#Delete The Car
def Delete_Car(model):
    with sqlite3.connect("Car_Database.dp") as con:
        cursor = con.cursor()
        cursor.execute("SELECT *FROM Cars WHERE model = ?", (model,))
        car=cursor.fetchall()
        if not car :
            print(f"No car found with model {model} to delete.")
            return
        try:  
            cursor.execute("Delete From Cars where model= ? ",(model,))
            print(f"The row of model :{model} is deleted successfully")
            con.commit()
        except sqlite3.Error as e:
           print (f"No Car deleted becouse {e}")
            

#Show The Data of The Car  
def Show_all_data_of_car(model):
    with sqlite3.connect("Car_Database.dp") as con:
        cursor = con.cursor()
        cursor.execute("SELECT *FROM Cars WHERE model = ?", (model,))
        description = cursor.fetchall() 
        try: 
         if description :
           for Row in description : 
                print(f"""                         -----------------------The car_id = {Row[0]}--------------------------------            
                          model = {Row[1]} , manufacturer = {Row[2]}, year_of_manufacture = {Row[3]},
                          engine_size = {Row[4]}, horsepower = {Row[5]} , top_speed = {Row[6]}, acceleration = {Row[7]},
                          number_of_doors = {Row[8]}, number_of_seats = {Row[9]}, fuel_capacity = {Row[10]}, drivetrain = {Row[11]}, 
                          gearbox_type = {Row[12]}, safety_rating = {Row[13]},satisfy_rating = {Row[14]}, rental_history = {Row[15]},
                          tenant_count = {Row[16]}, rental_status = {Row[17]}, rental_until = {Row[18]}, price = {Row[19]}, features = {Row[20]}
                          ----------------------------------------------------------------------""")
         else:
             print("No cars found with that model or the table is empty")  
        except sqlite3.Error as e:
            print(f"Error: The Show Data fail becouse {e}  ")

def Show_all_cars_of_table():
    with sqlite3.connect("Car_Database.dp") as con:
        cursor = con.cursor()
        cursor.execute("SELECT *FROM Cars")
        data = cursor.fetchall() 
        try: 
         if  data :
           print(f"The Table has {len( data)} of Cars")
           for Row in  data : 
              
                print(f"""                         -----------------------The car_id = {Row[0]}--------------------------------            
                          model = {Row[1]} , manufacturer = {Row[2]}, year_of_manufacture = {Row[3]},
                          engine_size = {Row[4]}, horsepower = {Row[5]} , top_speed = {Row[6]}, acceleration = {Row[7]},
                          number_of_doors = {Row[8]}, number_of_seats = {Row[9]}, fuel_capacity = {Row[10]}, drivetrain = {Row[11]}, 
                          gearbox_type = {Row[12]}, safety_rating = {Row[13]},satisfy_rating = {Row[14]}, rental_history = {Row[15]},
                          tenant_count = {Row[16]}, rental_status = {Row[17]}, rental_until = {Row[18]}, price = {Row[19]}, features = {Row[20]}
                          ----------------------------------------------------------------------""")
         else:
             print("The Table is empty")  
        except sqlite3.Error as e:
            print(f"Error: The Show Data fail becouse {e}  ")              

#update all
def Update_all(model,name_column,new_value):
 
    with sqlite3.connect("Car_Database.dp") as con:
       cursor = con.cursor()
       All_Coulmns=[ "model", "manufacturer", "year_of_manufacture", "engine_size", "horsepower", 
                     "top_speed", "acceleration", "number_of_doors", "number_of_seats", "fuel_capacity",
                     "drivetrain", "gearbox_type", "safety_rating", "satisfy_rating", "rental_history",
                     "tenant_count", "rental_status", "rental_until", "price", "features", "satisfaction_rating"]
 
 
       if name_column not in All_Coulmns:
          print(f"The {name_column} is not exist in All_Columns ")
          return
       elif new_value==None:
            print(f"Error: The  new_value for {name_column} can not be {new_value} ")
            return
       else:      
         try:
            cursor.execute(f"UPDATE Cars SET {name_column} = ? WHERE model = ? ", (new_value,model)) 
            print(f"The value of coulmn {name_column} was successfully update")
         except sqlite3.Error as e:
            print(f"Error: The update fail becouse {e} ")


Add_Car("gfgfgfg","fggfg",22222)
Add_Car("fgdgfjk","dfs",5555)
Show_all_data_of_car("gfgfgfg")
Show_all_cars_of_table()
