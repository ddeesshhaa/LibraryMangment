#from ast import Or
#import string
import tkinter as tk
from tkinter import END, SINGLE, messagebox
from tokenize import Single
from pip import main
from tkcalendar import Calendar
import database
import datetime
import tables


day = datetime.datetime.today().strftime("%A")
today = datetime.date.today()
d1 = today.strftime("%Y/%m/%d")
cartItems = []
DataOfDB = ()
OrderOfDB = ""

def viewLang(showFrame, root):
    showFrame.tkraise()
    showFrame = tk.Frame(root, width=1000, height=550, bg='#318352')
    showFrame.place(x=300, y=200)
    def CurSelet(evt):
        if L1.curselection() != ():
            x = L1.get(L1.curselection())
            eventselect.set(x)
            authors = database.ReadLine("select * from languages where languages_name=?",[x])
            author = authors[0]  
            books = database.ReadData("select * from books")
            L2.delete(0,END)
            for i in books:
                if i[3]==author:
                    L2.insert(i[0], i[1])
                    L2.place(x=400, y=i[0]+80)
            
    tk.Label(showFrame, text="Choose Language", bg='#318352', fg='#D99A25',
             font=('calibri', 20, 'bold')).place(x=100, y=30)
    L1 = tk.Listbox(showFrame, width=25, height=18, bg='#318352',selectmode=SINGLE, borderwidth=0, highlightthickness=0, fg='#F2F2F2',
                    font=('calibri', 16, 'bold'))
    tk.Label(showFrame, text="Books", bg='#318352', fg='#D99A25',
             font=('calibri', 20, 'bold')).place(x=450, y=30)
    L2 = tk.Listbox(showFrame, width=25, height=18, bg='#318352',selectmode=Single, borderwidth=0, highlightthickness=0, fg='#F2F2F2',
                    font=('calibri', 16, 'bold'))

    faculties = database.ReadData("select * from languages")
    for i in range(len(faculties)):
        L1.insert(faculties[i][0], faculties[i][1])
        L1.place(x=30, y=i+80)

    L1.bind('<<ListboxSelect>>', CurSelet)
    eventselect = tk.StringVar(showFrame)

def viewFaCU(showFrame, root):
    showFrame.tkraise()
    showFrame = tk.Frame(root, width=1000, height=550, bg='#318352')
    showFrame.place(x=300, y=200)
    def CurSelet(evt):
        if L1.curselection() != ():
            def CurSelet1(evt):
                if L2.curselection() != ():
                    y = L2.get(L2.curselection())
                    ticketselect.set(y)
                    quant.set(books[9])
            x = L1.get(L1.curselection())
            eventselect.set(x)
            authors = database.ReadLine("select * from faculties where faculty_name=?",[x])
            author = authors[0]  
            books = database.ReadDataV("select * from books where faculty_id =?",[author])
            L2.delete(0,END)
            for i in range (len(books)):
                L2.insert(books[i][0], books[i][1])
                L2.place(x=400, y=i+80)
                L2.bind('<<ListboxSelect>>', CurSelet1)
       
    tk.Label(showFrame, text="Choose Faculty", bg='#318352', fg='#D99A25',
             font=('calibri', 20, 'bold')).place(x=100, y=30)
    L1 = tk.Listbox(showFrame, width=25, height=18, bg='#318352',selectmode=SINGLE, borderwidth=0, highlightthickness=0, fg='#F2F2F2',
                    font=('calibri', 16, 'bold'))
    tk.Label(showFrame, text="Books", bg='#318352', fg='#D99A25',
             font=('calibri', 20, 'bold')).place(x=450, y=30)
    L2 = tk.Listbox(showFrame, width=25, height=18, bg='#318352',selectmode=Single, borderwidth=0, highlightthickness=0, fg='#F2F2F2',
                    font=('calibri', 16, 'bold'))

    faculties = database.ReadData("select * from faculties")
    for i in range(len(faculties)):
        L1.insert(faculties[i][0], faculties[i][1])
        L1.place(x=30, y=i+80)

    L1.bind('<<ListboxSelect>>', CurSelet)
    eventselect = tk.StringVar(showFrame)
    ticketselect = tk.StringVar(showFrame)
    
    quant = tk.StringVar(showFrame)
    tk.Label(showFrame, text="Available : ", bg='#318352', fg='#D99A25',
             font=('calibri', 16, 'bold')).place(x=700, y=30)
    tk.Label(showFrame, textvariable=quant,  bg='#318352', fg='#D99A25',
             font=('calibri', 16, 'bold')).place(x=800, y=30)
    tk.Label(showFrame, text="Copies", bg='#318352', fg='#D99A25',
             font=('calibri', 16, 'bold')).place(x=850, y=30)

def viewCate(showFrame, root):
    showFrame.tkraise()
    showFrame = tk.Frame(root, width=1000, height=550, bg='#318352')
    showFrame.place(x=300, y=200)
    def CurSelet(evt):
        if L1.curselection() != ():
            def CurSelet1(evt):
                if L2.curselection() != ():
                    y = L2.get(L2.curselection())
                    ticketselect.set(y)
                    quant.set(books[9])
            x = L1.get(L1.curselection())
            eventselect.set(x)
            authors = database.ReadLine("select * from categories where name=?",[x])
            author = authors[0]  
            books = database.ReadDataV("select * from books where category_id =?",[author])
            L2.delete(0,END)
            for i in range (len(books)):
                L2.insert(books[i][0], books[i][1])
                L2.place(x=400, y=i+80)
                L2.bind('<<ListboxSelect>>', CurSelet1)
            
       
    tk.Label(showFrame, text="Choose category", bg='#318352', fg='#D99A25',
             font=('calibri', 20, 'bold')).place(x=100, y=30)
    L1 = tk.Listbox(showFrame, width=25, height=18, bg='#318352',selectmode=SINGLE, borderwidth=0, highlightthickness=0, fg='#F2F2F2',
                    font=('calibri', 16, 'bold'))
    tk.Label(showFrame, text="Books", bg='#318352', fg='#D99A25',
             font=('calibri', 20, 'bold')).place(x=450, y=30)
    L2 = tk.Listbox(showFrame, width=25, height=18, bg='#318352',selectmode=Single, borderwidth=0, highlightthickness=0, fg='#F2F2F2',
                    font=('calibri', 16, 'bold'))

    categories = database.ReadData("select * from categories")
    for i in range(len(categories)):
        L1.insert(categories[i][0], categories[i][1])
        L1.place(x=30, y=i+80)

    L1.bind('<<ListboxSelect>>', CurSelet)
    eventselect = tk.StringVar(showFrame)
    ticketselect = tk.StringVar(showFrame)
    
    quant = tk.StringVar(showFrame)
    tk.Label(showFrame, text="Available : ", bg='#318352', fg='#D99A25',
             font=('calibri', 16, 'bold')).place(x=700, y=30)
    tk.Label(showFrame, textvariable=quant,  bg='#318352', fg='#D99A25',
             font=('calibri', 16, 'bold')).place(x=800, y=30)
    tk.Label(showFrame, text="Copies", bg='#318352', fg='#D99A25',
             font=('calibri', 16, 'bold')).place(x=850, y=30)

def viewAuth(showFrame, root):
    showFrame.tkraise()
    showFrame = tk.Frame(root, width=1000, height=550, bg='#318352')
    showFrame.place(x=300, y=200)
    def CurSelet(evt):
        if L1.curselection() != ():
            def CurSelet1(evt):
                if L2.curselection() != ():
                    y = L2.get(L2.curselection())
                    ticketselect.set(y)
                    quant.set(books[9])
            x = L1.get(L1.curselection())
            eventselect.set(x)
            authors = database.ReadLine("select * from author where author_name=?",[x])
            author = authors[0]  
            books = database.ReadDataV("select * from books where author_id =?",[author])
            print(books)
            L2.delete(0,END)
            for i in range (len(books)):
                L2.insert(books[i][0], books[i][1])
                L2.place(x=400, y=i+80)
                L2.bind('<<ListboxSelect>>', CurSelet1)
        
       
        
    tk.Label(showFrame, text="Choose Author", bg='#318352', fg='#D99A25',
             font=('calibri', 20, 'bold')).place(x=100, y=30)
    L1 = tk.Listbox(showFrame, width=25, height=18, bg='#318352',selectmode=SINGLE, borderwidth=0, highlightthickness=0, fg='#F2F2F2',
                    font=('calibri', 16, 'bold'))
    tk.Label(showFrame, text="Books", bg='#318352', fg='#D99A25',
             font=('calibri', 20, 'bold')).place(x=450, y=30)
    L2 = tk.Listbox(showFrame, width=25, height=18, bg='#318352',selectmode=Single, borderwidth=0, highlightthickness=0, fg='#F2F2F2',
                    font=('calibri', 16, 'bold'))

    authors = database.ReadData("select * from author")
    for i in range(len(authors)):
        L1.insert(authors[i][0], authors[i][1])
        L1.place(x=30, y=i+80)

    L1.bind('<<ListboxSelect>>', CurSelet)
    eventselect = tk.StringVar(showFrame)
    ticketselect = tk.StringVar(showFrame)
    
    quant = tk.StringVar(showFrame)
    tk.Label(showFrame, text="Available : ", bg='#318352', fg='#D99A25',
             font=('calibri', 16, 'bold')).place(x=700, y=30)
    tk.Label(showFrame, textvariable=quant,  bg='#318352', fg='#D99A25',
             font=('calibri', 16, 'bold')).place(x=800, y=30)
    tk.Label(showFrame, text="Copies", bg='#318352', fg='#D99A25',
             font=('calibri', 16, 'bold')).place(x=850, y=30)

