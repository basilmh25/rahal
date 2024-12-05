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
        phone TEXT NOT NULL
    )
""")

# Add new user -> use in sign up
def Add_User(firstname, lastname, email, password, phone):
    with sqlite3.connect("DataBase.db") as con:
        cursor = con.cursor()
        try:
            cursor.execute("INSERT INTO users (firstname, lastname, email, password, phone) VALUES (? ,? ,?, ?, ?)",
                    (firstname, lastname, email, password, phone))
        except:
            print("The Email or Password isn't exist")


# Gitting email -> use in log in
def Log_in(email,password):
    with sqlite3.connect("DataBase.db") as con:
        cursor = con.cursor()
        login = cursor.execute("SELECT email, password FROM users")
        data = login.fetchall()
        for a in data:
            if email == a[0]:
                if password==a[1]:
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