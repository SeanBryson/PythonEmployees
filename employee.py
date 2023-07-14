import mysql.connector;

con = mysql.connector.connect(
    host="localhost", user="root", password="root", database="emp")

# Function To Check if Employee with
# given Id Exist or Not
 
def check_employee(employee_id):
 
    # Query to select all Rows f
    # rom employee Table
    sql = 'select * from emp where EmployeeID=%s'
 
    # making cursor buffered to make
    # rowcount method work properly
    c = con.cursor(buffered=True)
    data = (employee_id,)
 
    # Executing the SQL Query
    c.execute(sql, data)
 
    # rowcount method to find
    # number of rows with given values
    r = c.rowcount
     
    if r == 1:
        return True
    else:
        return False

# Function to mAdd_Employee 
def Add_Employ():
 
    Id = input("Enter Employee Id : ")
 
    # Checking if Employee with given Id
    # Already Exist or Not
    if(check_employee(Id) == True):
        print("Employee already exists\nTry Again\n")
        menu()
     
    else:
        FirstName = input("Enter First Name : ")
        LastName = input("Enter Last Name : ")
        DOE = input("Enter Date of Employment : ")
        Salary = input("Enter Employee Salary : ")
        Department = input("Enter Department : ")
        data = (Id, FirstName, LastName, DOE, Salary, Department)
 
        # Inserting Employee details in the Employee
        # Table
        sql = 'insert into emp values(%s,%s,%s,%s,%s,%s)'
        c = con.cursor()
 
        # Executing the SQL Query
        c.execute(sql, data)
 
        # commit() method to make changes in the table
        con.commit()
        print("Employee Added Successfully ")
        menu()

# Function to Remove Employee with given Id
def Remove_Employ():
	Id = input("Enter Employee Id : ")

	# Checking if Employee with given Id
	# Exist or Not
	if(check_employee(Id) == False):
		print("Employee does not exists\nTry Again\n")
		menu()
	
	else:
		
		# Query to Delete Employee from Table
		sql = 'delete from emp where id=%s'
		data = (Id,)
		c = con.cursor()

		# Executing the SQL Query
		c.execute(sql, data)

		# commit() method to make changes in
		# the table
		con.commit()
		print("Employee Removed")
		menu()

# Function to Update Salary
def Update_Salary():
    Id = int(input("Enter Employee Id"))
 
    # Checking if Employee with given Id
    # Exist or Not
    if(check_employee(Id) == False):
        print("Employee does not exists\nTry Again\n")
        menu()
    else:
        Amount = int(input("Enter increase in Salary"))
 
        # Query to Fetch Salary of Employee with
        # given Id
        sql = 'select salary from emp where id=%s'
        data = (Id,)
        c = con.cursor()
 
        # Executing the SQL Query
        c.execute(sql, data)
 
        # Fetching Salary of Employee with given Id
        r = c.fetchone()
        t = r[0]+Amount
 
        # Query to Update Salary of Employee with
        # given Id
        sql = 'update emp set salary=%s where id=%s'
        d = (t, Id)
 
        # Executing the SQL Query
        c.execute(sql, d)
 
        # commit() method to make changes in the table
        con.commit()
        print("Employee Promoted")
        menu()

        # Function to Display All Employees
        # from Employee Table

# Function to Update First Name
def Update_FirstName():
    Id = int(input("Enter Employee Id"))
 
    # Checking if Employee with given Id
    # Exist or Not
    if(check_employee(Id) == False):
        print("Employee does not exists\nTry Again\n")
        menu()
    else:
        fname = input("Enter new first name")
 
        # Query to Update First Name of Employee with
        # given Id
        sql = 'update emp set firstname=%s where id=%s'
        d = (fname, Id)
 
        # Executing the SQL Query
        c = con.cursor()
        c.execute(sql, d)
 
        # commit() method to make changes in the table
        con.commit()
        print("Employee Name Updated")
        menu()

        # Function to Display All Employees
        # from Employee Table

# Function to Update Last Name
def Update_LastName():
    Id = int(input("Enter Employee Id"))
 
    # Checking if Employee with given Id
    # Exist or Not
    if(check_employee(Id) == False):
        print("Employee does not exists\nTry Again\n")
        menu()
    else:
        fname = input("Enter new last name")
 
        # Query to Update Last Name of Employee with
        # given Id
        sql = 'update emp set lastname=%s where id=%s'
        d = (fname, Id)
 
        # Executing the SQL Query
        c = con.cursor()
        c.execute(sql, d)
 
        # commit() method to make changes in the table
        con.commit()
        print("Employee Name Updated")
        menu()

        # Function to Display All Employees
        # from Employee Table
 
def Display_Employees():
     
    # query to select all rows from
    # Employee Table
    sql = 'select * from emp'
    c = con.cursor()
     
    # Executing the SQL Query
    c.execute(sql)
     
    # Fetching all details of all the
    # Employees
    r = c.fetchall()
    for i in r:
        print("Employee Id : ", i[0])
        print("Employee First Name : ", i[1])
        print("Employee Last Name : ", i[2])
        print("Date of Employment : ", i[3])
        print("Employee Salary : ", i[4])
        print("Employee Salary : ", i[5])
        print("-----------------------------\
        -------------------------------------\
        -----------------------------------")
    menu()

    # menu function to display the menu
def menu():
	print("Welcome to Employee Management Record")
	print("Press ")
	print("1 to Add Employee")
	print("2 to Remove Employee")
    print("3 to Update Employee First Name")    
    print("4 to Update Employee First Name")  
    print("5 to Update Salary")
	print("6 to Display Employees")
	print("7 to Exit")
	
	# Taking choice from user
	ch = int(input("Enter your Choice "))
	if ch == 1:
		Add_Employ()
		
	elif ch == 2:
		Remove_Employ()
                          
    elif ch == 3:
        Update_FirstName()

    elif ch == 4:
        Update_FirstName()
		
	elif ch == 5:
		Update_Salary()
		
	elif ch == 6:
		Display_Employees()
		
	elif ch == 7:
		exit(0)
		
	else:
		print("Invalid Choice")
		menu()