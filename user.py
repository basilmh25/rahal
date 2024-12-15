import sqlite3

con = sqlite3.connect("DataBase.db")
cursor = con.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        firstname TEXT NOT NULL,
        lastname TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL,
        phone TEXT NOT NULL,
        current_car TEXT,
        past_car TEXT
    )
""")

con.commit()
con.close()


# return list from datauser long in
def get_data_user(email):
    with sqlite3.connect("DataBase.db") as con:
        cursor = con.cursor()
        d = cursor.execute("SELECT * FROM users where email = ?", (email,))
        data = d.fetchone()
        return list(data[1:])


# Add new user -> use in sign up
def Add_User(firstname, lastname, email, password, phone):
    with sqlite3.connect("DataBase.db") as con:
        cursor = con.cursor()
        try:
            cursor.execute("INSERT INTO users (firstname, lastname, email, password, phone) VALUES (? ,? ,?, ?, ?)",
                    (firstname, lastname, email, password, phone))
        except:
            print("Email already exists")

# Gitting email -> use in log in
def Log_in(email,password):
    with sqlite3.connect("DataBase.db") as con:
        cursor = con.cursor()
        login = cursor.execute("SELECT password FROM users WHERE email = ?", (email,))
        data = login.fetchone()

        if data is None:
            return False

        if password==data[0]:
            return True
        return False


def check_email(email):
    with sqlite3.connect("DataBase.db") as con:
        cursor = con.cursor()
        em = cursor.execute("SELECT email FROM users")
        data = em.fetchall()
        for a in data:
            if(email == a[0]):
                return False
        return True


# Update first name -> used by send the new name and send email
def Update_firstname(email, new_name = ""):
    with sqlite3.connect("DataBase.db") as con:
        cursor = con.cursor()
        if len(new_name) != 0:
            cursor.execute("UPDATE users SET firstname = ? WHERE email = ? ", (new_name, email))


# Update last name -> used by send the new name and send email
def Update_lastname(email, new_name = ""):
    with sqlite3.connect("DataBase.db") as con:
        cursor = con.cursor()
        if len(new_name) != 0:
            cursor.execute("UPDATE users SET lastname = ? WHERE email = ? ", (new_name, email))


# Update password name -> used by send the new password and send email
def Update_password(email, new_password = "" ):
    with sqlite3.connect("DataBase.db") as con:
        cursor = con.cursor()
        if len(new_password) != 0:
            cursor.execute("UPDATE users SET password = ? WHERE email = ? ", (new_password, email))


# Update phone name -> used by send the new phone and send email
def Update_phone(email, new_phone = ""):
    with sqlite3.connect("DataBase.db") as con:
        cursor = con.cursor()
        if len(new_phone) != 0:
            cursor.execute("UPDATE users SET phone = ? WHERE email = ? ", (new_phone, email))


# convert the value current_car into value past_car -> used by send email and id new car
def Update_Current_car(email, id_car = ""):
    with sqlite3.connect("DataBase.db") as con:
        cursor = con.cursor()
        if len(id_car) != 0:
            cursor.execute("UPDATE users SET past_car = current_car WHERE email = ?", (email,))
            cursor.execute("UPDATE users SET current_car = ? WHERE email = ?", (id_car, email))



# delet user -> used by send email
def Delete_user(email):
    with sqlite3.connect("DataBase.db") as con:
        cursor = con.cursor()
        cursor.execute("DELETE FROM users WHERE email = ?", (email,))
