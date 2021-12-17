from tkinter import *
from tkcalendar import *
import tkinter.messagebox
import sqlite3


#define Adauga window
def adauga_win():
    window=Tk()
    window.title("Adauga client nou")
    window.geometry("600x500")

    class MyWindow:
        def __init__(self, window):
            self.lbl1=Label(window, text='Nume')
            self.lbl2=Label(window, text='Prenume')
            self.lbl3=Label(window, text='Email')
            self.lbl4=Label(window, text='Telefon')
            self.lbl5=Label(window, text='Data')
            self.t1=Entry(window, bd=3)
            self.t2=Entry(window, bd=3)
            self.t3=Entry(window, bd=3)
            self.t4=Entry(window, bd=3)
            self.t5= my_label
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
            self.b1=Button(window, text='Adauga', command=self.add)
            self.b2=Button(window, text='Iesire', command=window.destroy)
            self.b1.place(x=50, y=350)
            self.b2.place(x=126, y=350)

   
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

    cal = Calendar(window, selectmode="day", year=2021, month=9, day=7)
    cal.pack(anchor=NE, padx=50, pady=50)

    def grab_date():
        my_label.config(text=cal.get_date())
        

    my_button = Button(window, text="Selecteaza Data Expirare", command=grab_date)
    my_button.pack(anchor=E, padx=100)


    my_label = Label(window, text="")

            
    mywin=MyWindow(window)


root=Tk()
root.title('Adeverinte')
root.geometry("600x500+10+10")


my_menu = Menu(root)
root.config(menu=my_menu)


# connecting to the database
con = sqlite3.connect("adeverinte.db")
# preparing a cursor object
cur = con.cursor()

cur.execute("""create table if not exists adeverinte(ROWID INTEGER PRIMARY KEY, nume VARCHAR(200) not null, prenume VARCHAR(200) not null, email VARCHAR(200), telefon INT, data DATE);""")


#Expired entries
def file_expirate():
    window1=Tk()
    window1.title("Adeverinte Expirate")
    window1.geometry("600x500")

    class MyWindow1:
        def __init__(self, window):
            self.btn1 = Button(window, text='Iesire')
            self.b1=Button(window, text='Iesire', command=window.destroy)
        
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
        
    my_label = Label(window1, text="")
    
    mywin1=MyWindow1(window1)

def about_command():
    pass

#Hide all frames
def hide_all_frames():
    #file_new_frame.pack_forget()
    file_expirate_frame.pack_forget()

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
file_expirate_frame = Frame(root, width=600, height=500)

root.mainloop()
    
