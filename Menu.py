from tkinter import *
import os
from tkinter import ttk



def menu():
       root = Tk()
       root.title('Menu')
       root.geometry('1200x650')
       root.config(bg = '#090844')
       
       title_Frame = LabelFrame(root, font = ('arial',50,'bold'), width = 1000, height = 100, bg = '#11536c', relief = 'raise', bd = 13)
       title_Frame.grid(row = 0, column = 0, pady = 50)
       
       title_Label = Label(title_Frame, text = 'MENU', font = ('arial',20,'bold'),fg ='black', bg = '#11536c')
       title_Label.grid(row = 0, column = 0, padx = 150)

       def manage_employee():
              filename = 'manage_employee.py'
              os.system(filename)
              os.system('notepad'+ filename)

       def manage_payroll():
              filename = 'manage_payroll.py'
              os.system(filename)
              os.system('notepad'+ filename)


       #========================================================FRAMES===================================================================
       Frame_1 = LabelFrame(root, font = ('arial',17,'bold'), width = 1000, height = 100, bg = '#090844', relief = 'ridge', bd = 10)
       Frame_1.grid(row = 1, column = 0, padx = 280)

       Frame_2 = LabelFrame(root, font = ('arial',17,'bold'), width = 1000, height = 100, bg = '#090844', relief = 'ridge', bd = 10)
       Frame_2.grid(row = 2, column = 0, padx = 130, pady = 7)

       Frame_3 = LabelFrame(root, font = ('arial',17,'bold'), width = 1000, height = 100, bg = '#090844', relief = 'ridge', bd = 10)
       Frame_3.grid(row = 3, column = 0, pady = 7)



       #========================================================LABELS===================================================================
       Tname = Label(root, text="EMPLOYEE DATABASE AND PAYROLL MANAGEMENT SYSTEM ", fg="#e4d209", bg="#090844", font=('arial',18,'bold'))
       Tname.place(x=250, y="10")

       Label_1 = Label(Frame_1, text = 'Manage Employee', font = ('Arial ',20,'bold'), fg="white",bg = '#090844')
       Label_1.grid(row = 0, column = 0, padx = 50, pady = 5)

       Label_2 = Label(Frame_2, text = 'Manage Payroll', font = ('Arial',20,'bold'), fg="white", bg = '#090844')
       Label_2.grid(row = 0, column = 0, padx = 67, pady = 5)

       Label_3 = Label(Frame_3, text = 'Logout', font = ('Arial',20,'bold'), fg="white", bg = '#090844')
       Label_3.grid(row = 0, column = 0, padx = 60, pady = 5)



       #========================================================BUTTONS===================================================================
       Button_1 = Button(Frame_1, text = 'View', font = ('arial',16,'bold'), width = 8, command = manage_employee)
       Button_1.grid(row = 0, column = 3, padx = 50)

       Button_2 = Button(Frame_2, text = 'View', font = ('arial',16,'bold'), width = 8, command = manage_payroll)
       Button_2.grid(row = 0, column = 3, padx = 50)

       Button_3 = Button(Frame_3, text = 'Confirm', font = ('arial',16,'bold'), width = 8, command = root.destroy)
       Button_3.grid(row = 0, column = 3, padx = 50)



       root.mainloop()


       

if __name__ == '__main__':
       menu()
