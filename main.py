from tkinter import *
from tkinter import messagebox 
import random as r
import string
import json

my_password = ''


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
   
def pasword_gen():
        global my_password
        my_password_entry.delete(0, END)
        cha = characters.get()
        num = numbers.get()
        esp = especial.get()
        
        password = []
        
        for _ in range(int(cha)):
            a = r.choice(string.ascii_letters)
            password.append(a)
        
        for _ in range(int(num)):
            b = r.choice(string.digits)
            password.append(b)
        
        for _ in range(int(esp)):
            c = r.choice(string.punctuation)
            password.append(c)
            
        r.shuffle(password)
        generated_password = ''.join(password)
        my_password_entry.insert(0,generated_password)   
                 
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    mymail = mail.get()
    mypage = page.get()
    mypass = my_password_entry.get()
    new_data = {mypage: {
        "email": mymail,
        "password": mypass
    }}
    try:
        with open("data.json","r") as file_data:
            #read old data
            data = json.load(file_data)
            #update old data
            data.update(new_data)
            
            with open("data.json","w") as file_data:
                #saving data 
                json.dump(data, file_data, indent=4)
            
    except FileNotFoundError:
        with open("data.json","w") as file_data:
            json.dump(new_data, file_data, indent=4)
        
# ---------------------------- SHOW PASSWORD SETUP -----------------------#  
def password_searcher():
    mypage = page.get()
    with open("data.json","r") as file_data:
        data = json.load(file_data) 
    try:
        if mypage in data:
            email = data[mypage]["email"]
            password = data[mypage]["password"]
            messagebox.showinfo(title=mypage, message=f"Email: {email}\nPassword: {password}")
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
            
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.config(padx=125, pady=50)


canvas = Canvas(width=300, height=200)
logo = PhotoImage(file= "logo.png")
canvas.create_image(100,100, image = logo)
canvas.place(x=-160, y=-30)

char_text = Label(text="Characters", font=("Arial", 11, "bold"))
char_text.grid(column=2, row=1)

number_text = Label(text="Numbers", font=("Arial", 11, "bold"))
number_text.grid(column=2, row=2)

especial_text = Label(text="Especial Symbol", font=("Arial", 11, "bold"))
especial_text.grid(column=2, row=3)

mail_text = Label(text="Enter the E-MAIL", font=("Arial", 11, "bold"))
mail_text.grid(column=2, row=4)

page_text = Label(text="Enter the WEB PAGE", font=("Arial", 11, "bold"))
page_text.grid(column=2, row=5)

my_password = Label(text=my_password, font=("Arial", 11, "bold"))
my_password.grid(column=3, row= 3)


# entry char#
characters = Entry(width=3)
characters.grid(column=3, row=1)

numbers = Entry(width=3)
numbers.grid(column=3, row=2)

especial = Entry(width=3)
especial.grid(column=3, row=3)

mail = Entry(width=20)
mail.grid(column=3, row=4)

page = Entry(width=20)
page.grid(column=3, row=5)

generator_password = Button(text="Generate Password", command=pasword_gen)
generator_password.grid(column=2, row=6)

add_password = Button(text="add", command=save_password, width = 18)
add_password.grid(column=2, row=7)

search_password = Button(text="search", command=password_searcher, width = 18)
search_password.grid(column=3, row=7)

my_password_entry = Entry(width=20)
my_password_entry.grid(column=3, row=6)

window.mainloop()