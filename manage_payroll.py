from tkinter import *

import tkinter.messagebox

import manage_employee_back




class emp_info():
    def __init__(self, master):
        self.master = master
        self.master.title('Manage Payroll')
        self.master.geometry('1600x3000')
        self.master.config(bg='#090844')

        def information():
            # ========================================================Variables=====================================================================
            self.EmpNo = StringVar()
            self.FirstName = StringVar()
            self.LastName = StringVar()
            self.Position = StringVar()
            self.BasicSalary = StringVar()
            self.OTHours = StringVar()
            self.OTRate = StringVar()
            self.Travelling_Allowances = StringVar()
            self.CashAdvance = StringVar()
            self.Loan = StringVar()
            self.OTpayment = StringVar()
            self.GrossSalary = StringVar()
            self.EPF = StringVar()
            self.TotalDeduction = StringVar()
            self.NetSalary = StringVar()
            self.EPFcom_con = StringVar()

            #===================Pay slip========================================
            def Receipt():
                self.Display.delete('1.0', END)
                self.Display.insert(
                    END, '\t\tPay sheet' + '\n\n\n')
                self.Display.insert(
                    END, '\tEMP No.\t : ' + self.EmpNo.get() + '\n')
                self.Display.insert(
                    END, '\tFirst Name   : ' + self.FirstName.get() + '\n')
                self.Display.insert(
                    END, '\tLast Name.\t : ' + self.LastName.get() + '\n')
                self.Display.insert(
                    END, '\tPosition\t : ' + self.Position.get() + '\n\n')
                self.Display.insert(
                    END, '\tBasic Salary\t : ' + self.BasicSalary.get() + '\n\n')
                self.Display.insert(
                    END, '\tOT Hours \t : ' + self.OTHours.get() + '\n\n')
                self.Display.insert(
                    END, '\tOT Rate \t : ' + self.OTRate.get() + '\n\n')
                self.Display.insert(
                    END, '\tTravelling Allowances \t : ' + self.Travelling_Allowances.get() + '\n\n')
                self.Display.insert(
                    END, '\tCash Advance \t : ' + self.CashAdvance.get() + '\n\n')
                self.Display.insert(
                    END, '\tLoan \t : ' + self.Loan.get() + '\n\n')
                self.Display.insert(
                    END, '\tOT Payment \t : ' + self.OTpayment.get() + '\n\n')
                self.Display.insert(
                    END, '\tGross Salary \t : ' + self.GrossSalary.get() + '\n\n')
                self.Display.insert(
                    END, '\tEPF \t : ' + self.EPF.get() + '\n\n')
                self.Display.insert(
                    END, '\tTotal Deduction \t : ' + self.TotalDeduction.get() + '\n\n')
                self.Display.insert(
                    END, '\tNet Salary \t : ' + self.NetSalary.get() + '\n\n')
                self.Display.insert(
                    END, '\tEPF Company contribution \t : ' + self.EPFcom_con.get() + '\n\n')


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

                    self.Entry_Position.delete(0, END)
                    self.Entry_Position.insert(END, selected_tuple[9])

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
                self.Position.set('')
                self.BasicSalary.set('')
                self.OTHours.set('')
                self.OTRate.set('')
                self.Travelling_Allowances.set('')
                self.CashAdvance.set('')
                self.Loan.set('')
                self.OTpayment.set('')
                self.GrossSalary.set('')
                self.EPF.set('')
                self.TotalDeduction.set('')
                self.NetSalary.set('')
                self.EPFcom_con.set('')


                self.listbox.delete(0, END)



            def Search():
                self.listbox.delete(0, END)
                for row in manage_employee_back.search(self.EmpNo.get(), self.FirstName.get(), self.LastName.get(),
                                                       self.Position.get(),self.BasicSalary.get(),self.OTHours.get(),
                                                       self.OTRate.get(), self.Travelling_Allowances.get(),self.CashAdvance.get(),self.Loan.get()):
                    self.listbox.insert(END, row, str(' '))



            def OTpayment():
               a= int(self.OTHours.get())
               b= int(self.OTRate.get())
               c = a * b
               self.OTpayment.set(c)

            def GrossSalary():

                d = float(self.BasicSalary.get())
                e = float(self.OTpayment.get())
                f = float(self.Travelling_Allowances.get())
                g = d + e + f
                self.GrossSalary.set(g)

            def EPF():
                h = float(self.BasicSalary.get())
                i = h * 8/100
                self.EPF.set(i)

            def TotalDeduction():
                j = float(self.CashAdvance.get())
                k = float(self.Loan.get())
                l = float(self.EPF.get())
                m = j + k + l
                self.TotalDeduction.set(m)

            def NetSalary():
                n = float(self.GrossSalary.get())
                o = float(self.TotalDeduction.get())
                p = float(n - o)
                self.NetSalary.set(p)

            def EPFcom_con():
                r = float(self.GrossSalary.get())
                s = float(r * 12/100)
                self.EPFcom_con.set(s)

            def Result():
                Result = (OTpayment(),GrossSalary(),EPF(),TotalDeduction(),NetSalary(),EPFcom_con())
                return



            # ============================================================Frames=====================================================================

            self.Main_Frame = LabelFrame(self.master, width=1800, height=500, font=('arial', 20, 'bold'), \
                                         bg='#090844', bd=15, relief='ridge')
            self.Main_Frame.grid(row=0, column=0, padx=10, pady=20)

            self.Frame_1 = LabelFrame(self.Main_Frame, width=600, height=400, font=('arial', 15, 'bold'), \
                                      relief='ridge', bd=10, bg='#090844',fg='#ecf409', text='SALARY INFORMATION ')
            self.Frame_1.grid(row=1, column=0, padx=10)

            self.Frame_2 = LabelFrame(self.Main_Frame, width=750, height=400, font=('arial', 15, 'bold'), \
                                      relief='ridge', bd=10, bg='#090844',fg='#ecf409', text='EMPLOYEE DATABASE')
            self.Frame_2.grid(row=1, column=1, padx=5)

            self.Frame_3 = LabelFrame(self.master, width=1200, height=100, font=('arial', 10, 'bold'), \
                                      bg='#090844', relief='ridge', bd=13)
            self.Frame_3.grid(row=2, column=0, pady=10)

            self.Frame_4 = LabelFrame(self.Main_Frame, width=490, height=650, font=('arial', 15, 'bold'), \
                        relief='ridge', bd=10, bg='#090844',fg='#ecf409', text='PAY SLIP')
            self.Frame_4.grid(row=1, column=3, padx=5)

            # ========================================================Labels of Frame_1========================================================

            self.Label_EmpNo = Label(self.Frame_1, text='Emp No', font=('arial', 12, 'bold'), bg='#090844',fg='white')
            self.Label_EmpNo.grid(row=0, column=0, sticky=W, padx=20, pady=10)

            self.Label_FirstName = Label(self.Frame_1, text='First Name', font=('arial', 12, 'bold'), bg='#090844',fg='white')
            self.Label_FirstName.grid(row=1, column=0, sticky=W, padx=20)

            self.Label_LastName = Label(self.Frame_1, text='Last Name', font=('arial', 12, 'bold'), bg='#090844',fg='white')
            self.Label_LastName.grid(row=2, column=0, sticky=W, padx=20)

            self.Label_Position = Label(self.Frame_1, text='Position', font=('arial', 12, 'bold'), bg='#090844',fg='white')
            self.Label_Position.grid(row=9, column=0, sticky=W, padx=20)

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

            self.Label_OTpayment = Label(self.Frame_1, text='OTpayment', font=('arial', 12, 'bold'), bg='#090844',fg='white')
            self.Label_OTpayment.grid(row=17, column=0, sticky=W, padx=20)

            self.Label_GrossSalary = Label(self.Frame_1, text='Gross Salary', font=('arial', 12, 'bold'), bg='#090844',fg='white')
            self.Label_GrossSalary.grid(row=18, column=0, sticky=W, padx=20)

            self.Label_EPF = Label(self.Frame_1, text='EPF', font=('arial', 12, 'bold'), bg='#090844',fg='white')
            self.Label_EPF.grid(row=19, column=0, sticky=W, padx=20)

            self.Label_TotalDeduction = Label(self.Frame_1, text='Total Deduction', font=('arial', 12, 'bold'), bg='#090844',fg='white')
            self.Label_TotalDeduction.grid(row=20, column=0, sticky=W, padx=20)

            self.Label_NetSalary = Label(self.Frame_1, text='Net Salary', font=('arial', 12, 'bold'), bg='#090844',fg='white')
            self.Label_NetSalary.grid(row=21, column=0, sticky=W, padx=20)

            self.EPFcom_Con = Label(self.Frame_1, text='EPF company contribution', font=('arial', 12, 'bold'), bg='#090844',fg='white')
            self.EPFcom_Con.grid(row=22, column=0, sticky=W, padx=20)




            # ========================================================Entries of Frame_1========================================================

            self.Entry_EmpNo = Entry(self.Frame_1, font=('arial', 12, 'bold'), textvariable=self.EmpNo)
            self.Entry_EmpNo.grid(row=0, column=1, padx=10, pady=5)

            self.Entry_FirstName = Entry(self.Frame_1, font=('arial', 12, 'bold'), textvariable=self.FirstName)
            self.Entry_FirstName.grid(row=1, column=1, padx=10, pady=5)

            self.Entry_LastName = Entry(self.Frame_1, font=('arial', 12, 'bold'), textvariable=self.LastName)
            self.Entry_LastName.grid(row=2, column=1, padx=10, pady=5)


            self.Entry_Position = Entry(self.Frame_1, font=('arial', 12, 'bold'), textvariable=self.Position)
            self.Entry_Position.grid(row=9, column=1, padx=10, pady=5)

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

            self.Entry_OTpayment = Entry(self.Frame_1, font=('arial', 12, 'bold'), textvariable=self.OTpayment)
            self.Entry_OTpayment.grid(row=17, column=1, padx=10, pady=5)

            self.Entry_GrossSalary = Entry(self.Frame_1, font=('arial', 12, 'bold'), textvariable=self.GrossSalary)
            self.Entry_GrossSalary.grid(row=18, column=1, padx=10, pady=5)

            self.Entry_EPF = Entry(self.Frame_1, font=('arial', 12, 'bold'), textvariable=self.EPF)
            self.Entry_EPF.grid(row=19, column=1, padx=10, pady=5)

            self.Entry_TotalDeduction = Entry(self.Frame_1, font=('arial', 12, 'bold'), textvariable=self.TotalDeduction)
            self.Entry_TotalDeduction.grid(row=20, column=1, padx=10, pady=5)

            self.Entry_NetSalary = Entry(self.Frame_1, font=('arial', 12, 'bold'), textvariable=self.NetSalary)
            self.Entry_NetSalary.grid(row=21, column=1, padx=10, pady=5)

            self.Entry_EPFcom_con = Entry(self.Frame_1, font=('arial', 12, 'bold'), textvariable=self.EPFcom_con)
            self.Entry_EPFcom_con.grid(row=22, column=1, padx=10, pady=5)
