from tkinter import *
import os

def __login__():
       filename = 'login.py'
       os.system(filename)
       os.system('notepad'+filename)

window=Tk()
window.title('Home')

canvas=Canvas(window, width=1024,height=666)
canvas.pack()

my_image=PhotoImage(file='C:\\Users\\udari\\PycharmProjects\\semifinal\\management-consulting.png')
canvas.create_image(0, 0, anchor = NW, image=my_image)

title=Label(window, text="EMPLOYEE DATABASE AND PAYROLL MANAGEMENT SYSTEM ",fg="white",bg="#011f43",font=("bold",17))
title.place( x=210,  y="10")

submit=Button( window, text="Login",fg="white",bg="black",font=("bold",21), width = 8,command = __login__)
submit.place(x=450,y=300)




window.mainloop()