def paytickets(id,name,quan,price,cash,uid,evename):
    userid=uid
    events=database.ReadData("select * from events")
    for i in events:
        if i[1]==evename:
            eveid=i[0]
    data={(id,name,quan,price,cash,d1)}
    t=database.ReadData("select * from transactions")
    transid = len(t)+1

    x = (transid,userid,id,price, quan,cash, d1)
    tickts=database.ReadData("select * from tickets")
    for i in tickts:
        if id == i[0]:
            realquan = i[4]-quan
        
    aud=(userid,transid,eveid,id,quan)
    database.WriteData(
            "insert into transactions(transaction_id,user_id,book_id,price,quantity,cash,date)values(?,?,?,?,?,?,?)", x)
    database.WriteData(
            "update tickets set quantity = ? where tickets_id = ?", (realquan, id))

    database.WriteData("insert into audience(customer_id,transaction_id,event_id,ticket_id,ticket_num)values(?,?,?,?,?)",aud)
    messagebox.showinfo("Booked Successfully",
                        "Thanks for using our services !!")

def check_ticket(ids, quantity, state, showFrame, q,uid,eventselect):
    realquan = 0
    id = int(ids.get())-1
    quan = quantity.get()
    eventname=eventselect.get()
    
    data = database.ReadData("select * from tickets")
    for i in data:
        if (id+1 == int(i[0])):   
            realquan = i[4]
            

    if realquan < quan:
        messagebox.showinfo("Failed", "No Enough tickets")
    elif realquan >= quan:
        realquan -= quan
        totalprice = data[id][3] * quan
        x=str(totalprice)
        messagebox.showinfo("Total Cash", "Total cash is "+x+"L.E" )
        quantity.set("")
        state.set("")
        q.set(realquan)
        x = int(id)+1
        paytickets(x, data[id][1], quan, data[id][3], totalprice,uid,eventname)
        return realquan

def sellTickets(showFrame, root,uid):
    showFrame.tkraise()
    showFrame = tk.Frame(root, width=1000, height=550, bg='#318352')
    showFrame.place(x=300, y=200)

    def CurSelet(evt):
        if L1.curselection() != ():
            def CurSelet1(evt):
                if L2.curselection() != ():
                    y = L2.get(L2.curselection())
                    ticketselect.set(y)
                    tickets = database.ReadData("select * from tickets")
                    for i in tickets:
                        if i[1] == y:
                            ticket=i
                            quant.set(ticket[4])
                            ticketselect.set(ticket[0])
            x = L1.get(L1.curselection())
            eventselect.set(x)
            events = database.ReadData("select * from events")
            for i in events:
                if i[1] == x:
                    event = i  
            tickets = database.ReadData("select * from tickets")
            L2.delete(0,END)
            for i in range(len(tickets)):
                if (tickets[i][5]==event[0]):
                    L2.insert(tickets[i][0], tickets[i][1])
                    L2.place(x=400, y=i+80)
            L2.bind('<<ListboxSelect>>', CurSelet1)
        
       
        
    tk.Label(showFrame, text="Choose Event", bg='#318352', fg='#D99A25',
             font=('calibri', 20, 'bold')).place(x=100, y=30)
    L1 = tk.Listbox(showFrame, width=25, height=18, bg='#318352',selectmode=SINGLE, borderwidth=0, highlightthickness=0, fg='#F2F2F2',
                    font=('calibri', 16, 'bold'))
    tk.Label(showFrame, text="Choose Ticket", bg='#318352', fg='#D99A25',
             font=('calibri', 20, 'bold')).place(x=450, y=30)
    L2 = tk.Listbox(showFrame, width=25, height=18, bg='#318352',selectmode=Single, borderwidth=0, highlightthickness=0, fg='#F2F2F2',
                    font=('calibri', 16, 'bold'))

    events = database.ReadData("select * from events")
    for i in range(len(events)):
        L1.insert(events[i][0], events[i][1])
        L1.place(x=30, y=i+80)

    L1.bind('<<ListboxSelect>>', CurSelet)
    eventselect = tk.StringVar(showFrame)
    ticketselect = tk.StringVar(showFrame)
    
    quant = tk.StringVar(showFrame)
    tk.Label(showFrame, text="Available : ", bg='#318352', fg='#D99A25',
             font=('calibri', 16, 'bold')).place(x=700, y=30)
    tk.Label(showFrame, textvariable=quant,  bg='#318352', fg='#D99A25',
             font=('calibri', 16, 'bold')).place(x=800, y=30)
    tk.Label(showFrame, text="Enter Quantity",  bg='#318352', fg='#D99A25',
             font=('calibri', 16, 'bold')).place(x=700, y=100)
    tk.Label(showFrame, text="Tickets", bg='#318352', fg='#D99A25',
             font=('calibri', 16, 'bold')).place(x=850, y=30)
    quan = tk.IntVar(showFrame)
    tk.Entry(showFrame, textvariable=quan, width=15, bg='#262626', fg='#D99A25',
             font=('calibri', 16, 'bold')).place(x=900, y=100)
    state = tk.StringVar(showFrame)
    tk.Label(showFrame, textvariable=state, bg='#318352', fg='#D99A25',
             font=('calibri', 16, 'bold')).place(x=750, y=300)
    tk.Button(showFrame, text="Book Now", width=18, bg='#25403B', fg='#D99A25',
              font=('calibri', 16, 'bold'), command=lambda: [
                  check_ticket(ticketselect, quan, state, showFrame, quant,uid,eventselect)]).place(x=750, y=200)
    
def editttt(id,fname,lname,dob,uname,password,Privlage,phone,email,addr,Salary,rootreg,mid):
    id = id
    mainid=mid
    fname1 = fname.get()
    lname1 = lname.get()
    dob1   = dob.get()
    phone1 = phone.get()
    email1 = email.get()
    addr1  = addr.get()
    x = uname.get().strip().lower()
    y = password.get()
    priv=Privlage.get()
    sal=Salary.get()
    o=database.ReadLine("SELECT * from users where User_id=?",[mainid])
    mainu=o[4]
    mainpriv=o[6]
    order = "update users set First_name=?,Last_name=?,Date_Of_Birth=?,user_name=?,user_pass=?, priv=?,phone_number=?,email=?,address=?,salary=? WHERE user_id =?"
    d = (fname1,lname1,dob1,x,y,priv,phone1,email1,addr1,sal,id)
    database.WriteData(order,d)
    messagebox.showinfo("Success", "Done!")
    rootreg.destroy()
    start(mainid,mainu,mainpriv)

