from datetime import datetime
import customtkinter

class CompanyModel:
    
    name: str
    address: str
    phone_number: str
    email_address: str
    city: str
    country: str
    
    def __init__(self, Name: str, Address: str, Phone_Number: str, Email_Address: str, City: str, Country: str) -> None:
        self.name = Name
        self.address = Address
        self.phone_number = Phone_Number
        self.email_address = Email_Address
        self.city = City
        self.country = Country

class Ticket:
    
    id: int
    
    def __init__(self, ID) -> None:
        self.id = ID
    
    def initID(self):
        now = datetime.now()
        myId = now.strftime('%H%M%S') * 2
        return myId
    
    def new_ticket(self, name, address, phone_number, email_address, city, country):
        newTicket: CompanyModel = CompanyModel(name, address, phone_number, email_address, city, country)
        return print(newTicket)
    
    def run_app(self):
        print('Hello to Ticketing App')
        name = input('Type Name: ')
        address = input('Type address: ')
        phone_number = input('Type Phone Number: ')
        email_address = input('Type email address: ')
        city = input('Type City: ')
        country = input('Type Country: ')
        self.new_ticket(name, address, phone_number, email_address, city, country)

class App(customtkinter.CTk):
    def __init__(self) -> None:
        super().__init__()
        
        self.title('my app')
        self.geometry('800x600')
        self.grid_columnconfigure((0,1), weight=1)
        
        self.button = customtkinter.CTkButton(self, text='Save', command=self.button_callback)
        self.button.grid(row=0, column=0, pady=20, sticky='ew', columnspan=2)
    
    def button_callback(self):
        print('button pressed')
    

if __name__ == '__main__':
    app = App()
    app.mainloop()