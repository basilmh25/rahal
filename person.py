import pandas as pd

file_path = r"C:\Users\almaktab alhandasy\OneDrive\Desktop\اسلام حسن يحيى رمضان sec2\a.xlsx"

locations_df = pd.read_excel(file_path)
class Person:
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
        return self.Pass


    def add_to_dataframe(self, df):
        new_row = pd.DataFrame({
            'First name': [self.first_name],
            'Last name': [self.last_name],
            'Email': [self.email],
            'Phone': [self.phone],
            'Current Car': [self.current_car],
            'Past Car': [self.past_car],
            'Password':[self.Pass]
        })
        updated_df = pd.concat([df, new_row], ignore_index=True)
        return updated_df

    def search_by_email(df, email):
        results = df[df['Email'].str.contains(email, case=False, na=False)]
        if results.empty:
            print(f"No results found for email '{email}'.")
            return None
        results = results.drop(columns=['Password'])
        return results

fname = input("Enter your first name: ")
lname = input("Enter your last name: ")
email = input("Enter your email: ")
phone = input("Enter your phone: ")
current_car = input("Enter your current car: ")
past_car = input("Enter your past car: ")
password=input("Enter the password:")

person = Person()
person.set_first_name(fname)
person.set_last_name(lname)
person.set_email(email)
person.set_phone(phone)
person.set_current_car(current_car)
person.set_past_car(past_car)
person.set_password(password)

locations_df = person.add_to_dataframe(locations_df)

locations_df.to_excel(file_path, index=False)
print("Information successfully added to the file!")

search_email = input("Enter the email to search for: ")
email_results = Person.search_by_email(locations_df, search_email)

if email_results is not None:
    print("Search Results:")
    print(email_results)
else:
    print("The email not found")