def edituse(usname,success,root,mainid):
    global DataOfDB
    global OrderOfDB
    
    username = usname.get().strip()
    if username == "":
        success.set("Enter Valid Data!!!")
    else:
        i = database.ReadLine("select * from users where user_name=?",[username])
        if not i:
            usname.set("")
            messagebox.showerror("Error","Username not found!!")
        else:
                if i[4]==username:
                    root.destroy()
                    rootreg = tk.Tk()
                    rootreg.title("Edit")
                    rootreg.state('zoomed')
                    rootreg.configure(bg="#318352")
                    rootreg.iconbitmap(r"icon.ico")
                    rootRegFrame=tk.Frame(rootreg,width = 1024 , height = 768 ,bg='#318352')
                    rootRegFrame.place(relx=0.5 , rely=0.5 , anchor = tk.CENTER)
                    id = i[0]
                    tk.Label(rootreg, text="First Name", bg='#318352', fg='#F5E0EC',
                            font=('calibri', 20, 'bold')).place(x=100, y=100)
                    
                    fname = tk.StringVar()
                    fname.set(i[1])
                    f=tk.Entry(rootreg, textvariable=fname, width=20,borderwidth=0,highlightthickness=0,bg='#595959', fg='#F5E0EC',
                            font=('calibri', 20, 'italic'))
                    f.place(x=350, y=100)

                    tk.Label(rootreg, text="Last Name", bg='#318352', fg='#F5E0EC',
                            font=('calibri', 20, 'bold')).place(x=800, y=100)
                    lname = tk.StringVar()
                    lname.set(i[2])
                    l=tk.Entry(rootreg, textvariable=lname, width=20,borderwidth=0,highlightthickness=0,bg='#595959', fg='#F5E0EC',
                            font=('calibri', 20, 'italic'))
                    l.place(x=1050, y=100)

                    tk.Label(rootreg, text="Date of Birth", bg='#318352', fg='#F5E0EC',
                            font=('calibri', 20, 'bold')).place(x=100, y=200)
                    dob = tk.StringVar()
                    dob.set(i[3])
                    d=tk.Entry(rootreg, textvariable=dob, width=20,borderwidth=0,highlightthickness=0,bg='#595959', fg='#F5E0EC',
                            font=('calibri', 20, 'italic'))
                    d.place(x=350, y=200)

                    tk.Label(rootreg, text="User Name", bg='#318352', fg='#F5E0EC',
                            font=('calibri', 20, 'bold')).place(x=800, y=200)
                    uname = tk.StringVar()
                    uname.set(i[4])
                    u=tk.Entry(rootreg, textvariable=uname, width=20,borderwidth=0,highlightthickness=0,bg='#595959', fg='#F5E0EC',
                            font=('calibri', 20, 'italic'))
                    u.place(x=1050, y=200)
                    
                    tk.Label(rootreg, text="password", bg='#318352', fg='#F5E0EC',
                            font=('calibri', 20, 'bold')).place(x=100, y=300)
                    password = tk.StringVar()
                    password.set(i[5])
                    p=tk.Entry(rootreg,textvariable=password, width=20,borderwidth=0,highlightthickness=0,bg='#595959', fg='#F5E0EC',
                            font=('calibri', 20, 'italic'))
                    p.place(x=350, y=300)

                    tk.Label(rootreg, text="Privlage", bg='#318352', fg='#F5E0EC',
                            font=('calibri', 20, 'bold')).place(x=800, y=300)
                    Privlage = tk.StringVar()
                    Privlage.set(i[6])
                    pr=tk.Entry(rootreg,textvariable=Privlage, width=20,borderwidth=0,highlightthickness=0,bg='#595959', fg='#F5E0EC',
                            font=('calibri', 20, 'italic'))
                    pr.place(x=1050, y=300)

                    tk.Label(rootreg, text="Phone", bg='#318352', fg='#F5E0EC',
                            font=('calibri', 20, 'bold')).place(x=100, y=400)
                    phone = tk.StringVar()
                    phone.set(i[7])
                    ph=tk.Entry(rootreg,textvariable=phone, width=20,borderwidth=0,highlightthickness=0,bg='#595959', fg='#F5E0EC',
                            font=('calibri', 20, 'italic'))
                    ph.place(x=350, y=400)
        
                    tk.Label(rootreg, text="Email", bg='#318352', fg='#F5E0EC',
                            font=('calibri', 20, 'bold')).place(x=800, y=400)
                    email = tk.StringVar()
                    email.set(i[8])
                    em=tk.Entry(rootreg,textvariable=email, width=20,borderwidth=0,highlightthickness=0,bg='#595959', fg='#F5E0EC',
                            font=('calibri', 20, 'italic'))
                    em.place(x=1050, y=400)

                    tk.Label(rootreg, text="Address", bg='#318352', fg='#F5E0EC',
                            font=('calibri', 20, 'bold')).place(x=100, y=500)
                    address = tk.StringVar()
                    address.set(i[9])
                    add=tk.Entry(rootreg,textvariable=address, width=20,borderwidth=0,highlightthickness=0,bg='#595959', fg='#F5E0EC',
                            font=('calibri', 20, 'italic'))
                    add.place(x=350, y=500)

                    tk.Label(rootreg, text="Salary", bg='#318352', fg='#F5E0EC',
                            font=('calibri', 20, 'bold')).place(x=800, y=500)
                    Salary = tk.StringVar()
                    Salary.set(i[10])
                    sa =tk.Entry(rootreg, textvariable=Salary, width=20,borderwidth=0,highlightthickness=0,bg='#595959', fg='#F5E0EC',
                            font=('calibri', 20, 'italic'))
                    sa.place(x=1050, y=500)
                            
                    tk.Button(rootreg, text="Submit",
                            command=lambda: editttt(id,fname,lname,dob,uname,password,Privlage,phone,email,address,Salary,rootreg,mainid), width=10, fg='#318352',
                            font=('calibri', 20, 'bold')).place(x=600, y=600)
           
def editUsers(showFrame, root,id):
    showFrame.tkraise()
    showFrame = tk.Frame(root, width=1000, height=550, bg='#318352')
    showFrame.place(x=300, y=200)

    tk.Label(showFrame, text="Enter User Name", bg='#318352', fg='#D99A25',
             font=('calibri', 16, 'bold')).place(x=50, y=30)
    usname = tk.StringVar(showFrame)
    tk.Entry(showFrame, textvariable=usname, width=20, borderwidth=0, highlightthickness=0, bg='#262626', fg='#D99A25',
             font=('calibri', 16, 'bold')).place(x=300, y=30)

    success = tk.StringVar(showFrame)
    
    tk.Button(showFrame, text="Edit", command=lambda: [edituse(usname,success,root,id)], width=20,fg='#D99A25',bg='#318352',
              font=('calibri', 16, 'bold')).place(x=250, y=100)

def addTick(ticket_name,ticket_price,ticket_quantity,event_name,success):
    global DataOfDB
    global OrderOfDB
    tname = ticket_name.get().strip().capitalize()
    tprice = ticket_price.get()
    tquan = ticket_quantity.get()
    evename=event_name.get().strip().capitalize()
    if tname == "":
        success.set("Enter Valid Data!!!")
    else:
        data = database.ReadData("select * from tickets")
        events= database.ReadData("select * from events")
        for i in events:
            if i[1]==evename:
                eveid=i[0]
        for x in data:
            if tname == x[1]:
                messagebox.showinfo("Failed", "Already Existed!!")
                ticket_name.set("")
                return
                
        id = len(data)+1
        DataOfDB = (id,tname,"AVAILBLE",tprice,tquan,eveid)
        OrderOfDB = "INSERT into tickets(tickets_id ,ticket_name ,status ,price ,quantity,event_id ) values(?,?,?,?,?,?)"
        database.WriteData(OrderOfDB, DataOfDB)
        success.set("Added Successfuly")
        messagebox.showinfo("Success", "Added Successfuly")
        success.set("")

def addTickets(showFrame, root):
    showFrame.tkraise()
    showFrame = tk.Frame(root, width=1000, height=550, bg='#318352')
    showFrame.place(x=300, y=200)

    tk.Label(showFrame, text="Enter Ticket Name", bg='#318352', fg='#D99A25',
             font=('calibri', 16, 'bold')).place(x=50, y=30)
    ticket_name = tk.StringVar(showFrame)
    tk.Entry(showFrame, textvariable=ticket_name, width=30, borderwidth=0, highlightthickness=0, bg='#262626', fg='#D99A25',
             font=('calibri', 16, 'bold')).place(x=300, y=30)

    tk.Label(showFrame, text="Enter Ticket Price", bg='#318352', fg='#D99A25',
             font=('calibri', 16, 'bold')).place(x=50, y=110)
    ticket_price = tk.StringVar(showFrame)
    tk.Entry(showFrame, textvariable=ticket_price, width=30, borderwidth=0, highlightthickness=0, bg='#262626', fg='#D99A25',
             font=('calibri', 16, 'bold')).place(x=300, y=110)

    tk.Label(showFrame, text="Enter Ticket Quantity", bg='#318352', fg='#D99A25',
             font=('calibri', 16, 'bold')).place(x=50, y=190)
    ticket_quantity = tk.StringVar(showFrame)
    tk.Entry(showFrame, textvariable=ticket_quantity, width=30, borderwidth=0, highlightthickness=0, bg='#262626', fg='#D99A25',
             font=('calibri', 16, 'bold')).place(x=300, y=190)

    tk.Label(showFrame, text="Enter Event Name", bg='#318352', fg='#D99A25',
             font=('calibri', 16, 'bold')).place(x=50, y=270)
    event_name = tk.StringVar(showFrame)
    tk.Entry(showFrame, textvariable=event_name, width=30, borderwidth=0, highlightthickness=0, bg='#262626', fg='#D99A25',
             font=('calibri', 16, 'bold')).place(x=300, y=270)

    success = tk.StringVar(showFrame)
    tk.Label(showFrame, textvariable=success, bg='#318352', fg='#D99A25',
             font=('calibri', 16, 'bold')).place(x=720, y=350)

    tk.Button(showFrame, text="Add Ticket", command=lambda: [addTick(ticket_name,ticket_price,ticket_quantity,event_name,success)], width=20,fg='#D99A25',bg='#318352',
              font=('calibri', 16, 'bold')).place(x=300, y=450)
    
