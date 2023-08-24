from datetime import datetime
import customtkinter
from peewee import *
import os


db = SqliteDatabase('database.db')

class Company(Model):
    
    name: str = CharField()
    address: str = CharField()
    phone_number: str = CharField()
    email_address: str = CharField()
    city: str = CharField()
    country: str = CharField()
    
    class Meta:
        database = db
    
class Ticket:
    
    def new_ticket(self):
        pass

        
class MyTab(customtkinter.CTkTabview):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        
        name_input = customtkinter.StringVar()
        
        self.add('View Data')
        self.add('New Data')
        
        self.label_tab1 = customtkinter.CTkLabel(master=self.tab('View Data'), text='View Data')
        
        self.label_tab2 = customtkinter.CTkLabel(master=self.tab('New Data'), text='New Data')
         
        self.label_name = customtkinter.CTkLabel(master=self.tab('New Data'), text='Company Name', fg_color='transparent')
        self.label_name.grid(row=0, column=0, sticky='ew', padx=20)
        self.input_name = customtkinter.CTkEntry(master=self.tab('New Data'), placeholder_text='Company')
        self.input_name.grid(row=0, column=1, pady=5)
        name_input = self.input_name.get()
        print(name_input)
        
        self.label_address = customtkinter.CTkLabel(master=self.tab('New Data'), text='Address', fg_color='transparent')
        self.label_address.grid(row=1, column=0, sticky='ew', padx=20)
        self.input_address = customtkinter.CTkEntry(master=self.tab('New Data'), placeholder_text='Address')
        self.input_address.grid(row=1, column=1, pady=5)
        
        self.label_phone_number = customtkinter.CTkLabel(master=self.tab('New Data'), text='Phone Number', fg_color='transparent')
        self.label_phone_number.grid(row=2, column=0, sticky='ew', padx=20)
        self.input_phone_number = customtkinter.CTkEntry(master=self.tab('New Data'), placeholder_text='1234-1234')
        self.input_phone_number.grid(row=2, column=1, pady=5)
        
        self.label_email_address = customtkinter.CTkLabel(master=self.tab('New Data'), text='email address', fg_color='transparent')
        self.label_email_address.grid(row=3, column=0, sticky='ew', padx=20)
        self.input_email_address = customtkinter.CTkEntry(master=self.tab('New Data'), placeholder_text='email@mail.com')
        self.input_email_address.grid(row=3, column=1, pady=5)
        
        self.label_city = customtkinter.CTkLabel(master=self.tab('New Data'), text='City', fg_color='transparent')
        self.label_city.grid(row=4, column=0, sticky='ew', padx=20)
        self.input_city = customtkinter.CTkEntry(master=self.tab('New Data'), placeholder_text='Type City')
        self.input_city.grid(row=4, column=1, pady=5)
        
        self.label_country = customtkinter.CTkLabel(master=self.tab('New Data'), text='Country', fg_color='transparent')
        self.label_country.grid(row=5, column=0, sticky='ew', padx=20)
        self.input_country = customtkinter.CTkEntry(master=self.tab('New Data'), placeholder_text='country..')
        self.input_country.grid(row=5, column=1, pady=5)
        


class Utilities:
    def button_create_database(self):
        database = db
        if os.path.exists('database.db'):
            print('Database already exists..')
        else:
            print('Connecting to Database..')
            db.connect()
            print('Creating Tables')
            db.create_tables([Company])
            print('Tables Created')
    
    def add_data(self, data):
        print(f'Hello {data}')
        
class App(customtkinter.CTk):
    def __init__(self) -> None:
        super().__init__()
        
        self.title('my app')
        self.geometry('500x350')
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.columnconfigure(3, weight=1)
        self.resizable(0,0)
        
        self.tab_view = MyTab(master=self)
        self.tab_view.grid(row=0, column=0)
        
        self.button1 = customtkinter.CTkButton(self, text='Create Database', command=Utilities().button_create_database, width=20)
        self.button1.grid(row=6, column=1, sticky='nw', ipadx=100)
        self.button1.place(x=50, y=300)
        if os.path.exists('database.db'):
            self.button1.configure(state='disabled')
            
        self.button2 = customtkinter.CTkButton(self, text='Insert Data', command=Utilities().add_data)
        self.button2.grid(row=6, column=2, sticky='nw')
        self.button2.place(x=170, y=300)

if __name__ == '__main__':
    app = App()
    app.mainloop()