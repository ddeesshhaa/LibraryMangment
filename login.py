from operator import truediv
import tkinter as tk
from tkinter import messagebox
#from tkinter.ttk import Style
import database
import session
from tkcalendar import Calendar
import datetime



def login(name, password,root):
    x = name.get() 
    y = password.get()
    user = database.ReadLine("SELECT * from users where user_name = ?",[x])
    if user:
        if user[5] == y:
            root.destroy()
            session.start(user[0],user[1],user[6])
        else:
            password.set("")
            messagebox.showerror("Error","Wrong Password")
    else:
        messagebox.showerror("Error","User not found")
        name.set("")
        password.set("")




def register(fname,lname,dob,uname,password,phone,email,addr,rootreg,regchecker):
    fname = fname.get()
    lname = lname.get()
    dob   = dob.selection_get()
    phone = phone.get()
    email = email.get()
    addr  = addr.get()
    x = uname.get().strip().lower()
    y = password.get()
    if x =="" or y=="":
        messagebox.showerror("Error","Please Fill the Form!!")
    elif x == "admin" or x == "administrator":
        messagebox.showerror("Error","Unallowed Username")
        uname.set("")
        password.set("")
    else:
        data = database.ReadData("SELECT * from users")
        check = True
        priv = 2
        salary=0
        for row in data:
            if row[4] == x  :
                uname.set("")
                password.set("")
                messagebox.showerror("Error","Already Registered")
                check = False
        if check == True:
            User_id = len(data)+1
            order = "insert into users(User_id,First_name,Last_name,Date_Of_Birth,user_name,user_pass,priv,phone_number,email,address,salary )values(?,?,?,?,?,?,?,?,?,?,?)"
            d = (User_id,fname,lname,dob,x,y,priv,phone,email,addr,salary)
            database.WriteData(order,d)
            messagebox.showinfo("Successfully Registerd", "You can log in now!")
            rootreg.destroy()
            choose()
            
    

def reg(r):
    r.destroy()
    rootreg = tk.Tk()
    rootreg.title("Register")
    rootreg.state('zoomed')
    rootreg.configure(bg="#318352")
    rootreg.iconbitmap(r"icon.ico")
    rootRegFrame=tk.Frame(rootreg,width = 1024 , height = 768 ,bg='#318352')
    rootRegFrame.place(relx=0.5 , rely=0.5 , anchor = tk.CENTER)
    
    tk.Label(rootreg, text="Enter First Name", bg='#318352', fg='#F5E0EC',
             font=('calibri', 20, 'bold')).place(x=100, y=100)
    fname = tk.StringVar()
    tk.Entry(rootreg, textvariable=fname, width=20,borderwidth=0,highlightthickness=0,bg='#595959', fg='#F5E0EC',
             font=('calibri', 20, 'italic')).place(x=350, y=100)

    tk.Label(rootreg, text="Enter Last Name", bg='#318352', fg='#F5E0EC',
             font=('calibri', 20, 'bold')).place(x=800, y=100)
    lname = tk.StringVar()
    tk.Entry(rootreg, textvariable=lname, width=20,borderwidth=0,highlightthickness=0,bg='#595959', fg='#F5E0EC',
             font=('calibri', 20, 'italic')).place(x=1050, y=100)

    tk.Label(rootreg, text="Enter User Name", bg='#318352', fg='#F5E0EC',
             font=('calibri', 20, 'bold')).place(x=100, y=200)
    uname = tk.StringVar()
    tk.Entry(rootreg, textvariable=uname, width=20,borderwidth=0,highlightthickness=0,bg='#595959', fg='#F5E0EC',
             font=('calibri', 20, 'italic')).place(x=350, y=200)

    tk.Label(rootreg, text="Enter password", bg='#318352', fg='#F5E0EC',
             font=('calibri', 20, 'bold')).place(x=800, y=200)
    password = tk.StringVar()
    tk.Entry(rootreg, show="*",textvariable=password, width=20,borderwidth=0,highlightthickness=0,bg='#595959', fg='#F5E0EC',
             font=('calibri', 20, 'italic')).place(x=1050, y=200)

    tk.Label(rootreg, text="Enter Phone Number", bg='#318352', fg='#F5E0EC',
             font=('calibri', 20, 'bold')).place(x=800, y=300)
    phone = tk.StringVar()
    tk.Entry(rootreg, textvariable=phone, width=20,borderwidth=0,highlightthickness=0,bg='#595959', fg='#F5E0EC',
             font=('calibri', 20, 'italic')).place(x=1050, y=300)

    tk.Label(rootreg, text="Enter Email Address", bg='#318352', fg='#F5E0EC',
             font=('calibri', 20, 'bold')).place(x=100, y=300)
    email = tk.StringVar()
    tk.Entry(rootreg, textvariable=email, width=20,borderwidth=0,highlightthickness=0,bg='#595959', fg='#F5E0EC',
             font=('calibri', 20, 'italic')).place(x=350, y=300)

    tk.Label(rootreg, text="Enter Address", bg='#318352', fg='#F5E0EC',
             font=('calibri', 20, 'bold')).place(x=100, y=400)
    addr = tk.StringVar()
    tk.Entry(rootreg, textvariable=addr, width=20,borderwidth=0,highlightthickness=0,bg='#595959', fg='#F5E0EC',
             font=('calibri', 20, 'italic')).place(x=350, y=400)
    
    day = datetime.datetime.today().strftime("%A")
    today = datetime.date.today()
    d1 = today.strftime("%Y/%m/%d")
    cal = Calendar(rootreg,
                   font="calibri 12", selectmode='day',
                    year=int(today.strftime("%Y")), month=int(today.strftime("%m")), day=int(today.strftime("%d")))
    cal.place(x=350, y=400)

    tk.Label(rootreg, text="Choose Date of Birth", bg='#318352', fg='#F5E0EC',
            font=('calibri', 20, 'bold')).place(x=100, y=400)


    
    regchecker = tk.StringVar()
    tk.Label(rootreg,textvariable=regchecker,bg='#318352', fg='#F5E0EC',font=('calibri',20,'bold')).place(x=400,y=720)
             
    tk.Button(rootreg, text="Register",
              command=lambda: register(fname,lname,cal,uname,password,phone,email,addr,rootreg,regchecker), width=10, fg='#318352',
              font=('calibri', 20, 'bold')).place(x=400, y=700)