def addFacu(faculty_name,success):
    global DataOfDB
    global OrderOfDB
    faculty = faculty_name.get().strip().capitalize()

    if faculty == "":
        success.set("Enter Valid Data!!!")
    else:
        data = database.ReadData("select * from faculties")
        for x in data:
            if faculty == x[1]:
                messagebox.showinfo("Failed", "Already Existed!!")
                faculty_name.set("")
                return
                
        id = len(data)+1
        DataOfDB = (id,faculty)
        OrderOfDB = "INSERT into faculties(faculty_id,faculty_name) values(?,?)"
        database.WriteData(OrderOfDB, DataOfDB)
        success.set("Added Successfuly")
        messagebox.showinfo("Success", "Added Successfuly")
        success.set("")
    
def addFaculty(showFrame, root):
    showFrame.tkraise()
    showFrame = tk.Frame(root, width=1000, height=550, bg='#318352')
    showFrame.place(x=300, y=200)

    tk.Label(showFrame, text="Enter Faculty Name", bg='#318352', fg='#D99A25',
             font=('calibri', 16, 'bold')).place(x=50, y=30)
    faculty_name = tk.StringVar(showFrame)
    tk.Entry(showFrame, textvariable=faculty_name, width=20, borderwidth=0, highlightthickness=0, bg='#262626', fg='#D99A25',
             font=('calibri', 16, 'bold')).place(x=300, y=30)

    success = tk.StringVar(showFrame)
    tk.Label(showFrame, textvariable=success, bg='#318352', fg='#D99A25',
             font=('calibri', 16, 'bold')).place(x=230, y=100)

    tk.Button(showFrame, text="Add Publisher", command=lambda: [addFacu(faculty_name,success)], width=20,fg='#D99A25',bg='#318352',
              font=('calibri', 16, 'bold')).place(x=200, y=150)

def addEve(event_name,author_name,event_date,success):
    global DataOfDB
    global OrderOfDB
    eve = event_name.get().strip().capitalize()
    auth = author_name.get().strip().capitalize()
    #ticketp = ticket_price.get()
    eve_date = event_date
    if eve == "":
        success.set("Enter Valid Data!!!")
    else:
        data = database.ReadData("select * from events")
        for x in data:
            if eve == x[1]:
                messagebox.showinfo("Failed", "Already Existed!!")
                event_name.set("")
                return
                
        id = len(data)+1
        auth_id =database.ReadData("select * from author")
        for i in auth_id:
            if auth == i[1]:
                a=i[0]
        #DataOfDB = (id,eve,a,ticketp,eve_date)
        DataOfDB = (id,eve,a,eve_date)
        #OrderOfDB = "INSERT into events(event_id,event_name,author_id,ticket_id,event_date) values(?,?,?,?,?)"
        OrderOfDB = "INSERT into events(event_id,event_name,author_id,event_date) values(?,?,?,?)"
        database.WriteData(OrderOfDB, DataOfDB)
        success.set("Added Successfuly")
        messagebox.showinfo("Success", "Added Successfuly")
        success.set("")

def addEvent(showFrame, root):
    showFrame.tkraise()
    showFrame = tk.Frame(root, width=1000, height=550, bg='#318352')
    showFrame.place(x=300, y=200)

    tk.Label(showFrame, text="Enter Event Name", bg='#318352', fg='#D99A25',
             font=('calibri', 16, 'bold')).place(x=50, y=30)
    event_name = tk.StringVar(showFrame)
    tk.Entry(showFrame, textvariable=event_name, width=30, borderwidth=0, highlightthickness=0, bg='#262626', fg='#D99A25',
             font=('calibri', 16, 'bold')).place(x=300, y=30)

    tk.Label(showFrame, text="Enter Author Name", bg='#318352', fg='#D99A25',
             font=('calibri', 16, 'bold')).place(x=50, y=110)
    author_name = tk.StringVar(showFrame)
    tk.Entry(showFrame, textvariable=author_name, width=30, borderwidth=0, highlightthickness=0, bg='#262626', fg='#D99A25',
             font=('calibri', 16, 'bold')).place(x=300, y=110)

    #tk.Label(showFrame, text="Enter Ticket Price", bg='#318352', fg='#D99A25',
             #font=('calibri', 16, 'bold')).place(x=50, y=190)
    #ticket_price = tk.StringVar(showFrame)
    #tk.Entry(showFrame, textvariable=ticket_price, width=30, borderwidth=0, highlightthickness=0, bg='#262626', fg='#D99A25',
             #font=('calibri', 16, 'bold')).place(x=300, y=190)

    tk.Label(showFrame, text="Enter Event Date", bg='#318352', fg='#D99A25',
             font=('calibri', 16, 'bold')).place(x=50, y=270)

    cal = Calendar(showFrame,
                   font="calibri 14", selectmode='day',
                    year=int(today.strftime("%Y")), month=int(today.strftime("%m")), day=int(today.strftime("%d")))
    cal.place(x=300, y=270)

    success = tk.StringVar(showFrame)
    tk.Label(showFrame, textvariable=success, bg='#318352', fg='#D99A25',
             font=('calibri', 16, 'bold')).place(x=720, y=350)

    #tk.Button(showFrame, text="Add Event", command=lambda: [addEve(event_name,author_name,ticket_price,cal.selection_get(),success)], width=20,fg='#D99A25',bg='#318352',
    tk.Button(showFrame, text="Add Event", command=lambda: [addEve(event_name,author_name,cal.selection_get(),success)], width=20,fg='#D99A25',bg='#318352',

              font=('calibri', 16, 'bold')).place(x=700, y=450)

def addLang(language_name,success):
    global DataOfDB
    global OrderOfDB
    Language = language_name.get().strip().capitalize()
    if Language == "":
        success.set("Enter Valid Data!!!")
    else:
        data = database.ReadData("select * from Languages")
        for x in data:
            if Language == x[1]:
                messagebox.showinfo("Failed", "Already Existed!!")
                language_name.set("")
                return
                
        id = len(data)+1
        DataOfDB = (id,Language)
        OrderOfDB = "INSERT into languages(languages_id,languages_name) values(?,?)"
        database.WriteData(OrderOfDB, DataOfDB)
        success.set("Added Successfuly")
        messagebox.showinfo("Success", "Added Successfuly")
        success.set("")

def addLanguage(showFrame, root):
    showFrame.tkraise()
    showFrame = tk.Frame(root, width=1000, height=550, bg='#318352')
    showFrame.place(x=300, y=200)

    tk.Label(showFrame, text="Enter Language Name", bg='#318352', fg='#D99A25',
             font=('calibri', 16, 'bold')).place(x=50, y=30)
    language_name = tk.StringVar(showFrame)
    tk.Entry(showFrame, textvariable=language_name, width=20, borderwidth=0, highlightthickness=0, bg='#262626', fg='#D99A25',
             font=('calibri', 16, 'bold')).place(x=300, y=30)

    success = tk.StringVar(showFrame)
    tk.Label(showFrame, textvariable=success, bg='#318352', fg='#D99A25',
             font=('calibri', 16, 'bold')).place(x=230, y=100)

    tk.Button(showFrame, text="Add Publisher", command=lambda: [addLang(language_name,success)], width=20,fg='#D99A25',bg='#318352',
              font=('calibri', 16, 'bold')).place(x=200, y=150)

