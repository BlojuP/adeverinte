from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import sqlite3
from datetime import *
from dateutil.relativedelta import *
from dateutil.parser import parse
from xlsxwriter.workbook import Workbook


def viewAdev(): 
    
    root = Tk()
    root.title("Adeverinte")
    root.minsize(width=400,height=400)
    root.geometry("900x500")



#print content from specific date
    ed = date.today()
    data_expirare = ed.strftime('%B/%y')
    #print("Luna curenta este", data_expirare)
    data_expira = [data_expirare]
    #numbers = len(records)    

#Display Data
    Canvas1 = Canvas(root) 
    Canvas1.config(bg="#12a4d9")
    Canvas1.pack(expand=True,fill=BOTH)
    headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
    headingLabel = Label(headingFrame1, text="Adeverinte Expirate", bg='black', fg='white', font = ('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)
    y = 0.25
    Label(labelFrame, text="%-10s%-20s%-17s%-30s%-20s%-10s%-20s"%('ID','Nume','Prenume', 'Email', 'Telefon','Emitere','Expirare'),
    bg='black',fg='white').place(relx=0.07,rely=0.1)
    Label(labelFrame, text = "------------------------------------------------------------------------------------------------------------------",bg='black',fg='white').place (relx=0.05,rely=0.2)



#Connecting to Sqlite3 db
    connection = sqlite3.connect("data/adeverinte.db")
    cur = connection.cursor()

    getAdev = """Select ROWID, nume, prenume, email, telefon, data, expira from adev where expira = ? ; """
    try:
        cur.execute(getAdev, data_expira)
        rows = cur.fetchall()
        for row in rows:
            Label(labelFrame,text="%-10s%-20s%-20s%-30s%-20s%-10s%-20s"%(row[0],row[1],row[2],row[3],row[4],row[5],row[6]) ,bg='black', fg='white').place(relx=0.07,rely=y)
            y += 0.1
    except:
        messagebox.showinfo("Failed to fetch files from database")

#export to Excel
    def exportAdev():
        workbook = Workbook('export/output2.xlsx')
        worksheet = workbook.add_worksheet()
        mysel = cur.execute(getAdev, data_expira)
        for i, row in enumerate(mysel):
            for j, value in enumerate(row):
                worksheet.write(i, j, value)
        workbook.close()
    
    quitBtn = Button(root,text="Export",bg='#f7f1e3', fg='black', command=exportAdev)
    quitBtn.place(relx=0.2,rely=0.9, relwidth=0.18,relheight=0.08)

    quitBtn = Button(root,text="Iesire",bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.6,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()
