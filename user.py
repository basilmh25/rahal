import sqlite3

con = sqlite3.connect("DataBase.db")
cursor = con.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        firstname TEXT NOT NULL,
        lastname TEXT,
        email TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL,
        phone TEXT
    )
""")

# Add new user -> use in sign up
def Add_User(firstname, email, password, lastname = None, phone = None):
    with sqlite3.connect("DataBase.db") as con:
        cursor = con.cursor()
        try:
            cursor.execute("INSERT INTO users (firstname, lastname, email, password, phone) VALUES (? ,? ,?, ?, ?)", 
                    (firstname, lastname, email, password, phone))
        except:
            print("The Email or Password is exist")


# Gitting email -> use in log in
def Log_in(user,password):
    with sqlite3.connect("DataBase.db") as con:
        cursor = con.cursor()
        login = cursor.execute("SELECT email, password FROM users")
        data = login.fetchall()
        # print(data)
        for a in data:
            if user == a[0]:
                if password==a[1]:
                    return True
        return False
    
# login = cursor.execute("SELECT email, password FROM users")
# data = login.fetchall()
# print(data)