def addPublish(publisher_name,publisher_loc, success):
    global DataOfDB
    global OrderOfDB
    publisher = publisher_name.get().strip().capitalize()
    location = publisher_loc.get().strip().capitalize()
    if publisher == "" or location =="":
        success.set("Enter Valid Data!!!")
    else:
        data = database.ReadData("select * from publisher")
        for x in data:
            if publisher == x[2]:
                messagebox.showinfo("Failed", "Already Existed!!")
                publisher_name.set("")
                return
                
        id = len(data)+1
        DataOfDB = (id,location,publisher)
        OrderOfDB = "INSERT into publisher(publisher_id,location,publisher_name) values(?,?,?)"
        database.WriteData(OrderOfDB, DataOfDB)
        success.set("Added Successfuly")
        messagebox.showinfo("Success", "Added Successfuly")
        success.set("")

def addPublisher(showFrame, root):
    showFrame.tkraise()
    showFrame = tk.Frame(root, width=1000, height=550, bg='#318352')
    showFrame.place(x=300, y=200)

    tk.Label(showFrame, text="Enter Publisher Name", bg='#318352', fg='#D99A25',
             font=('calibri', 16, 'bold')).place(x=50, y=30)
    publisher_name = tk.StringVar(showFrame)
    tk.Entry(showFrame, textvariable=publisher_name, width=20, borderwidth=0, highlightthickness=0, bg='#262626', fg='#D99A25',
             font=('calibri', 16, 'bold')).place(x=300, y=30)

    tk.Label(showFrame, text="Enter Publisher Location", bg='#318352', fg='#D99A25',
             font=('calibri', 16, 'bold')).place(x=50, y=110)
    publisher_loc = tk.StringVar(showFrame)
    tk.Entry(showFrame, textvariable=publisher_loc, width=20, borderwidth=0, highlightthickness=0, bg='#262626', fg='#D99A25',
             font=('calibri', 16, 'bold')).place(x=300, y=110)


    success = tk.StringVar(showFrame)
    tk.Label(showFrame, textvariable=success, bg='#318352', fg='#D99A25',
             font=('calibri', 16, 'bold')).place(x=230, y=150)

    tk.Button(showFrame, text="Add Publisher", command=lambda: [addPublish(publisher_name,publisher_loc, success)], width=20,fg='#D99A25',bg='#318352',
              font=('calibri', 16, 'bold')).place(x=200, y=200)

def addAuth(author_name, success):
    global DataOfDB
    global OrderOfDB
    author = author_name.get().strip().capitalize()
    if author == "":
        success.set("Enter Valid Data!!!")
    else:
        data = database.ReadData("select * from author")
        for x in data:
            if author == x[1]:
                messagebox.showinfo("Failed", "Already Existed!!")
                author_name.set("")
                return
                
        id = len(data)+1
        DataOfDB = (id,author)
        OrderOfDB = "INSERT into author(author_id,author_name) values(?,?)"
        database.WriteData(OrderOfDB, DataOfDB)
        success.set("Added Successfuly")
        messagebox.showinfo("Success", "Added Successfuly")
        success.set("")

def addAuthor(showFrame,root):
    showFrame.tkraise()
    showFrame = tk.Frame(root, width=1000, height=550, bg='#318352')
    showFrame.place(x=300, y=200)

    tk.Label(showFrame, text="Enter Author Name", bg='#318352', fg='#D99A25',
             font=('calibri', 16, 'bold')).place(x=50, y=30)
    author_name = tk.StringVar(showFrame)
    tk.Entry(showFrame, textvariable=author_name, width=20, borderwidth=0, highlightthickness=0, bg='#262626', fg='#D99A25',
             font=('calibri', 16, 'bold')).place(x=250, y=30)

    success = tk.StringVar(showFrame)
    tk.Label(showFrame, textvariable=success, bg='#318352', fg='#D99A25',
             font=('calibri', 16, 'bold')).place(x=230, y=100)

    tk.Button(showFrame, text="Add Author", command=lambda: [addAuth(author_name, success)], width=20,fg='#D99A25',bg='#318352',
              font=('calibri', 16, 'bold')).place(x=200, y=150)

def insertCate(category_name, success):
    global DataOfDB
    global OrderOfDB
    category = category_name.get().strip().capitalize()
    if category == "":
        success.set("Enter Valid Data!!!")
    else:
        data = database.ReadData("select * from categories")
        for x in data:
            if category == x[1]:
                messagebox.showinfo("Failed", "Already Existed!!")
                category_name.set("")
                return
                
        id = len(data)+1
        DataOfDB = (id,category)
        OrderOfDB = "INSERT into categories(categories_id,name) values(?,?)"
        database.WriteData(OrderOfDB, DataOfDB)
        success.set("Added Successfuly")
        messagebox.showinfo("Success", "Added Successfuly")
        success.set("")

def addCategory(showFrame,root):
    showFrame.tkraise()
    showFrame = tk.Frame(root, width=1000, height=550, bg='#318352')
    showFrame.place(x=300, y=200)

    tk.Label(showFrame, text="Enter Category Name", bg='#318352', fg='#D99A25',
             font=('calibri', 16, 'bold')).place(x=50, y=30)
    category_name = tk.StringVar(showFrame)
    tk.Entry(showFrame, textvariable=category_name, width=20, borderwidth=0, highlightthickness=0, bg='#262626', fg='#D99A25',
             font=('calibri', 16, 'bold')).place(x=300, y=30)

    success = tk.StringVar(showFrame)
    tk.Label(showFrame, textvariable=success, bg='#318352', fg='#D99A25',
             font=('calibri', 16, 'bold')).place(x=230, y=100)

    tk.Button(showFrame, text="Add Category", command=lambda: [insertCate(category_name, success)], width=20,fg='#D99A25',bg='#318352',
              font=('calibri', 16, 'bold')).place(x=200, y=150)

def users(showFrame,root,data):
    showFrame=tk.Tk()
    showFrame.title("Users")
    showFrame.state('zoomed')
    showFrame.configure(bg="#318352")
    showFrame.iconbitmap(r"icon.ico")
    data = database.ReadData("SELECT * FROM users")
    tables.Table4(showFrame,len(data),len(data[0]),data)

def WriteToDb(book_name, author_name,book_language,facu, category,Book_Price,Publisher,book_edition,Quantity, success):
    global DataOfDB
    global OrderOfDB
    book_name1 = book_name.get().strip().capitalize()
    author_name1 = author_name.get().strip().capitalize()
    book_language1 = book_language.get().strip().capitalize()
    category1 = category.get().strip().capitalize()
    Book_Price1 = Book_Price.get()
    Publisher1 = Publisher.get().strip().capitalize()
    book_edition1 = book_edition.get()
    quan = Quantity.get()
    faculty=facu.get().strip().capitalize()
    if book_name1 == "" or Book_Price1 <= 0 or quan <= 0:
        messagebox.showerror("Error","Enter valid data")
    else:
        data = database.ReadData("select * from books")
        id = len(data)+1
        for i in data:
            if i[0] == id:
                id += 1

        if database.ReadLine("select author_id from author where author_name =?",[author_name1]):
            authid = database.ReadLine("select author_id from author where author_name =?",[author_name1])
            authid =authid[0]
        else:
            authors=database.ReadData("select * from author")
            authid=len(authors)+1
            DataOfDB = (authid,author_name1)
            OrderOfDB = "INSERT into author(author_id,author_name) values(?,?)"
            database.WriteData(OrderOfDB, DataOfDB)
        if database.ReadLine("select languages_id from languages where languages_name=?",[book_language1]):
            langid = database.ReadLine("select languages_id from languages where languages_name=?",[book_language1])
            langid = langid[0]
        else:
            languages=database.ReadData("select * from languages")
            langid=len(languages)+1
            DataOfDB = (langid,book_language1)
            OrderOfDB = "INSERT into languages(languages_id,languages_name) values(?,?)"
            database.WriteData(OrderOfDB, DataOfDB)           
        if database.ReadLine("select categories_id from categories where name=?",[category1]):
            cateid = database.ReadLine("select categories_id from categories where name=?",[category1])
            cateid = cateid[0]
        else:
            categories=database.ReadData("select * from categories")
            cateid=len(categories)+1
            DataOfDB = (cateid,category1)
            OrderOfDB = "INSERT into categories(categories_id,name) values(?,?)"
            database.WriteData(OrderOfDB, DataOfDB)
        if database.ReadLine("select publisher_id from publisher where publisher_name =?",[Publisher1]):
            publisherid = database.ReadLine("select publisher_id from publisher where publisher_name =?",[Publisher1])
            publisherid = publisherid[0]
        else:
            publishers=database.ReadData("select * from publisher")
            publisherid=len(publishers)+1
            DataOfDB = (publisherid,Publisher1)
            OrderOfDB = "INSERT into publisher(publisher_id,publisher_name) values(?,?)"
            database.WriteData(OrderOfDB, DataOfDB)
        if database.ReadLine("select faculty_id from faculties where faculty_name=?",[faculty]):
            facultyid = database.ReadLine("select faculty_id from faculties where faculty_name=?",[faculty])
            facultyid = facultyid[0]
        else:
            faucltis=database.ReadData("select * from faculties")
            facultyid=len(faucltis)+1
            DataOfDB = (facultyid,faculty)
            OrderOfDB = "INSERT into faculties(faculty_id,faculty_name) values(?,?)"
            database.WriteData(OrderOfDB, DataOfDB)

        DataOfDB = (id, book_name1, authid, langid,cateid,facultyid,publisherid,Book_Price1,book_edition1,quan)
        OrderOfDB = "INSERT into books(book_id,book_title,author_id,language_id,category_id,faculty_id, publisher_id,book_price,book_edition,book_copies)values(?,?,?,?,?,?,?,?,?,?)"
        for i in data:
            if i[1] == book_name1 and i[6] == Book_Price1 and i[7] == book_edition1:
                q = quan + i[2]
                DataOfDB = (q, i[0])
                OrderOfDB = "update books set book_copies = ? where book_id = ?"

            elif i[1] == book_name1 and i[3] != Book_Price1 and i[7]==book_edition1:
                n = n + "_ " + str(i[0])
                DataOfDB = (id, n, authid, langid,cateid,facultyid,publisherid,Book_Price1,book_edition1,quan)



        database.WriteData(OrderOfDB, DataOfDB)
        book_name.set("")
        author_name.set("")
        book_language.set("")
        category.set("")
        Book_Price.set("")
        Publisher.set("")
        book_edition.set("")
        Quantity.set("")
        facu.set("")
        messagebox.showinfo("Success", "Added Successfuly")
        success.set("")

