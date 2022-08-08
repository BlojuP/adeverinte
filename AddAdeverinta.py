from tkinter import *
from tkcalendar import *
from datetime import *
from dateutil.relativedelta import *
from dateutil.parser import parse
from PIL import ImageTk,Image
from tkinter import messagebox
import sqlite3


#Function – AdeverintaRegister()
def adevRegister():
               
    #bid = adevInfo1.get()
    nume = adevInfo1.get()
    prenume = adevInfo2.get()
    email = adevInfo3.get()
    telefon = adevInfo4.get()
    emitere = dt
    expira = expira1

    textlist = [adevInfo1.get(), adevInfo2.get(), adevInfo3.get(), adevInfo4.get(), emitere, expira]
    cur.execute("""insert into adev (nume, prenume, email, telefon, data, expira) VALUES (?, ?, ?, ?, ?, ?); """, textlist)
    con.commit()
        
    #print(bid)
    print(nume)
    print(prenume)
    print(email)
    print(telefon)
    print(emitere)
    print(expira)
    root.destroy()


#Function – addAdeverinta()
def addAdev(): 

    global adevInfo1 ,adevInfo2, adevInfo3, adevInfo4, adevInfo5, adevInfo6, Canvas1, con, cur, adevTable, root, dt, expira1
            
    root = Tk()
    root.title("Adeverinte")
    root.minsize(width=400,height=400)
    root.geometry("1200x600")

    con = sqlite3.connect("data/adeverinte.db")
    cur = con.cursor()
        
    # Enter Table Names here
    #adevTable = "adev" # Book Table
    Canvas1 = Canvas(root)
            
    Canvas1.config(bg="#ff6e40")
    Canvas1.pack(expand=True,fill=BOTH)

#Frame2
    #labelFrame2 = Frame(root,bg='black')
    #labelFrame2.place(relx=0.6,rely=0.25,relwidth=0.27,relheight=0.6)
    #today = date.today()
    #cal = Calendar(labelFrame2, selectmode="day", year=today.year, month=today.month, day=today.day)
    #cal.place(relx=0.05,rely=0.04, relheight=0.6) 
        

    #def grab_date():
        #global expira1, dt
        #my_label.config(text=cal.get_date()) #selected date
        #dt = cal.get_date()
        #date1 = datetime.strptime(dt, "%m/%d/%y")
        #date_expira = date1 + relativedelta(months=+6)
        #expira1 = date_expira.strftime("%B/%y")
        #my_sixlabel.config(text=expira1)
        #my_label.config(text="Data emitere" + cal.get_date())

    #my_button = Button(labelFrame2, text="Get Date", command = grab_date)
    #my_button.place(relx=0.35,rely=0.67)

    #my_label = Label(labelFrame2, text="")
    #my_label.place(relx=0.3,rely=0.95, relwidth=0.62, relheight=0.08)
    #my_sixlabel = Label(labelFrame2, text= "")
    #my_sixlabel.place(relx=0.3,rely=0.105, relwidth=0.62, relheight=0.08)

#Frame1               
    headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
    headingLabel = Label(headingFrame1, text="Adauga Adeverinte", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.25,relwidth=0.8,relheight=0.5)
    today = date.today()
    cal = Calendar(labelFrame, selectmode="day", year=today.year, month=today.month, day=today.day)
    cal.place(relx=0.70,rely=0.04, relheight=0.6) 


    def grab_date():
        global expira1, dt
        my_label.config(text=cal.get_date()) #selected date
        dt = cal.get_date()
        date1 = datetime.strptime(dt, "%m/%d/%y")
        date_expira = date1 + relativedelta(months=+6)
        expira1 = date_expira.strftime("%B/%y")
        my_sixlabel.config(text=expira1)
        #my_label.config(text="Data emitere" + cal.get_date())

    my_button = Button(labelFrame, text="Get Date", command = grab_date)
    my_button.place(relx=0.80,rely=0.67)

                
    # Nume
    lb1 = Label(labelFrame,text="Nume : ", bg='black', fg='white')
    lb1.place(relx=0.05, rely=0.10, relheight=0.08)
                
    adevInfo1 = Entry(labelFrame)
    adevInfo1.place(relx=0.3 ,rely=0.10, relwidth=0.35, relheight=0.08)
                
    # Prenume
    lb2 = Label(labelFrame,text="Prenume : ", bg='black', fg='white')
    lb2.place(relx=0.05,rely=0.25, relheight=0.08)
                
    adevInfo2 = Entry(labelFrame)
    adevInfo2.place(relx=0.3,rely=0.25, relwidth=0.35, relheight=0.08)
                
    # Email
    lb3 = Label(labelFrame,text="Email : ", bg='black', fg='white')
    lb3.place(relx=0.05,rely=0.40, relheight=0.08)
                
    adevInfo3 = Entry(labelFrame)
    adevInfo3.place(relx=0.3,rely=0.40, relwidth=0.35, relheight=0.08)
                
    # Telefon
    lb4 = Label(labelFrame,text="Telefon : ", bg='black', fg='white')
    lb4.place(relx=0.05,rely=0.55, relheight=0.08)
                
    adevInfo4 = Entry(labelFrame)
    adevInfo4.place(relx=0.3,rely=0.55, relwidth=0.35, relheight=0.08)

    # Emitere
    #lb5 = Label(labelFrame,text="Data Emitere : ", bg='black', fg='white')
    #lb5.place(relx=0.05,rely=0.70, relheight=0.08)
                
    #adevInfo5 = dt
    #adevInfo5.place(relx=0.3,rely=0.70, relwidth=0.35, relheight=0.08)

    # Expira
    #lb6 = Label(labelFrame,text="Data Expira : ", bg='black', fg='white')
    #lb6.place(relx=0.05,rely=0.85)
                
    #adevInfo6 = expira1
    #adevInfo6.place(relx=0.3,rely=0.85, relwidth=0.35, relheight=0.08)

    # Emitere
    lb5 = Label(labelFrame,text="Data Emitere : ", bg='black', fg='white')
    lb5.place(relx=0.05,rely=0.70, relheight=0.08)
    my_label = Label(labelFrame, text="", bg='black', fg='white')
    my_label.place(relx=0.3,rely=0.70, relwidth=0.35, relheight=0.08)

    # Expira
    lb6 = Label(labelFrame,text="Data Expira : ", bg='black', fg='white')
    lb6.place(relx=0.05,rely=0.85)
    my_sixlabel = Label(labelFrame, text="", bg='black', fg='white')
    my_sixlabel.place(relx=0.3,rely=0.85, relwidth=0.35, relheight=0.08)

    


    #Submit Button
    SubmitBtn = Button(root,text="Adauga",bg='#d1ccc0', fg='black',command=adevRegister)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)

    #CalBtn = Button (root, text= "Alege Data Emitere", bg='#d1ccc0', fg='black', command=root.destroy)
    #CalBtn.place(relx=0.39,rely=0.9, relwidth=0.18,relheight=0.08)
            
    quitBtn = Button(root,text="Iesire",bg='#f7f1e3', fg='black',       command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)

    root.mainloop()
