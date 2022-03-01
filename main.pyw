from tkinter import *
from PIL import ImageTk,Image #PIL -> Pillow
import sqlite3
from tkinter import messagebox
from AddAdeverinta import *
from ViewAdeverinta import *
import sys
import os

#Create Data Folder
if not os.path.exists('data'):
    os.makedirs('data')

#Create export Folder
if not os.path.exists('export'):
    os.makedirs('export')

#Connecting to Sqlite3 db
connection = sqlite3.connect("data/adeverinte.db")

cur = connection.cursor()
print("Connected to the database")

#create table in DB is not existing
cur.execute("create table if not exists adev(ROWID INTEGER PRIMARY KEY, nume VARCHAR(200) not null, prenume VARCHAR(200) not null, email VARCHAR(200), telefon INT, data DATE, expira DATE);")
connection.close()

#Designing the Window
root = Tk()
root.title("Adeverinte")
root.minsize(width=400,height=400)
root.geometry("600x500")

#Adding a Background Image
same=True
n=0.6

background_image =Image.open("pic/Adeverinta.jpg")
[imageSizeWidth, imageSizeHeight] = background_image.size

newImageSizeWidth = int(imageSizeWidth*n)
if same:
    newImageSizeHeight = int(imageSizeHeight*n) 
else:
    newImageSizeHeight = int(imageSizeHeight/n) 
    
background_image = background_image.resize((newImageSizeWidth,newImageSizeHeight),Image.ANTIALIAS)
img = ImageTk.PhotoImage(background_image)
Canvas1 = Canvas(root)
Canvas1.create_image(300,250,image = img)      
Canvas1.config(bg="white",width = newImageSizeWidth, height = newImageSizeHeight)
Canvas1.pack(expand=True,fill=BOTH)


#Setting up the Head Frame
headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)
headingLabel = Label(headingFrame1, text="Program \n Evidenta Adeverinte", bg='black', fg='white', font=('Courier',15))
headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)


#Adding the Buttons
btn1 = Button(root,text="Adaugare Adeverinta",bg='black', fg='white', command=addAdev)
btn1.place(relx=0.28,rely=0.4, relwidth=0.45,relheight=0.1)

btn2 = Button(root,text="Vizualizare adeveriunta",bg='black', fg='white', command=viewAdev)
btn2.place(relx=0.28,rely=0.6, relwidth=0.45,relheight=0.1)
root.mainloop()