def addItem(showFrame, root):
    showFrame.tkraise()
    showFrame = tk.Frame(root, width=1000, height=550, bg='#318352')
    showFrame.place(x=300, y=200)

    tk.Label(showFrame, text="Enter Book Name", bg='#318352', fg='#D99A25',
             font=('calibri', 16, 'bold')).place(x=50, y=30)
    book_name = tk.StringVar(showFrame)
    tk.Entry(showFrame, textvariable=book_name, width=20, borderwidth=0, highlightthickness=0, bg='#262626', fg='#D99A25',
             font=('calibri', 16, 'bold')).place(x=250, y=30)

    tk.Label(showFrame, text="Enter Author Name", bg='#318352', fg='#D99A25',
             font=('calibri', 16, 'bold')).place(x=550, y=30)
    author_name = tk.StringVar(showFrame)
    tk.Entry(showFrame, textvariable=author_name, width=20, borderwidth=0, highlightthickness=0, bg='#262626', fg='#D99A25',
             font=('calibri', 16, 'bold')).place(x=750, y=30)

    tk.Label(showFrame, text="Book Language", bg='#318352', fg='#D99A25',
             font=('calibri', 16, 'bold')).place(x=50, y=110)
    book_language = tk.StringVar(showFrame)
    tk.Entry(showFrame, textvariable=book_language, width=20, borderwidth=0, highlightthickness=0, bg='#262626', fg='#D99A25',
             font=('calibri', 16, 'bold')).place(x=250, y=110)

    tk.Label(showFrame, text="Enter Category", bg='#318352', fg='#D99A25',
             font=('calibri', 16, 'bold')).place(x=550, y=110)
    category = tk.StringVar(showFrame)
    tk.Entry(showFrame, textvariable=category, width=20, borderwidth=0, highlightthickness=0, bg='#262626', fg='#D99A25',
             font=('calibri', 16, 'bold')).place(x=750, y=110)

    tk.Label(showFrame, text="Enter Book price", bg='#318352', fg='#D99A25',
             font=('calibri', 16, 'bold')).place(x=50, y=190)
    Book_Price = tk.IntVar(showFrame)
    tk.Entry(showFrame, textvariable=Book_Price, width=20, borderwidth=0, highlightthickness=0,  bg='#262626', fg='#D99A25',
             font=('calibri', 16, 'bold')).place(x=250, y=190)

    tk.Label(showFrame, text="Enter Publisher", bg='#318352', fg='#D99A25',
             font=('calibri', 16, 'bold')).place(x=550, y=190)
    Publisher = tk.StringVar(showFrame)
    tk.Entry(showFrame, textvariable=Publisher, width=20, borderwidth=0, highlightthickness=0, bg='#262626', fg='#D99A25',
             font=('calibri', 16, 'bold')).place(x=750, y=190)

    tk.Label(showFrame, text="Enter Book Edition", bg='#318352', fg='#D99A25',
             font=('calibri', 16, 'bold')).place(x=50, y=270)
    book_edition = tk.StringVar(showFrame)
    tk.Entry(showFrame, textvariable=book_edition, width=20, borderwidth=0, highlightthickness=0, bg='#262626', fg='#D99A25',
             font=('calibri', 16, 'bold')).place(x=250, y=270)

    tk.Label(showFrame, text="Enter Quantity", bg='#318352', fg='#D99A25',
             font=('calibri', 16, 'bold')).place(x=550, y=270)
    Quantity = tk.IntVar(showFrame)
    tk.Entry(showFrame, textvariable=Quantity, width=20, borderwidth=0, highlightthickness=0, bg='#262626', fg='#D99A25',
             font=('calibri', 16, 'bold')).place(x=750, y=270)

    tk.Label(showFrame, text="Enter Faculty", bg='#318352', fg='#D99A25',
             font=('calibri', 16, 'bold')).place(x=50, y=350)
    facu = tk.StringVar(showFrame)
    tk.Entry(showFrame, textvariable=facu, width=20, borderwidth=0, highlightthickness=0, bg='#262626', fg='#D99A25',
             font=('calibri', 16, 'bold')).place(x=250, y=350)

    success = tk.StringVar(showFrame)
    tk.Label(showFrame, textvariable=success, bg='#318352', fg='#D99A25',
             font=('calibri', 16, 'bold')).place(x=430, y=450)

    tk.Button(showFrame, text="Add Book", command=lambda: [WriteToDb(book_name, author_name,book_language,facu ,category,Book_Price,Publisher,book_edition,Quantity, success)], width=20,fg='#D99A25',bg='#318352',
              font=('calibri', 16, 'bold')).place(x=400, y=500)

def view_items(showFrame, root):
    """
    showFrame.tkraise()
    showFrame = tk.Frame(root, width=1000, height=550, bg='#318352')
    showFrame.place(x=300, y=200)
    showFrame.tkraise()
    """
    showFrame=tk.Tk()
    showFrame.title("Books")

    showFrame.state('zoomed')
    showFrame.configure(bg="#318352")
    showFrame.iconbitmap(r"icon.ico")
    total_rows = 0
    total_columns = 0
    data = database.ReadData("select * from books")
    authors = database.ReadData("select *from author")
    languages = database.ReadData("select * from languages")
    categories = database.ReadData("select * from categories")
    publishers = database.ReadData("select * from publisher")
    faculties = database.ReadData("select * from faculties")
          
        
    try:
        total_rows = len(data)
        total_columns = len(data[0])
        tables.Table(showFrame, total_rows, total_columns, data,authors,languages,categories,publishers,faculties)
    except IndexError:
        messagebox.showinfo("Error", "There's no data to show!")

def pay(data, realdata, showFrame,userid):
    uid = userid
    t=database.ReadData("select * from transactions")
    transid = len(t)
    cash = 0
    for i in data:
        transid=transid+1
        id = i[0]
        cash += i[4]
        x = (transid,uid,i[0], i[3], i[2], i[4], d1)
        for j in realdata:
            if i[0] == j[0]:
                realquan = j[9]-i[2]
                database.WriteData(
                "insert into transactions(transaction_id,user_id,book_id,price,quantity,cash,date)values(?,?,?,?,?,?,?)", x)
                database.WriteData(
                "update books set book_copies = ? where book_id = ?", (realquan, id))
       

    cartItems.clear()
    showFrame.destroy()
    messagebox.showinfo("Paid Successfully",
                        "Thanks for using our services !!")

def viewCart(showFrame, root,id):
    showFrame.tkraise()
    showFrame = tk.Frame(root, width=1000, height=550, bg='#318352')
    showFrame.place(x=300, y=200)
    showFrame1 = tk.Frame(root, width=1000, height=100, bg='#318352')
    showFrame1.place(x=300, y=500)
    realdata = database.ReadData("SELECT * from books")
    try:
        total_rows = len(cartItems)
        total_columns = len(cartItems[0])
        tables.Table2(showFrame, total_rows, total_columns, cartItems)
        tk.Button(showFrame1, text="Check out", command=lambda: pay(cartItems, realdata, showFrame,id), width=9, height=2, bg='#25403B', fg='#D99A25',
                  font=('calibri', 16, 'bold')).place(x=700, y=0)

    except IndexError:
        messagebox.showerror("Error", "Cart is Empty!")

