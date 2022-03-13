from tkinter import *

import tkinter.messagebox

import manage_employee_back




class emp_info():
    def __init__(self, master):
        self.master = master
        self.master.title('Manage Employee')
        self.master.geometry('1600x3000')
        self.master.config(bg='#090844')

        def information():
            # ========================================================Variables=====================================================================
            self.EmpNo = StringVar()
            self.FirstName = StringVar()
            self.LastName = StringVar()
            self.Age = StringVar()
            self.Gender = StringVar()
            self.status = StringVar()
            self.Address = StringVar()
            self.ContactNo = StringVar()
            self.Email = StringVar()
            self.Position = StringVar()
            self.DateHired = StringVar()
            self.BasicSalary = StringVar()
            self.OTHours = StringVar()
            self.OTRate = StringVar()
            self.Travelling_Allowances = StringVar()
            self.CashAdvance = StringVar()
            self.Loan = StringVar()


            # ==========================================================Functions====================================================================
            def EmpRec(event):
                try:
                    global selected_tuple

                    index = self.listbox.curselection()[0]
                    selected_tuple = self.listbox.get(index)

                    self.Entry_EmpNo.delete(0, END)
                    self.Entry_EmpNo.insert(END, selected_tuple[0])

                    self.Entry_FirstName.delete(0, END)
                    self.Entry_FirstName.insert(END, selected_tuple[1])

                    self.Entry_LastName.delete(0, END)
                    self.Entry_LastName.insert(END, selected_tuple[2])

                    self.Entry_Age.delete(0, END)
                    self.Entry_Age.insert(END, selected_tuple[3])

                    self.Entry_Gender.delete(0, END)
                    self.Entry_Gender.insert(END, selected_tuple[4])

                    self.Entry_Status.delete(0, END)
                    self.Entry_Status.insert(END, selected_tuple[5])

                    self.Entry_Address.delete(0, END)
                    self.Entry_Address.insert(END, selected_tuple[6])

                    self.Entry_ContactNo.delete(0, END)
                    self.Entry_ContactNo.insert(END, selected_tuple[7])

                    self.Entry_Email.delete(0, END)
                    self.Entry_Email.insert(END, selected_tuple[8])

                    self.Entry_Position.delete(0, END)
                    self.Entry_Position.insert(END, selected_tuple[9])

                    self.Entry_DateHired.delete(0, END)
                    self.Entry_DateHired.insert(END, selected_tuple[10])

                    self.Entry_BasicSalary.delete(0, END)
                    self.Entry_BasicSalary.insert(END, selected_tuple[11])

                    self.Entry_OTHours.delete(0, END)
                    self.Entry_OTHours.insert(END, selected_tuple[12])

                    self.Entry_OTRate.delete(0, END)
                    self.Entry_OTRate.insert(END, selected_tuple[13])

                    self.Entry_Travelling_Allowances.delete(0, END)
                    self.Entry_Travelling_Allowances.insert(END, selected_tuple[14])

                    self.Entry_CashAdvance.delete(0, END)
                    self.Entry_CashAdvance.insert(END, selected_tuple[15])

                    self.Entry_Loan.delete(0, END)
                    self.Entry_Loan.insert(END, selected_tuple[16])

                except IndexError:
                    pass

            def Add():
                if (len(self.EmpNo.get()) != 0):
                    manage_employee_back.insert(self.EmpNo.get(), self.FirstName.get(), self.LastName.get(), self.Age.get(),
                                            self.Gender.get(), self.status.get(), self.Address.get(),self.ContactNo.get(),
                                                self.Email.get(),self.Position.get(),self.DateHired.get(),self.BasicSalary.get(),
                                                self.OTHours.get(),self.OTRate.get(),self.Travelling_Allowances.get(),self.CashAdvance.get(),
                                                self.Loan.get(), \
                                            )

                    self.listbox.delete(0, END)
                    self.listbox.insert(END, (
                    self.EmpNo.get(), self.FirstName.get(), self.LastName.get(), self.Age.get(), self.Gender.get(),
                    self.status.get(), self.Address.get(),self.ContactNo.get(),self.Email.get(),self.Position.get(),
                    self.DateHired.get(),self.BasicSalary.get() ,self.OTHours.get(),self.OTRate.get(),
                    self.Travelling_Allowances.get(),self.CashAdvance.get(),self.Loan.get(),\
                    ))

            def Display():
                self.listbox.delete(0, END)
                for row in manage_employee_back.view():
                    self.listbox.insert(END, row, str(' '))

            def Exit():
                Exit = tkinter.messagebox.askyesno("Login System", "Confirm if you want to Exit")
                if Exit > 0:
                    self.master.destroy()
                    return

            def Reset():
                self.EmpNo.set('')
                self.FirstName.set('')
                self.LastName.set('')
                self.Age.set('')
                self.Gender.set('')
                self.status.set('')
                self.Address.set('')
                self.ContactNo.set('')
                self.Email.set('')
                self.Position.set('')
                self.DateHired.set('')
                self.BasicSalary.set('')
                self.OTHours.set('')
                self.OTRate.set('')
                self.Travelling_Allowances.set('')
                self.CashAdvance.set('')
                self.Loan.set('')
                self.listbox.delete(0, END)

            def Delete():
                if (len(self.EmpNo.get()) != 0):
                    manage_employee_back.delete(selected_tuple[0])
                    Reset()
                    Display()

            def Search():
                self.listbox.delete(0, END)
                for row in manage_employee_back.search(self.EmpNo.get(), self.FirstName.get(),
                                                       self.LastName.get(),self.Age.get(), self.Gender.get(),
                                                       self.status.get(),self.Address.get(),self.ContactNo.get(),
                                                       self.Email.get(),self.Position.get(),self.DateHired.get(),
                                                       self.BasicSalary.get(),self.OTHours.get(),self.OTRate.get(),
                                                       self.Travelling_Allowances.get(),self.CashAdvance.get(),
                                                       self.Loan.get()):
                    self.listbox.insert(END, row, str(' '))

            def Update():
                if (len(self.EmpNo.get()) != 0):
                    manage_employee_back.delete(selected_tuple[0])

                if (len(self.EmpNo.get()) != 0):
                    manage_employee_back.insert(self.EmpNo.get(), self.FirstName.get(), self.LastName.get(), self.Age.get(),
                                            self.Gender.get(), self.status.get(), self.Address.get(),self.ContactNo.get(),
                                                self.Email.get(),self.Position.get(),self.DateHired.get(),self.BasicSalary.get(),
                                                self.OTHours.get(),self.OTRate.get(),self.Travelling_Allowances.get(),
                                                self.CashAdvance.get(),self.Loan.get(), \
                                            )

                    self.listbox.delete(0, END)
                    self.listbox.insert(END, (
                    self.EmpNo.get(), self.FirstName.get(), self.LastName.get(), self.Age.get(), self.Gender.get(),

                    self.status.get(), self.Address.get(),self.ContactNo.get(),self.Email.get(), self.Position.get(),
                    self.DateHired.get(),self.BasicSalary.get(),self.OTHours.get(),self.OTRate.get(),
                    self.Travelling_Allowances.get(),self.CashAdvance.get(),self.Loan.get(),\
                    ))

            # ============================================================Frames=====================================================================

            self.Main_Frame = LabelFrame(self.master, width=1300, height=500, font=('arial', 20, 'bold'), \
                                         bg='#090844', bd=15, relief='ridge')
            self.Main_Frame.grid(row=0, column=0, padx=10, pady=20)

            self.Frame_1 = LabelFrame(self.Main_Frame, width=600, height=400, font=('arial', 15, 'bold'), \
                                      relief='ridge', bd=10, bg='#090844',fg='#22f91c', text='EMPLOYEE INFORMATION ')
            self.Frame_1.grid(row=1, column=0, padx=10)

            self.Frame_2 = LabelFrame(self.Main_Frame, width=750, height=400, font=('arial', 15, 'bold'), \
                                      relief='ridge', bd=10, bg='#090844',fg='#22f91c', text='EMPLOYEE DATABASE')
            self.Frame_2.grid(row=1, column=1, padx=5)

            self.Frame_3 = LabelFrame(self.master, width=1200, height=100, font=('arial', 10, 'bold'), \
                                      bg='#090844', relief='ridge', bd=13)
            self.Frame_3.grid(row=2, column=0, pady=10)

            # ========================================================Labels of Frame_1========================================================
            self.Label_EmpNo = Label(self.Frame_1, text='Emp No', font=('arial', 12, 'bold'), bg='#090844',fg='white')
            self.Label_EmpNo.grid(row=0, column=0, sticky=W, padx=20, pady=10)

            self.Label_FirstName = Label(self.Frame_1, text='First Name', font=('arial', 12, 'bold'), bg='#090844',fg='white')
            self.Label_FirstName.grid(row=1, column=0, sticky=W, padx=20)

            self.Label_LastName = Label(self.Frame_1, text='Last Name', font=('arial', 12, 'bold'), bg='#090844',fg='white')
            self.Label_LastName.grid(row=2, column=0, sticky=W, padx=20)

            self.Label_Age = Label(self.Frame_1, text='Age', font=('arial', 12, 'bold'), bg='#090844',fg='white')
            self.Label_Age.grid(row=3, column=0, sticky=W, padx=20, pady=10)

            self.Label_Gender = Label(self.Frame_1, text='Gender', font=('arial', 12, 'bold'), bg='#090844',fg='white')
            self.Label_Gender.grid(row=4, column=0, sticky=W, padx=20)

            self.Label_Status = Label(self.Frame_1, text='Ststus', font=('arial', 12, 'bold'), bg='#090844',fg='white')
            self.Label_Status.grid(row=5, column=0, sticky=W, padx=20)

            self.Label_Address = Label(self.Frame_1, text='Address', font=('arial', 12, 'bold'), bg='#090844',fg='white')
            self.Label_Address.grid(row=6, column=0, sticky=W, padx=20)

            self.Label_ContactNo = Label(self.Frame_1, text='Contact No', font=('arial', 12, 'bold'), bg='#090844',fg='white')
            self.Label_ContactNo.grid(row=7, column=0, sticky=W, padx=20)

            self.Label_Email = Label(self.Frame_1, text='Email', font=('arial', 12, 'bold'), bg='#090844',fg='white')
            self.Label_Email.grid(row=8, column=0, sticky=W, padx=20)

            self.Label_Position = Label(self.Frame_1, text='Position', font=('arial', 12, 'bold'), bg='#090844',fg='white')
            self.Label_Position.grid(row=9, column=0, sticky=W, padx=20)

            self.Label_DateHired = Label(self.Frame_1, text='Date Hired', font=('arial', 12, 'bold'), bg='#090844',fg='white')
            self.Label_DateHired.grid(row=10, column=0, sticky=W, padx=20)

            self.Label_BasicSalary= Label(self.Frame_1, text='Basic Salary', font=('arial', 12, 'bold'), bg='#090844',fg='white')
            self.Label_BasicSalary.grid(row=11, column=0, sticky=W,padx=20)

            self.Label_OTHours = Label(self.Frame_1, text='OT Hours', font=('arial', 12, 'bold'), bg='#090844',fg='white')
            self.Label_OTHours.grid(row=12, column=0, sticky=W, padx=20)

            self.Label_OTRate = Label(self.Frame_1, text='OT Rate', font=('arial', 12, 'bold'), bg='#090844',fg='white')
            self.Label_OTRate.grid(row=13, column=0, sticky=W, padx=20)

            self.Label_Travelling_Allowances = Label(self.Frame_1, text='Travelling Allowances', font=('arial', 12, 'bold'), bg='#090844',fg='white')
            self.Label_Travelling_Allowances.grid(row=14, column=0, sticky=W, padx=20)

            self.Label_CashAdvance = Label(self.Frame_1, text='Cash Advance', font=('arial', 12, 'bold'), bg='#090844',fg='white')
            self.Label_CashAdvance.grid(row=15, column=0, sticky=W, padx=20)

            self.Label_Loan = Label(self.Frame_1, text='Loan', font=('arial', 12, 'bold'), bg='#090844',fg='white')
            self.Label_Loan.grid(row=16, column=0, sticky=W, padx=20)



            # ========================================================Entries of Frame_1========================================================
            self.Entry_EmpNo = Entry(self.Frame_1, font=('arial', 12, 'bold'), textvariable=self.EmpNo)
            self.Entry_EmpNo.grid(row=0, column=1, padx=10, pady=5)

            self.Entry_FirstName = Entry(self.Frame_1, font=('arial', 12, 'bold'), textvariable=self.FirstName)
            self.Entry_FirstName.grid(row=1, column=1, padx=10, pady=5)

            self.Entry_LastName = Entry(self.Frame_1, font=('arial', 12, 'bold'), textvariable=self.LastName)
            self.Entry_LastName.grid(row=2, column=1, padx=10, pady=5)

            self.Entry_Age = Entry(self.Frame_1, font=('arial', 12, 'bold'), textvariable=self.Age)
            self.Entry_Age.grid(row=3, column=1, padx=10, pady=5)

            self.Entry_Gender = Entry(self.Frame_1, font=('arial', 12, 'bold'), textvariable=self.Gender)
            self.Entry_Gender.grid(row=4, column=1, padx=10, pady=5)

            self.Entry_Status = Entry(self.Frame_1, font=('arial', 12, 'bold'), textvariable=self.status)
            self.Entry_Status.grid(row=5, column=1, padx=10, pady=5)

            self.Entry_Address = Entry(self.Frame_1, font=('arial', 12, 'bold'), textvariable=self.Address)
            self.Entry_Address.grid(row=6, column=1, padx=10, pady=5)

            self.Entry_ContactNo = Entry(self.Frame_1, font=('arial', 12, 'bold'), textvariable=self.ContactNo)
            self.Entry_ContactNo.grid(row=7, column=1, padx=10, pady=5)

            self.Entry_Email = Entry(self.Frame_1, font=('arial', 12, 'bold'), textvariable=self.Email)
            self.Entry_Email.grid(row=8, column=1, padx=10, pady=5)

            self.Entry_Position = Entry(self.Frame_1, font=('arial', 12, 'bold'), textvariable=self.Position)
            self.Entry_Position.grid(row=9, column=1, padx=10, pady=5)

            self.Entry_DateHired = Entry(self.Frame_1, font=('arial', 12, 'bold'), textvariable=self.DateHired)
            self.Entry_DateHired.grid(row=10, column=1, padx=10, pady=5)

            self.Entry_BasicSalary = Entry(self.Frame_1, font=('arial', 12, 'bold'), textvariable=self.BasicSalary)
            self.Entry_BasicSalary.grid(row=11, column=1, padx=10, pady=5)

            self.Entry_OTHours= Entry(self.Frame_1, font=('arial', 12, 'bold'), textvariable=self.OTHours)
            self.Entry_OTHours.grid(row=12, column=1, padx=10, pady=5)

            self.Entry_OTRate = Entry(self.Frame_1, font=('arial', 12, 'bold'), textvariable=self.OTRate)
            self.Entry_OTRate.grid(row=13, column=1, padx=10, pady=5)

            self.Entry_Travelling_Allowances = Entry(self.Frame_1, font=('arial', 12, 'bold'), textvariable=self.Travelling_Allowances)
            self.Entry_Travelling_Allowances.grid(row=14, column=1, padx=10, pady=5)

            self.Entry_CashAdvance = Entry(self.Frame_1, font=('arial', 12, 'bold'), textvariable=self.CashAdvance)
            self.Entry_CashAdvance.grid(row=15, column=1, padx=10, pady=5)

            self.Entry_Loan = Entry(self.Frame_1, font=('arial', 12, 'bold'), textvariable=self.Loan)
            self.Entry_Loan.grid(row=16, column=1, padx=10, pady=5)


            # ========================================================Buttons of self.Frame_3=========================================================

            self.btnDisplay = Button(self.Frame_3, text='DISPLAY', font=('arial', 12, 'bold'), width=8, command=Display)
            self.btnDisplay.grid(row=0, column=1, padx=10, pady=10)

            self.btnReset = Button(self.Frame_3, text='RESET', font=('arial', 12, 'bold'), width=8, command=Reset)
            self.btnReset.grid(row=0, column=2, padx=10, pady=10)

            self.btnUpdate = Button(self.Frame_3, text='UPDATE', font=('arial', 12, 'bold'), width=8, command=Update)
            self.btnUpdate.grid(row=0, column=3, padx=10, pady=10)

            self.btnDelete = Button(self.Frame_3, text='DELETE', font=('arial', 12, 'bold'), width=8, command=Delete)
            self.btnDelete.grid(row=0, column=4, padx=10, pady=10)

            self.btnSave = Button(self.Frame_3, text='SAVE', font=('arial', 12, 'bold'), width=8, command=Add)
            self.btnSave.grid(row=0, column=0, padx=10, pady=10)

            self.btnSearch = Button(self.Frame_3, text='SEARCH', font=('arial', 12, 'bold'), width=8, command=Search)
            self.btnSearch.grid(row=0, column=5, padx=10, pady=10)

            self.btnExit = Button(self.Frame_3, text='EXIT', font=('arial', 12, 'bold'), width=8, command=Exit)
            self.btnExit.grid(row=0, column=6, padx=10, pady=10)

            # ===============================================List Box and self.scrollbar========================================================
            self.scrollbar = Scrollbar(self.Frame_2)
            self.scrollbar.grid(row=0, column=1, sticky='ns')

            self.listbox = Listbox(self.Frame_2, width=100, height=30, font=('arial', 12, 'bold'))
            self.listbox.bind('<<ListboxSelect>>', EmpRec)
            self.listbox.grid(row=0, column=0)
            self.scrollbar.config(command=self.listbox.yview)

        information()


root = Tk()

obj = emp_info(root)

root.mainloop()