##########################################################################################################################

            self.Display = Text(self.Main_Frame, width=49, height=31.4,
                                fg="#9d081a", bg="#a2d7f6",font=('arial', 12, 'bold',))
            self.Display.grid(row=1, column=3, padx=3)

            # ========================================================Buttons of self.Frame_3=========================================================

            self.btnDisplay = Button(self.Frame_3, text='DISPLAY', font=('arial', 12, 'bold'), width=8, command=Display)
            self.btnDisplay.grid(row=0, column=1, padx=10, pady=10)

            self.btnReset = Button(self.Frame_3, text='RESET', font=('arial', 12, 'bold'), width=8, command=Reset)
            self.btnReset.grid(row=0, column=2, padx=10, pady=10)

            self.btnSearch = Button(self.Frame_3, text='SEARCH', font=('arial', 12, 'bold'), width=8, command=Search)
            self.btnSearch.grid(row=0, column=5, padx=10, pady=10)

            self.btnExit = Button(self.Frame_3, text='EXIT', font=('arial', 12, 'bold'), width=8, command=Exit)
            self.btnExit.grid(row=0, column=6, padx=10, pady=10)

            self.btnResult = Button(self.Frame_3, text='Calculate salary', font=('arial', 12, 'bold'), width=16, command=Result)
            self.btnResult.grid(row=0, column=7, padx=10, pady=10)

            self.btnReceipt = Button(self.Frame_3, text='Generate salary report', font=('arial', 12, 'bold'), width=19, command=Receipt)
            self.btnReceipt.grid(row=0, column=8, padx=10, pady=10)


            # ===============================================List Box and self.scrollbar========================================================

            self.scrollbar = Scrollbar(self.Frame_2)
            self.scrollbar.grid(row=0, column=1, sticky='ns')
            self.listbox = Listbox(self.Frame_2, width=50, height=30, font=('arial', 12, 'bold'))
            self.listbox.bind('<<ListboxSelect>>', EmpRec)
            self.listbox.grid(row=0, column=0)
            self.scrollbar.config(command=self.listbox.yview)

        information()


root = Tk()

obj = emp_info(root)

root.mainloop()
