#from logging import root
import tkinter as tk
from tkinter import messagebox
import database
import login

def Ownername(name, phone,address,root):
    x = name.get()  # get() to get variable value [mustafa]
    n = x.strip().capitalize()
    y = phone.get().strip()
    z = address.get().strip()
    data = (n, y, z)  # (id,owner_name,store_name) from database
    if n == "" or y== "" or z== "":
        messagebox.showerror("Error","All Feilds Are Requiered")
    else:
        order = "insert into branch_data(branch_name,phone,address) values(?,?,?)"
        database.WriteData(order,data)
        messagebox.showinfo("Success", "Admin username is admin\nAdmin password is admin")
        root.destroy()
        login.choose()

def start():
    root = tk.Tk()
    root.title("Library Data")
    root.geometry("800x600")
    window_height = 600
    window_width = 800
    root.iconbitmap(r"icon.ico")
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x_cordinate = int((screen_width/2) - (window_width/2))
    y_cordinate = int((screen_height/2) - (window_height/2))

    root.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
    root.resizable(False, False)
    root.configure(bg="#318352")
    rootFrame=tk.Frame(root,width = 600 , height = 500 ,bg='#318352')
    rootFrame.place(relx=0.5 , rely=0.5 , anchor = tk.CENTER)
    tk.Label(rootFrame, text="Please Enter Library Data",bg='#318352', fg='#F5E0EC',
             font=('calibri', 20, 'bold')).place(x=180, y=20)
    tk.Label(rootFrame, text="Enter Library Name",bg='#318352', fg='#F5E0EC',
             font=('calibri', 20, 'bold')).place(x=50, y=100)
    name = tk.StringVar()
    tk.Entry(rootFrame, textvariable=name, width=20,borderwidth=0,highlightthickness=0,bg='#595959', fg='#F5E0EC',
             font=('calibri', 20, 'italic')).place(x=300, y=100)

    tk.Label(rootFrame, text="Enter Phone",bg='#318352', fg='#F5E0EC',
             font=('calibri', 20, 'bold')).place(x=50, y=150)
    phone = tk.StringVar()
    tk.Entry(rootFrame, textvariable=phone, width=20,borderwidth=0,highlightthickness=0,bg='#595959', fg='#F5E0EC',
             font=('calibri', 20, 'italic')).place(x=300, y=150)
             
    tk.Label(rootFrame, text="Enter Address",bg='#318352', fg='#F5E0EC',
             font=('calibri', 20, 'bold')).place(x=50, y=200)
    address = tk.StringVar()
    tk.Entry(rootFrame, textvariable=address, width=20,borderwidth=0,highlightthickness=0,bg='#595959', fg='#F5E0EC',
             font=('calibri', 20, 'italic')).place(x=300, y=200)

    tk.Button(rootFrame, text="Submit",
              command=lambda: Ownername(name, phone,address,root), fg='#318352',
              font=('calibri', 20, 'bold')).place(x=250, y=270)
    root.mainloop()