def watch(ca):
    data = database.ReadData("SELECT * FROM transactions")
    books = database.ReadData("select * from books")
    users = database.ReadData("select *from users")

    t = []
    for i in data:
        if str(ca)[0:4] == str(i[6])[0:4] and str(ca)[5:7] == str(i[6])[5:7]  and str(ca)[8:10]== str(i[6])[8:10]:
            t += [(i)]
    root=tk.Tk()
    root.title(str(ca) + " Log")
    tables.Table3(root,len(t),6,t,books,users)

def trans(showFrame, root):
    showFrame.tkraise()
    showFrame = tk.Frame(root, width=1000, height=550, bg='#318352')
    showFrame.place(x=300, y=200)
    cal = Calendar(showFrame,
                   font="calibri 14", selectmode='day',
                    year=int(today.strftime("%Y")), month=int(today.strftime("%m")), day=int(today.strftime("%d")))
    cal.place(x=250, y=70)
    tk.Label(showFrame, text="Pick A Date", bg='#318352', fg='#D99A25',
             font=('calibri', 16, 'bold')).place(x=360, y=30)
    tk.Button(showFrame, text="Show", width=18, bg='#25403B', fg='#D99A25',
              font=('calibri', 16, 'bold'), command=lambda: [
                  watch(cal.selection_get())]).place(x=300, y=350)

def cart(id, name, quantity, price, cost):
    global cartItems
    Item = (id, name, quantity, price, cost)
    cartItems += [(Item)]

def check_quan(value, quantity, state, showFrame, q):
    id = 0
    realquan = 0
    name = value.get()
    quan = quantity.get()
    data = database.ReadLine("select * from books where book_title=?",[name])
    realquan = data[9]
    id = data[0]
    #for i in range(len(data)):
    #    if data[i][1] == name:
    #        realquan = data[i][9]
    #       id = i

    if realquan < quan:
        messagebox.showinfo("Failed", "No Enough Books")
    elif realquan >= quan:
        realquan -= quan
        totalprice = data[7] * quan
        state.set("Added to cart")
        messagebox.showinfo("Success", "Added To Cart")
        value.set("")
        quantity.set("")
        state.set("")
        q.set(realquan)
        x = id+1
        cart(id,name, quan, data[7], totalprice)
        return realquan

def sell_items(showFrame, root):
    showFrame.tkraise()
    showFrame = tk.Frame(root, width=1000, height=550, bg='#318352')
    showFrame.place(x=300, y=200)

    def CurSelet(evt):
        if L1.curselection() != ():
            x = L1.get(L1.curselection())
            var2.set(x)
            #data = database.ReadData("select * from books")
            data = database.ReadLine("select * from books where book_title=?",[x])
            #for i in data:
            #    if i[1] == x:
            #        item = i
            #        quant.set(item[9])
            item = data[0]
            quant.set(data[9])

    tk.Label(showFrame, text="Choose Book", bg='#318352', fg='#D99A25',
             font=('calibri', 20, 'bold')).place(x=100, y=30)
    L1 = tk.Listbox(showFrame, width=25, height=18, bg='#318352', borderwidth=0, highlightthickness=0, fg='#F2F2F2',
                    font=('calibri', 16, 'bold'))
    data = database.ReadData("select * from books")
    for i in range(len(data)):
        L1.insert(data[i][0], data[i][1])
        L1.place(x=30, y=i+80)
    L1.bind('<<ListboxSelect>>', CurSelet)
    var2 = tk.StringVar(showFrame)
    quant = tk.StringVar(showFrame)
    tk.Label(showFrame, text="Available : ", bg='#318352', fg='#D99A25',
             font=('calibri', 16, 'bold')).place(x=400, y=30)
    tk.Label(showFrame, textvariable=quant,  bg='#318352', fg='#D99A25',  #real quantity
             font=('calibri', 16, 'bold')).place(x=520, y=30)
    tk.Label(showFrame, text="Enter Quantity",  bg='#318352', fg='#D99A25',
             font=('calibri', 16, 'bold')).place(x=400, y=100)
    tk.Label(showFrame, text="Peice", bg='#318352', fg='#D99A25',
             font=('calibri', 16, 'bold')).place(x=650, y=30)
    quan = tk.IntVar(showFrame)  #desired quantity
    tk.Entry(showFrame, textvariable=quan, width=15, bg='#262626', fg='#D99A25',
             font=('calibri', 16, 'bold')).place(x=600, y=100)
    state = tk.StringVar(showFrame)
    tk.Label(showFrame, textvariable=state, bg='#318352', fg='#D99A25',
             font=('calibri', 16, 'bold')).place(x=500, y=300)
    tk.Button(showFrame, text="Add to Cart", width=18, bg='#25403B', fg='#D99A25',
              font=('calibri', 16, 'bold'), command=lambda: [
                  check_quan(var2, quan, state, showFrame, quant)]).place(x=500, y=200)

def delete(var):
    ids = 0
    messagebox.showinfo("Done", "Deleted Successfuly")
    name = var.get()
    data = database.ReadLine("select * from books where book_title=?",[name])
    if data[1] == name:
        ids = data[0]
    database.DeleteData("delete from books where book_id = ?", (ids,))

def delete_item(showFrame,root):
    showFrame.tkraise()
    showFrame = tk.Frame(root, width=1000, height=550, bg='#318352')
    showFrame.place(x=300, y=200)

    def CurSelet(evt):
        x = L1.get(L1.curselection())
        var2.set(x)

    var1 = tk.StringVar(showFrame)
    L1 = tk.Listbox(showFrame, width=25, height=18, bg='#318352', borderwidth=2, highlightthickness=1, fg='#F2F2F2',
                    font=('calibri', 16, 'bold'))
    data = database.ReadData("select * from books")
    for i in range(len(data)):
        L1.insert(data[i][0], data[i][1])
        L1.place(x=10, y=i+50)
    L1.bind('<<ListboxSelect>>', CurSelet)
    x = var1.get()
    var2 = tk.StringVar(showFrame)
    tk.Label(showFrame, text="Choose Book", bg='#318352', fg='#D99A25',
             font=('calibri', 20, 'bold')).place(x=75, y=0)
    tk.Button(showFrame, text="Delete Book", width=14,height=3, bg='#25403B', fg='#D99A25',
              font=('calibri', 16, 'bold'), command=lambda: [
                  delete(var2)]).place(x=500, y=50)

