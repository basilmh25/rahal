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


def Add_firstname():
    pass

# Add new user -> use in sign up
def Add_User(firstname, email, password, lastname = None, phone = None):
    try:
        cursor.execute("INSERT INTO users VALUES (? ,? ,?, ?, ?)", (firstname, lastname, email, password, phone))
    except:
        print("The Email or Password or user_id is exist")

# Gitting email -> use in log in
def Log_in(user,password):
    login = cursor.execute("SELECT firstname, password FROM users")
    data = login.fetchall()
    for a in data:
        if user == a[0]:
            if password==a[1]:
                return True
    return False


# print(Log_in('Ahme', 'password123'))
con.commit()
# con.close()