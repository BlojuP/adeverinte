from tkinter import *
from tkcalendar import *
import tkinter.messagebox
import sqlite3

def get_posts():
    try:
        sqliteConnection = sqlite3.connect('adeverinte.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        sqlite_select_query = """Select * from adeverinte"""
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()
        numbers = len(records)
        print("Total rows are: ", len(records))
        print("Printing each row")
        for row in records:
            print(row[1], row[2], row[3], row[4], row[5])
            print("\n")

        cursor.close()

    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")

    get_posts()

class MyWindow:
    def __init__(self, win):
        self.lbl1=Label(win, text='Nume')
        self.lbl2=Label(win, text='Prenume')
        self.lbl3=Label(win, text='Email')
        self.lbl4=Label(win, text='Telefon')
        self.t1=Entry(bd=3)
        self.t2=Entry(bd=3)
        self.t3=Entry(bd=3)
        self.t4=Entry(bd=3)
        self.btn1 = Button(win, text='Adauga')
        self.btn2 = Button(win, text='Editeaza')
        self.btn3 = Button(win, text='Sterge')
        self.btn4 = Button(win, text='Cauta')
        self.btn5 = Button(win, text='Iesire')
        self.lbl1.place(x=50, y=70)
        self.t1.place(x=120, y=70)
        self.lbl2.place(x=50, y=120)
        self.t2.place(x=120, y=120)
        self.lbl3.place(x=50, y=170)
        self.t3.place(x=120, y=170)
        self.lbl4.place(x=50, y=220)
        self.t4.place(x=120, y=220)
        self.b1=Button(win, text='Adauga', command=self.add)
        self.b2=Button(win, text='Editeaza')
        self.b3=Button(win, text='Sterge')
        self.b4=Button(win, text='Expirate', command=get_posts)
        self.b5=Button(win, text='Cauta')
        self.b6=Button(root, text='Iesire', command=root.destroy)
        self.b1.place(x=50, y=350)
        self.b2.place(x=126, y=350)
        self.b3.place(x=204, y=350)
        self.b4.place(x=280, y=350)
        self.b5.place(x=358, y=350)
        self.b6.place(x=433, y=350)


    def add(self):
        #sql = "INSERT INTO adeverinte(nume, prenume, email, telefon, data) VALUES (?, ?, ?, ?, ?);"
        textlist = [self.t1.get() , self.t2.get(), self.t3.get(), self.t4.get(), cal.get_date()]
        cur.execute("""INSERT INTO adeverinte (nume, prenume, email, telefon, data) VALUES (?, ?, ?, ?, ?); """, textlist)
        con.commit()
        
        joined_string = " | ".join(textlist)
        outF = open("adeverinte.txt", "a")
        outF.write("\n")
        for line in joined_string:
            #write line to output file
            outF.write(line)
        outF.close()

    def sub(self, event):
        self.t3.delete(0, 'end')
        num1=int(self.t1.get())
        num2=int(self.t2.get())
        result=num1-num2
        self.t3.insert(END, str(result))



  
root=Tk()
mywin=MyWindow(root)
root.title('Adeverinte')
root.geometry("600x500+10+10")

# connecting to the database
con = sqlite3.connect("adeverinte.db")
# preparing a cursor object
cur = con.cursor()

cur.execute("""create table if not exists adeverinte(ROWID INTEGER PRIMARY KEY, nume VARCHAR(200) not null, prenume VARCHAR(200) not null, email VARCHAR(200), telefon INT, data DATE);""")



cal = Calendar(root, selectmode="day", year=2021, month=9, day=7)
cal.pack(anchor=NE, padx=50, pady=50)

def grab_date():
    my_label.config(text=cal.get_date())

my_button = Button(root, text="Selecteaza Data Expirare", command=grab_date)
my_button.pack(anchor=E, padx=100)


my_label = Label(root, text="")
my_label.pack(anchor=NW, padx=220, pady=270)



root.mainloop()