def start(id, username, priv):
    data = database.ReadData("SELECT * from branch_data")
    root = tk.Tk()
    root.title(data[0][0] + " Library")
    root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(),
                                       root.winfo_screenheight()))
    root.state('zoomed')
    root.configure(bg="#318352")
    root.iconbitmap(r"icon.ico")
    ud = tk.Frame(root,width=210,height=100,bg='#318352')
    ud.place(x=20 , y = 20)
    tk.Label(ud, text="Mr : " + username, bg='#318352', fg='#0F242E',
             font=('calibri', 16, 'bold')).place(x=0, y=10)
    tk.Label(ud, text="Branch : " + data[0][2], bg='#318352', fg='#0F242E',
             font=('calibri', 16, 'bold')).place(x=0, y=40)
    tk.Label(ud, text="Today is : " + day, bg='#318352', fg='#0F242E',
             font=('calibri', 16, 'bold')).place(x=0, y=70)

    tabsFrame = tk.Frame(root, width=210, height=550, bg='#318352')
    tabsFrame.place(x=20, y=200)
    showFrame = tk.Frame(root, width=1000, height=550, bg='#318352')
    showFrame.place(x=300, y=200)
    if priv == 2:
        tk.Button(tabsFrame, text="Buy\nBooks", command=lambda: sell_items(showFrame, root),  width=8, height=3, fg='#0F242E',bg='#3F5955',
                  font=('calibri', 16, 'bold')).grid(column=1, row=0)
        tk.Button(tabsFrame, text="View\nBooks", command=lambda: view_items(showFrame, root), width=8, height=3, fg='#0F242E',bg='#3F5955',
                  font=('calibri', 16, 'bold')).grid(column=0, row=0)
        tk.Button(tabsFrame, text="Cart", command=lambda: viewCart(showFrame, root,id), width=8, height=3,  fg='#0F242E',bg='#3F5955',
                  font=('calibri', 16, 'bold')).grid(column=1, row=1)
        tk.Button(tabsFrame, text="Buy\nTickets", command=lambda: sellTickets(showFrame, root,id), width=8, height=3, fg='#0F242E',bg='#3F5955',
                  font=('calibri', 16, 'bold')).grid(column=0, row=1)
        tk.Button(tabsFrame, text="View\nAuthors", command=lambda: viewAuth(showFrame, root), width=8, height=3, fg='#0F242E',bg='#3F5955',
                  font=('calibri', 16, 'bold')).grid(column=0, row=2)
        tk.Button(tabsFrame, text="View\nCategories", command=lambda: viewCate(showFrame, root), width=8, height=3, fg='#0F242E',bg='#3F5955',
                  font=('calibri', 16, 'bold')).grid(column=1, row=2)
        tk.Button(tabsFrame, text="View\nFaculties", command=lambda: viewFaCU(showFrame, root), width=8, height=3, fg='#0F242E',bg='#3F5955',
                  font=('calibri', 16, 'bold')).grid(column=0, row=3)
        tk.Button(tabsFrame, text="View\nLanguages", command=lambda: viewLang(showFrame, root), width=8, height=3, fg='#0F242E',bg='#3F5955',
                  font=('calibri', 16, 'bold')).grid(column=1, row=3)
    elif priv ==1:
        tk.Button(tabsFrame, text="Add\nBooks", command=lambda: addItem(showFrame, root), width=8, height=3, fg='#0F242E',bg='#3F5955',
                  font=('calibri', 16, 'bold')).grid(column=0, row=0)
        tk.Button(tabsFrame, text="Sell\nBooks", command=lambda: sell_items(showFrame, root),  width=8, height=3, fg='#0F242E',bg='#3F5955',
                  font=('calibri', 16, 'bold')).grid(column=1, row=0)
        tk.Button(tabsFrame, text="View\nBooks", command=lambda: view_items(showFrame, root), width=8, height=3, fg='#0F242E',bg='#3F5955',
                  font=('calibri', 16, 'bold')).grid(column=0, row=1)
        tk.Button(tabsFrame, text="View\nUsers",command=lambda: users(showFrame,root,data), width=8, height=3, fg='#0F242E',bg='#3F5955',
                  font=('calibri', 16, 'bold')).grid(column=1, row=1)
        tk.Button(tabsFrame, text="Cart", command=lambda: viewCart(showFrame, root,id), width=8, height=3,  fg='#0F242E',bg='#3F5955',
                  font=('calibri', 16, 'bold')).grid(column=0, row=2)          
        tk.Button(tabsFrame, text="Add\nCategory", command=lambda: addCategory(showFrame, root), width=8, height=3, fg='#0F242E',bg='#3F5955',
                  font=('calibri', 16, 'bold')).grid(column=1, row=2)
        tk.Button(tabsFrame, text="Add\nAuthor", command=lambda: addAuthor(showFrame, root), width=8, height=3, fg='#0F242E',bg='#3F5955',
                  font=('calibri', 16, 'bold')).grid(column=0, row=3)
        tk.Button(tabsFrame, text="Add\nPublisher", command=lambda: addPublisher(showFrame, root), width=8, height=3, fg='#0F242E',bg='#3F5955',
                  font=('calibri', 16, 'bold')).grid(column=1, row=3)
        tk.Button(tabsFrame, text="Add\nLanguages", command=lambda: addLanguage(showFrame, root), width=8, height=3, fg='#0F242E',bg='#3F5955',
                  font=('calibri', 16, 'bold')).grid(column=0, row=4)
        tk.Button(tabsFrame, text="Add\nEvents", command=lambda: addEvent(showFrame, root), width=8, height=3, fg='#0F242E',bg='#3F5955',
                  font=('calibri', 16, 'bold')).grid(column=1, row=4)
        tk.Button(tabsFrame, text="Add\nFaculty", command=lambda: addFaculty(showFrame, root), width=8, height=3, fg='#0F242E',bg='#3F5955',
                  font=('calibri', 16, 'bold')).grid(column=0, row=5)
        tk.Button(tabsFrame, text="Add\nTickets", command=lambda: addTickets(showFrame, root), width=8, height=3, fg='#0F242E',bg='#3F5955',
                  font=('calibri', 16, 'bold')).grid(column=1, row=5)
        tk.Button(tabsFrame, text="Sell\nTickets", command=lambda: sellTickets(showFrame, root,id), width=8, height=3, fg='#0F242E',bg='#3F5955',
                  font=('calibri', 16, 'bold')).grid(column=0, row=6)


    else:
        tk.Button(tabsFrame, text="Add\nBooks", command=lambda: addItem(showFrame, root), width=8, height=3, fg='#0F242E',bg='#3F5955',
                  font=('calibri', 16, 'bold')).grid(column=0, row=0)
        tk.Button(tabsFrame, text="Sell\nBooks", command=lambda: sell_items(showFrame, root),  width=8, height=3, fg='#0F242E',bg='#3F5955',
                  font=('calibri', 16, 'bold')).grid(column=1, row=0)
        tk.Button(tabsFrame, text="View\nBooks", command=lambda: view_items(showFrame, root), width=8, height=3, fg='#0F242E',bg='#3F5955',
                  font=('calibri', 16, 'bold')).grid(column=0, row=1)
        tk.Button(tabsFrame, text="Log", command=lambda: trans(showFrame, root), width=8, height=3,  fg='#0F242E',bg='#3F5955',
                  font=('calibri', 16, 'bold')).grid(column=1, row=1)
        tk.Button(tabsFrame, text="Delete\nBooks",command=lambda: delete_item(showFrame,root), width=8, height=3, fg='#0F242E',bg='#3F5955',
                  font=('calibri', 16, 'bold')).grid(column=0, row=2)
        tk.Button(tabsFrame, text="View\nUsers",command=lambda: users(showFrame,root,data), width=8, height=3, fg='#0F242E',bg='#3F5955',
                  font=('calibri', 16, 'bold')).grid(column=1, row=2)
        tk.Button(tabsFrame, text="Cart", command=lambda: viewCart(showFrame, root,id), width=8, height=3,  fg='#0F242E',bg='#3F5955',
                  font=('calibri', 16, 'bold')).grid(column=0, row=3)
        tk.Button(tabsFrame, text="Edit Users", command=lambda: editUsers(showFrame, root,id), width=8, height=3,  fg='#0F242E',bg='#3F5955',
                  font=('calibri', 16, 'bold')).grid(column=1, row=3)           
        tk.Button(tabsFrame, text="Add\nCategory", command=lambda: addCategory(showFrame, root), width=8, height=3, fg='#0F242E',bg='#3F5955',
                  font=('calibri', 16, 'bold')).grid(column=0, row=4)
        tk.Button(tabsFrame, text="Add\nAuthor", command=lambda: addAuthor(showFrame, root), width=8, height=3, fg='#0F242E',bg='#3F5955',
                  font=('calibri', 16, 'bold')).grid(column=1, row=4)
        tk.Button(tabsFrame, text="Add\nPublisher", command=lambda: addPublisher(showFrame, root), width=8, height=3, fg='#0F242E',bg='#3F5955',
                  font=('calibri', 16, 'bold')).grid(column=0, row=5)
        tk.Button(tabsFrame, text="Add\nLanguages", command=lambda: addLanguage(showFrame, root), width=8, height=3, fg='#0F242E',bg='#3F5955',
                  font=('calibri', 16, 'bold')).grid(column=1, row=5)
        tk.Button(tabsFrame, text="Add\nEvents", command=lambda: addEvent(showFrame, root), width=8, height=3, fg='#0F242E',bg='#3F5955',
                  font=('calibri', 16, 'bold')).grid(column=0, row=6)
        tk.Button(tabsFrame, text="Add\nFaculty", command=lambda: addFaculty(showFrame, root), width=8, height=3, fg='#0F242E',bg='#3F5955',
                  font=('calibri', 16, 'bold')).grid(column=1, row=6)
        tk.Button(tabsFrame, text="Add\nTickets", command=lambda: addTickets(showFrame, root), width=8, height=3, fg='#0F242E',bg='#3F5955',
                  font=('calibri', 16, 'bold')).grid(column=0, row=7)
        tk.Button(tabsFrame, text="Sell\nTickets", command=lambda: sellTickets(showFrame, root,id), width=8, height=3, fg='#0F242E',bg='#3F5955',
                  font=('calibri', 16, 'bold')).grid(column=1, row=7)

    root.mainloop()
