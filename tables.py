import tkinter as tk
class Table:
    def __init__(self, root, total_rows, total_columns, lst,authors,languages,categories,publishers,faculties):
        ids = ("ID", "Book Name", "Author Name", "Language", "Faculty", "Category", "Publisher", "Price", "Edition", "Copies")
        for j in range(total_columns):
            if j == 0:
                self.e = tk.Entry(root, width=5,bg='#3F5955', fg='#0F242E',borderwidth=1,
                                  font=('calibri', 16, 'bold'))
                self.e.grid(row=0, column=j)
                self.e.insert(tk.END, ids[j])
            elif j == 1:
                self.e = tk.Entry(root, width=30,bg='#3F5955', fg='#0F242E',borderwidth=1,
                                  font=('calibri', 16, 'bold'))
                self.e.grid(row=0, column=j)
                self.e.insert(tk.END, ids[j])
            elif j==2:
                self.e = tk.Entry(root, width=15,bg='#3F5955', fg='#0F242E',borderwidth=1,
                                  font=('calibri', 16, 'bold'))
                self.e.grid(row=0, column=j)
                self.e.insert(tk.END, ids[j])
            else:
                self.e = tk.Entry(root, width=10,bg='#3F5955', fg='#0F242E',borderwidth=1,
                
                                  font=('calibri', 16, 'bold'))
                self.e.grid(row=0, column=j)
                self.e.insert(tk.END, ids[j])

        for i in range(total_rows):
            for j in range(total_columns):
                if j == 0:
                    self.e = tk.Entry(root, width=5,bg='#3F5955', fg='#8C8C8C',borderwidth=1,
                                      font=('calibri', 16, ''))
                    self.e.grid(row=i+1, column=j)
                    self.e.insert(tk.END, lst[i][j])
                elif j == 1:
                    self.e = tk.Entry(root, width=30,bg='#3F5955', fg='#8C8C8C',borderwidth=1,
                    
                                      font=('calibri', 16, ''))
                    self.e.grid(row=i+1, column=j)
                    self.e.insert(tk.END, lst[i][j])
                elif j == 2:
                    x="NULL"
                    for k in authors:
                        if k[0] ==lst[i][2]:
                            x=k[1]
                            
                    self.e = tk.Entry(root, width=15, bg='#3F5955', fg='#8C8C8C',borderwidth=1,font=('calibri', 16, ''))
                    self.e.grid(row=i+1, column=2)
                    self.e.insert(tk.END,x)

                elif j == 3:
                    x="NULL"
                    for k in languages:
                        if k[0] ==lst[i][3]:
                            x=k[1]


                    self.e = tk.Entry(root, width=10, bg='#3F5955', fg='#8C8C8C',borderwidth=1,font=('calibri', 16, ''))
                    self.e.grid(row=i+1, column=3)
                    self.e.insert(tk.END, x)
                
                elif j == 4:
                    x="NULL"
                    for k in faculties:
                        if k[0] ==lst[i][4]:
                            x=k[1]

                    self.e = tk.Entry(root, width=10, bg='#3F5955', fg='#8C8C8C',borderwidth=1,font=('calibri', 16, ''))
                    self.e.grid(row=i+1, column=4)
                    self.e.insert(tk.END,x)

                elif j == 5:
                    x="NULL"
                    for k in categories:
                        if k[0] ==lst[i][5]:
                            x=k[1]

                    self.e = tk.Entry(root, width=10, bg='#3F5955', fg='#8C8C8C',borderwidth=1,font=('calibri', 16, ''))
                    self.e.grid(row=i+1, column=5)
                    self.e.insert(tk.END, x)

                elif j == 6:
                    x="NULL"
                    for k in publishers:
                        if k[0] ==lst[i][6]:
                            x=k[2]

                    self.e = tk.Entry(root, width=10, bg='#3F5955', fg='#8C8C8C',borderwidth=1,font=('calibri', 16, ''))
                    self.e.grid(row=i+1, column=6)
                    self.e.insert(tk.END,x)

                else:
                    self.e = tk.Entry(root, width=10, bg='#3F5955', fg='#8C8C8C',borderwidth=1,
                    
                                      font=('calibri', 16, ''))
                    self.e.grid(row=i+1, column=j)
                    self.e.insert(tk.END, lst[i][j])


