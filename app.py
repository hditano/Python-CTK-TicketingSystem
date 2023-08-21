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
        
        self.button1 = customtkinter.CTkButton(self, text='Create Database', command=self.button_create_database)
        self.button1.grid(row=0, column=0, pady=20, sticky='ew', columnspan=2)
        self.button2 = customtkinter.CTkButton(self, text='Insert Data', command=self.add_data)
        self.button2.grid(row=1, column=0, pady=20, sticky='ew', columnspan=2)
    
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