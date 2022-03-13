import sqlite3

def connect():
       conn = sqlite3.connect("employee.db")
       cur = conn.cursor()

       cur.execute("CREATE TABLE IF NOT EXISTS EmployeeINFO (EmpNo INTEGER PRIMARY KEY , FirstName TEXT,LastName TEXT,Age INTEGER ,Gender TEXT,Status TEXT,Address TEXT,ContactNo TEXT,Email TEXT,\
       Position TEXT,DateHired TEXT ,BasicSalary FLOAT ,OTHours INTEGER ,OTRate INTEGER ,Travelling_Allowances REAL ,CashAdvance REAL ,Loan REAL)")

       conn.commit()
       conn.close()

def insert(EmpNo = " ", FirstName = " ", LastName = " ", Age = " ", Gender = " ", status = " ", Address = " ", ContactNo = " ",Email=" ",Position=" ",DateHired=" ",BasicSalary=" ",OTHours=" ",OTRate=" ",Travelling_Allowances=" ",CashAdvance =" ",Loan= " "):
       conn = sqlite3.connect("employee.db")
       cur = conn.cursor()

       cur.execute("INSERT INTO EmployeeINFO VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", (EmpNo , FirstName, LastName , Age , Gender , status , Address , ContactNo ,Email,Position,DateHired,BasicSalary,OTHours,OTRate,Travelling_Allowances,CashAdvance ,Loan))

       conn.commit()
       conn.close()


def view():
       conn = sqlite3.connect("employee.db")
       cur = conn.cursor()

       cur.execute("SELECT * FROM EmployeeINFO")
       rows = cur.fetchall()
       return rows

       conn.close()

def delete(EmpNo):
       conn = sqlite3.connect("employee.db")
       cur = conn.cursor()

       cur.execute("DELETE FROM EmployeeINFO WHERE EmpNo = ?", (EmpNo,))

       conn.commit()
       conn.close()

def update(EmpNo = " ", FirstName = " ", LastName = " ", Age = " ", Gender = " ", status = " ", Address = " ", ContactNo = " ",Email=" ",Position=" ",DateHired=" ",BasicSalary=" ",OTHours=" ",OTRate=" ",Travelling_Allowances=" ",CashAdvance =" ",Loan= " "):
       conn = sqlite3.connect("employee.db")
       cur = conn.cursor()

       cur.execute("UPDATE EmployeeINFO SET EmpNo = ? OR FirstName = ? OR LastName = ? OR Age = ? OR Gender = ? OR status = ? OR Address = ? OR ContactNo = ? Email = ? OR Position = ? OR DateHired = ? OR BasicSalary = ?OR OTHours = ? OR OTRate = ? OR Travelling_Allowances = ? OR CashAdvance = ? OR Loan = ? ", \
                   (EmpNo , FirstName, LastName , Age , Gender , status , Address , ContactNo ,Email,Position,DateHired,BasicSalary,OTHours,OTRate,Travelling_Allowances,CashAdvance ,Loan))

       conn.commit()
       conn.close()

def search(EmpNo = " ", FirstName = " ", LastName = " ", Age = " ", Gender = " ", status = " ", Address = " ", ContactNo = " ",Email=" ",Position=" ",DateHired=" ",BasicSalary=" ",OTHours=" ",OTRate=" ",Travelling_Allowances=" ",CashAdvance =" ",Loan= " "):
       conn = sqlite3.connect("employee.db")
       cur = conn.cursor()

       cur.execute("SELECT * FROM EmployeeINFO WHERE EmpNo = ? OR FirstName = ? OR LastName = ? OR Age = ? OR Gender = ? OR Status = ? OR Address = ? OR ContactNo = ? OR Email = ? OR Position = ? OR DateHired = ? OR BasicSalary= ? OR OTHours = ? OR OTRate = ? OR Travelling_Allowances = ? OR CashAdvance = ? OR Loan = ? \
                      ", (EmpNo , FirstName, LastName , Age , Gender , status , Address , ContactNo ,Email,Position,DateHired,BasicSalary,OTHours,OTRate,Travelling_Allowances,CashAdvance ,Loan))
       rows = cur.fetchall()
       return rows

       conn.close()



connect()