class Table2:
    def __init__(self, root, total_rows, total_columns, lst):
        ids = ("ID", "Item Name", "Quantity", "Price", "Total Price")
        cash = 0
        for j in range(total_columns):
            if j == 0:
                self.e = tk.Entry(root, width=5,bg='#3F5955', fg='#0F242E',highlightthickness=0,
                                  font=('calibri', 16, 'bold'))
                self.e.grid(row=0, column=j)
                self.e.insert(tk.END, ids[j])
            elif j == 1:
                self.e = tk.Entry(root, width=20,bg='#3F5955', fg='#0F242E',highlightthickness=0,
                                  font=('calibri', 16, 'bold'))
                self.e.grid(row=0, column=j)
                self.e.insert(tk.END, ids[j])
            else:
                self.e = tk.Entry(root, width=15,bg='#3F5955', fg='#0F242E',highlightthickness=0,
                                  font=('calibri', 16, 'bold'))
                self.e.grid(row=0, column=j)
                self.e.insert(tk.END, ids[j])

        

        for i in range(total_rows):
            cash += lst[i][4]
            for j in range(total_columns):
                if j == 0:
                    self.e = tk.Entry(root, width=5, bg='#3F5955', fg='#8C8C8C',borderwidth=1,highlightthickness=0,
                                      font=('calibri', 16, ''))
                    self.e.grid(row=i+1, column=j)
                    self.e.insert(tk.END, lst[i][j])
                elif j == 1:
                    self.e = tk.Entry(root, width=20, bg='#3F5955', fg='#8C8C8C',borderwidth=1,highlightthickness=0,
                                      font=('calibri', 16, ''))
                    self.e.grid(row=i+1, column=j)
                    self.e.insert(tk.END, lst[i][j])
                else:
                    self.e = tk.Entry(root, width=15, bg='#3F5955', fg='#8C8C8C',borderwidth=1,highlightthickness=0,
                                      font=('calibri', 16, ''))
                    self.e.grid(row=i+1, column=j)
                    self.e.insert(tk.END, lst[i][j])

            self.e = tk.Entry(root, width=15,bg='#3F5955', fg='#0F242E',highlightthickness=0,
                                  font=('calibri', 16, 'bold'))
            self.e.grid(row=total_rows+2, column=2)
            self.e.insert(tk.END, "Total Cash :")
            self.e = tk.Entry(root, width=15,bg='#3F5955', fg='#0F242E',highlightthickness=0,
                                  font=('calibri', 16, 'bold'))
            self.e.grid(row=total_rows+2, column=total_columns-1)
            self.e.insert(tk.END, str(cash)+" L.E")


class Table3:
    def __init__(self, root, total_rows, total_columns, lst,books,users):
        ids = ("ID", "Username", "Bookname", "Price", "Copies","Total Cash")
        for j in range(total_columns):
            if j == 0:
                self.e = tk.Entry(root, width=5,bg='#3F5955', fg='#0F242E',highlightthickness=0,
                                  font=('calibri', 16, 'bold'))
                self.e.grid(row=0, column=j)
                self.e.insert(tk.END, ids[j])
            elif j == 1:

                self.e = tk.Entry(root, width=20,bg='#3F5955', fg='#0F242E',highlightthickness=0,
                                  font=('calibri', 16, 'bold'))
                self.e.grid(row=0, column=j)
                self.e.insert(tk.END, ids[j])
            elif j == 2:

                self.e = tk.Entry(root, width=20,bg='#3F5955', fg='#0F242E',highlightthickness=0,
                                  font=('calibri', 16, 'bold'))
                self.e.grid(row=0, column=j)
                self.e.insert(tk.END, ids[j])
            else:
                self.e = tk.Entry(root, width=15,bg='#3F5955', fg='#0F242E',highlightthickness=0,
                                  font=('calibri', 16, 'bold'))
                self.e.grid(row=0, column=j)
                self.e.insert(tk.END, ids[j])

        

        for i in range(total_rows):
            for j in range(total_columns):
                if j == 0:
                    self.e = tk.Entry(root, width=5, bg='#3F5955', fg='#8C8C8C',borderwidth=1,highlightthickness=0,
                                      font=('calibri', 16, ''))
                    self.e.grid(row=i+1, column=j)
                    self.e.insert(tk.END, lst[i][j])
                elif j==1:
                    for k in users:
                        if k[0] ==lst[i][1]:
                            x=k[4]
                    self.e = tk.Entry(root, width=20, bg='#3F5955', fg='#8C8C8C',borderwidth=1,highlightthickness=0,
                                      font=('calibri', 16, ''))
                    self.e.grid(row=i+1, column=j)
                    self.e.insert(tk.END, x)
                elif j==2:
                    for k in books:
                        if k[0] ==lst[i][2]:
                            x=k[1]
                    self.e = tk.Entry(root, width=20, bg='#3F5955', fg='#8C8C8C',borderwidth=1,highlightthickness=0,
                                      font=('calibri', 16, ''))
                    self.e.grid(row=i+1, column=j)
                    self.e.insert(tk.END, x)
                else:
                    self.e = tk.Entry(root, width=15, bg='#3F5955', fg='#8C8C8C',borderwidth=1,highlightthickness=0,
                                      font=('calibri', 16, ''))
                    self.e.grid(row=i+1, column=j)
                    self.e.insert(tk.END, lst[i][j])


