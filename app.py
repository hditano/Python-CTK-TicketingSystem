from datetime import datetime
import customtkinter
from peewee import *


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
        print('Hello to Ticketing App')
        name = input('Type Name: ')
        address = input('Type address: ')
        phone_number = input('Type Phone Number: ')
        email_address = input('Type email address: ')
        city = input('Type City: ')
        country = input('Type Country: ')
        new_ticket = Company.create(name=name, address=address, phone_number=phone_number, email_address=email_address, city=city, country=country)
        new_ticket.save()
        
class App(customtkinter.CTk):
    def __init__(self) -> None:
        super().__init__()
        
        self.title('my app')
        self.geometry('800x600')
        self.grid_columnconfigure((0,1), weight=1)
       
        self.label_name = customtkinter.CTkLabel(self, text='Company Name', fg_color='transparent')
        self.label_name.grid(row=0, column=0, sticky='ew', padx=20)
        self.input_name = customtkinter.CTkEntry(self, placeholder_text='Company')
        self.input_name.grid(row=0, column=1, pady=5)
        
        self.label_address = customtkinter.CTkLabel(self, text='Address', fg_color='transparent')
        self.label_address.grid(row=1, column=0, sticky='ew', padx=20)
        self.input_address = customtkinter.CTkEntry(self, placeholder_text='Address')
        self.input_address.grid(row=1, column=1, pady=5)
        
        self.label_phone_number = customtkinter.CTkLabel(self, text='Phone Number', fg_color='transparent')
        self.label_phone_number.grid(row=2, column=0, sticky='ew', padx=20)
        self.input_phone_number = customtkinter.CTkEntry(self, placeholder_text='1234-1234')
        self.input_phone_number.grid(row=2, column=1, pady=5)
        
        self.label_email_address = customtkinter.CTkLabel(self, text='email address', fg_color='transparent')
        self.label_email_address.grid(row=3, column=0, sticky='ew', padx=20)
        self.input_email_address = customtkinter.CTkEntry(self, placeholder_text='email@mail.com')
        self.input_email_address.grid(row=3, column=1, pady=5)
        
        self.label_city = customtkinter.CTkLabel(self, text='City', fg_color='transparent')
        self.label_city.grid(row=4, column=0, sticky='ew', padx=20)
        self.input_city = customtkinter.CTkEntry(self, placeholder_text='Type City')
        self.input_city.grid(row=4, column=1, pady=5)
        
        self.label_country = customtkinter.CTkLabel(self, text='Country', fg_color='transparent')
        self.label_country.grid(row=5, column=0, sticky='ew', padx=20)
        self.input_country = customtkinter.CTkEntry(self, placeholder_text='country..')
        self.input_country.grid(row=5, column=1, pady=5)
        
        self.button1 = customtkinter.CTkButton(self, text='Create Database', command=self.button_create_database, width=20)
        self.button1.grid(row=6, column=0, pady=10, padx=20, sticky='ew', columnspan=1)
        self.button2 = customtkinter.CTkButton(self, text='Insert Data', command=self.add_data)
        self.button2.grid(row=7, column=0, pady=10, padx=20, sticky='ew', columnspan=1)
    
    def button_create_database(self):
        database = db
        print('Connecting to Database..')
        db.connect()
        print('Creating Tables')
        db.create_tables([Company])
        print('Tables Created')
    
    def add_data(self):
        myTicket = Ticket()
        myTicket.new_ticket()   

if __name__ == '__main__':
    app = App()
    app.mainloop()