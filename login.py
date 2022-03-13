from tkinter import *
import tkinter.messagebox as MessageBox
import os


root=Tk()
root.title('Login Page')
root.geometry("600x300")
root.configure(bg="#090844")

def __MenuPage__():
    uname1=t_uname.get()
    password1=t_pwd.get()

    if uname1=="Admin" and password1=="12345":
        MessageBox.showinfo(uname1,"Logged successfully")

        filename = 'Menu.py'
        os.system(filename)
        os.system('notepad' + filename)


    elif uname1=="" and password1=="":
        MessageBox.showinfo(uname1,"Please provide correct username and Password ")

    else :
        MessageBox.showinfo(uname1,"Wrong Credintial")




title=Label(root, text="Login form ",fg="yellow",bg="#090844",font=("bold",15))
title.place( x=240,  y="10")

uname=Label(root, text="User name : ",fg="white",bg="#090844",font=("bold",15))
uname.place( x=70,  y="70")

Password=Label(root, text="Password  : ",fg="white",bg="#090844",font=("bold",15))
Password.place( x=70,  y="120")

t_uname=Entry(bd=10)
t_uname.place(x=300,y="70")

t_pwd=Entry(bd=10)
t_pwd.place(x=300,y=120)

submit=Button( root, text="Submit",fg="#000000",bg="white",font=("bold",17),command = __MenuPage__)
submit.place(x=200,y=200)

root.mainloop()