class Table4:
    def __init__(self, root, total_rows, total_columns, lst):
        ids = ("ID","FIRST NAME","LAST NAME","DATE OF BIRTH","Userame", "Password", "Privilege","PHONE NUMBER","EMAIL","ADDRESS","SALARY")
        for j in range(total_columns):
            if j == 0:
                self.e = tk.Entry(root, width=5,bg='#3F5955', fg='#0F242E',highlightthickness=0,
                                  font=('calibri', 16, 'bold'))
                self.e.grid(row=0, column=j)
                self.e.insert(tk.END, ids[j])
            elif j == 1:
                self.e = tk.Entry(root, width=10,bg='#3F5955', fg='#0F242E',highlightthickness=0,
                                  font=('calibri', 16, 'bold'))
                self.e.grid(row=0, column=j)
                self.e.insert(tk.END, ids[j])

            elif j == 7 or j== 8:
                self.e = tk.Entry(root, width=20,bg='#3F5955', fg='#0F242E',highlightthickness=0,
                                  font=('calibri', 16, 'bold'))
                self.e.grid(row=0, column=j)
                self.e.insert(tk.END, ids[j])
            else:
                self.e = tk.Entry(root, width=10, bg='#3F5955', fg='#0F242E',highlightthickness=0,
                                  font=('calibri', 16, 'bold'))
                self.e.grid(row=0, column=j)
                self.e.insert(tk.END, ids[j])

        

        for i in range(total_rows):
            for j in range(total_columns):
                if j == 0:
                    self.e = tk.Entry(root, width=5, bg='#3F5955', fg='#8C8C8C',borderwidth=1,highlightthickness=0,
                                      font=('calibri', 16, ''))
                    self.e.grid(row=i+1, column=j)
                    self.e.insert(tk.END, lst[i][j])
                elif j == 1:
                    self.e = tk.Entry(root, width=10, bg='#3F5955', fg='#8C8C8C',borderwidth=1,highlightthickness=0,
                                      font=('calibri', 16, ''))
                    self.e.grid(row=i+1, column=j)
                    self.e.insert(tk.END, lst[i][j])
                elif j ==6 :
                    if lst[i][6] == 0:
                        self.e = tk.Entry(root, width=10,bg='#3F5955', fg='#8C8C8C',borderwidth=1,highlightthickness=0,
                                      font=('calibri', 16, ''))
                        self.e.grid(row=i+1, column=j)
                        self.e.insert(tk.END, "Admin")
                    elif lst[i][6] == 1:
                        self.e = tk.Entry(root, width=10, bg='#3F5955', fg='#8C8C8C',borderwidth=1,highlightthickness=0,
                                        font=('calibri', 16, 'italic'))
                        self.e.grid(row=i+1, column=j)
                        self.e.insert(tk.END, "Librarian")
                    else:
                        self.e = tk.Entry(root, width=10, bg='#3F5955', fg='#8C8C8C',borderwidth=1,highlightthickness=0,
                                        font=('calibri', 16, 'italic'))
                        self.e.grid(row=i+1, column=j)
                        self.e.insert(tk.END, "Customer")
                elif j == 7 or j ==8:
                    self.e = tk.Entry(root, width=20, bg='#3F5955', fg='#8C8C8C',borderwidth=1,highlightthickness=0,
                                      font=('calibri', 16, ''))
                    self.e.grid(row=i+1, column=j)
                    self.e.insert(tk.END, lst[i][j])
                
                else:
                    self.e = tk.Entry(root, width=10, bg='#3F5955', fg='#8C8C8C',borderwidth=1,highlightthickness=0,
                                      font=('calibri', 16, ''))
                    self.e.grid(row=i+1, column=j)
                    self.e.insert(tk.END, lst[i][j])

