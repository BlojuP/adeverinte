from tkinter import *
from tkcalendar import *
from datetime import *
from dateutil.relativedelta import *
from dateutil.parser import parse
import tkinter.messagebox
import sqlite3

expira = date.today()

#define Adauga window
def adauga_win():
    window=Tk()
    window.title("Adauga client nou")
    window.geometry("600x500")

    def combineFunc(self, *funcs):
       def combinedFunc(*args, **kwargs):
            for f in funcs:
                f(*args, **kwargs)
       return combinedFunc
    
    class MyWindow:
        def __init__(self, window):
            self.lbl1=Label(window, text='Nume')
            self.lbl2=Label(window, text='Prenume')
            self.lbl3=Label(window, text='Email')
            self.lbl4=Label(window, text='Telefon')
            self.lbl5=Label(window, text='Data')
            self.lbl6=Label(window, text='Expira')
            self.t1=Entry(window, bd=3)
            self.t2=Entry(window, bd=3)
            self.t3=Entry(window, bd=3)
            self.t4=Entry(window, bd=3)
            self.t5= my_label
            self.t6= my_sixlabel
            self.btn1 = Button(window, text='Adauga')
            self.btn2 = Button(window, text='Iesire')
            self.lbl1.place(x=50, y=70)
            self.t1.place(x=120, y=70)
            self.lbl2.place(x=50, y=120)
            self.t2.place(x=120, y=120)
            self.lbl3.place(x=50, y=170)
            self.t3.place(x=120, y=170)
            self.lbl4.place(x=50, y=220)
            self.t4.place(x=120, y=220)
            self.lbl5.place(x=50, y=270)
            self.t5.place(x=120, y=270)
            self.lbl6.place(x=50, y=320)
            self.t6.place(x=120, y=320)
            self.b1=Button(window, text='Adauga', command=self.add)
            self.b2=Button(window, text='Iesire', command=window.destroy)
            self.b1.place(x=50, y=350)
            self.b2.place(x=126, y=350)

   
        def add(self):
            #sql = "INSERT INTO adeverinte(nume, prenume, email, telefon, data) VALUES (?, ?, ?, ?, ?);"
            textlist = [self.t1.get() , self.t2.get(), self.t3.get(), self.t4.get(), cal.get_date(), expira]
            cur.execute("""INSERT INTO adeverinte (nume, prenume, email, telefon, data, expira) VALUES (?, ?, ?, ?, ?, ?); """, textlist)
            con.commit()
            
            joined_string = " | ".join(textlist)
            outF = open("adeverinte.txt", "a")
            outF.write("\n")
            for line in joined_string:
                #write line to output file
                outF.write(line)
                
            outF.close()
            
            window.destroy()



#Today's Date Calendar
    today = date.today()
    cal = Calendar(window, selectmode="day", year=today.year, month=today.month, day=today.day)
    cal.pack(anchor=NE, padx=50, pady=50)
        
    def grab_date():
        global expira
        my_label.config(text=cal.get_date()) #selected date
        #calculate selected date + 6 months
        dt = cal.get_date()
        date1 = datetime.strptime(dt, "%m/%d/%y")
        date_expira = date1 + relativedelta(months=+6)
        expira = date_expira.strftime("%B/%y")
        my_sixlabel.config(text=expira)
        
    
    

    my_button = Button(window, text="Selecteaza Data Expirare", command = grab_date)
    my_button.pack(anchor=E, padx=100)

    
    my_label = Label(window, text="")
    my_sixlabel = Label(window, text= "")
                
    mywin=MyWindow(window)





# connecting to the database
con = sqlite3.connect("adeverinte.db")
# preparing a cursor object
cur = con.cursor()

cur.execute("""create table if not exists adeverinte(ROWID INTEGER PRIMARY KEY, nume VARCHAR(200) not null, prenume VARCHAR(200) not null, email VARCHAR(200), telefon INT, data DATE, expira DATE);""")


#Expired entries
def file_expirate():
    root=Tk()
    root.geometry("600x500+10+10")

#Connect to DB
    try:
        sqliteConnection = sqlite3.connect('adeverinte.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

#print all content
        #sqlite_select_query = """Select * from adeverinte"""
        #cursor.execute(sqlite_select_query)
        #records = cursor.fetchall()
        #numbers = len(records)
        #print("Total rows are: ", len(records))
        #print("Printing each row")
        #for row in records:
           #print(row[1], row[2], row[3], row[4], row[5], row[6])
           #print("\n")

#print content from specific date
        ed = date.today()
        data_expirare = ed.strftime('%B')
        print("Luna curenta este", data_expirare)
        cursor.execute("""Select * FROM adeverinte WHERE strftime('%m',expira)=?; """, data_expirare)
        records = cursor.fetchall()
        numbers = len(records)
        print("Total rows are: ", len(records))
        print("Printing each row")
        for row in records:
           print(row[1], row[2], row[3], row[4], row[5], row[6])
           print("\n")

        cursor.close()


    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)
    
    finally:
            if sqliteConnection:
                sqliteConnection.close()
                print("The SQLite connection is closed")
    
def about_command():
    pass

#Hide all frames
#def hide_all_frames():
    #file_new_frame.pack_forget()
    #file_expirate_frame.pack_forget()

    
root=Tk()
root.title('Adeverinte')
root.geometry("600x500+10+10")


my_menu = Menu(root)
root.config(menu=my_menu)

#Create a menu item

file_menu = Menu(my_menu)
my_menu.add_cascade(label="Adeverinte", menu=file_menu)
file_menu.add_command(label="Adauga...", command=adauga_win)
file_menu.add_command(label="Expirate...", command=file_expirate)
file_menu.add_separator()
file_menu.add_command(label="Iesire", command=root.destroy)

about_menu = Menu(my_menu)
my_menu.add_cascade(label="Despre", menu=about_menu)
about_menu.add_command(label="Autor", command=about_command)

#create frames
#file_new_frame = Frame(window, width=600, height=500)
#calendar_frame = Frame(file_new_frame, width = 300, height=300)
#file_expirate_frame = Frame(root, width=600, height=500)

root.mainloop()
    
