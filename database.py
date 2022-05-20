import sqlite3
from pathlib import Path

db = sqlite3.connect('mangement.db')  #database connection

def SetTables():
    db.execute("CREATE TABLE branch_data(branch_name text,phone text,address text)")
    db.execute("CREATE TABLE users(User_id INTEGER,First_name TEXT,Last_name TEXT,Date_Of_Birth TEXT,user_name TEXT,user_pass TEXT,priv INTEGER,phone_number TEXT,email TEXT,address TEXT,salary INTEGER,PRIMARY KEY(User_id))")
    db.execute("CREATE TABLE books(book_id INTEGER ,book_title TEXT,author_id INTEGER,language_id INTEGER,faculty_id INTEGER,category_id INTEGER, publisher_id INTEGER,book_price INTEGER,book_edition INTEGER,book_copies INTEGER,PRIMARY KEY(book_id),FOREIGN KEY(author_id) REFERENCES author(author_id),FOREIGN KEY(language_id) REFERENCES languages(language_id),FOREIGN KEY(publisher_id) REFERENCES publisher(publisher_id),FOREIGN KEY(category_id) REFERENCES categories(categories_id),FOREIGN KEY(faculty_id) REFERENCES faculties(faculty_id))")
    db.execute("CREATE TABLE author(author_id INTEGER ,author_name TEXT,PRIMARY KEY(author_id))")
    db.execute("CREATE TABLE audience(customer_id INTEGER,transaction_id INTEGER ,event_id INTEGER,ticket_id INTEGER,ticket_num INTEGER,PRIMARY KEY(customer_id),FOREIGN KEY(event_id) REFERENCES events(event_id),FOREIGN KEY(ticket_id) REFERENCES tickets(ticket_id),FOREIGN KEY(transaction_id) REFERENCES transactions(transaction_id))")
    db.execute("CREATE TABLE events(event_id INTEGER ,event_name TEXT,author_id INTEGER,event_date TEXT,PRIMARY KEY(event_id),FOREIGN KEY(author_id) REFERENCES author(author_id))")
    db.execute("CREATE TABLE transactions(transaction_id INTEGER,User_id INTEGER,book_id INTEGER,price INTEGER,quantity INTEGER,cash INTEGER,date TEXT,PRIMARY KEY(transaction_id),FOREIGN KEY(User_id) REFERENCES users(User_id),FOREIGN KEY(book_id) REFERENCES books(book_id),FOREIGN KEY(price) REFERENCES books(book_price))")
    db.execute("CREATE TABLE faculties(faculty_id INTEGER,faculty_name text,PRIMARY KEY(faculty_id))")
    db.execute("CREATE TABLE publisher(publisher_id INTEGER,Location TEXT,publisher_name TEXT,PRIMARY KEY(publisher_id))")
    db.execute("CREATE TABLE languages(languages_id INTEGER,languages_name TEXT,PRIMARY KEY(languages_id))")
    db.execute("CREATE TABLE tickets(tickets_id INTEGER,ticket_name TEXT,status TEXT,price INTEGER,quantity INTEGER,event_id INTEGER,PRIMARY KEY(tickets_id),FOREIGN KEY(event_id) REFERENCES events(event_id))")
    db.execute("CREATE TABLE categories(categories_id INTEGER,name TEXT,PRIMARY KEY(categories_id))")
    db.execute("CREATE TABLE copies(copies_id INTEGER,book_id INTEGER,PRIMARY KEY(copies_id))")
    db.execute("INSERT into users(User_id,First_name,Last_name,Date_Of_Birth,user_name,user_pass,priv,phone_number,email,address,salary)values(1,'Mustafa','Muhammed','23/7/2000','admin','admin',0,01554444247,'test@test.com','Cairo',5000)")
    db.commit()


def WriteData(order, data):
    db.execute(order, data)
    db.commit()

def DeleteData(order, data):
    db.execute(order, data)
    db.commit()



def ReadData(order):
    cr = db.cursor()
    getData = cr.execute(order)
    data = getData.fetchall()
    return data

def ReadLine(order,value):
    cr = db.cursor()
    getData = cr.execute(order,value)
    data = getData.fetchone()
    return data

def ReadDataV(order,value):
    cr = db.cursor()
    getData = cr.execute(order,value)
    data = getData.fetchall()
    return data