def choose():
    root = tk.Tk()
    root.title("Login")
    root.geometry("800x600")
    window_height = 600
    window_width = 800
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x_cordinate = int((screen_width/2) - (window_width/2))
    y_cordinate = int((screen_height/2) - (window_height/2))
    root.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
    root.resizable(False, False)
    root.configure(bg="#318352")
    root.iconbitmap(r"icon.ico")
    rootFrame=tk.Frame(root,width = 600 , height = 500 ,bg='#318352')
    rootFrame.place(relx=0.5 , rely=0.5 , anchor = tk.CENTER)
    
    tk.Label(rootFrame, text="Enter User Name", bg='#318352', fg='#F5E0EC',
             font=('calibri', 20, 'bold')).place(x=50, y=100)
    name = tk.StringVar()
    tk.Entry(rootFrame, textvariable=name, width=20,borderwidth=0,highlightthickness=0,bg='#595959', fg='#F5E0EC',
             font=('calibri', 20, 'italic')).place(x=300, y=100)

    tk.Label(rootFrame, text="Enter password", bg='#318352', fg='#F5E0EC',
             font=('calibri', 20, 'bold')).place(x=50, y=200)
    password = tk.StringVar()
    tk.Entry(rootFrame, show="*",textvariable=password, width=20,borderwidth=0,highlightthickness=0,bg='#595959', fg='#F5E0EC',
             font=('calibri', 20, 'italic')).place(x=300, y=200)
    
    #checker = tk.StringVar()
    #tk.Label(rootFrame,textvariable=checker,bg='#318352', fg='#F5E0EC',font=('calibri',20,'bold')).place(x=210,y=320)
             
    tk.Button(rootFrame, text="Register",
              command=lambda: reg(root), width=10, fg='#318352',
              font=('calibri', 20, 'bold')).place(x=100, y=300)
    tk.Button(rootFrame, text="Login",
              command=lambda: login(name,password,root), width=10, fg='#318352',
              font=('calibri', 20, 'bold')).place(x=350, y=300)


    root.mainloop()