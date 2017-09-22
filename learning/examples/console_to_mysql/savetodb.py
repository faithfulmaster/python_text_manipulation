import mysql.connector
from mysql.connector import Error


def connect():
    # Connect to database
    try:
        conn = mysql.connector.connect(host='localhost', database='Project',
                                       user='root', password='root')
        cursor = conn.cursor()
        if conn.is_connected():
            print('Connected to MySQL database')
    except Error as e:
        print(e)

    print "Do you wish to start (y/n)?"
    ch = raw_input('> ')

    while ch == 'Y' or 'y':
        print "What do you wish to do in the database?"
        print "1. Enter employee details"
        print "2. Display employee table"
        print "3. Delete employee record"
        print "4. Close and exit the database"
        choice = int(raw_input('> '))
        if choice == 1:
            # Insert a new entry
            print "Enter employee name and department name"
            empname = raw_input('> ')
            empdept = raw_input('> ')
            add_employee = ("insert into emp (name, dept) values (%s, %s)")
            data_employee = (empname, empdept)
            cursor.execute(add_employee, data_employee)
            print "Added a new entry\n"
            conn.commit()

        elif choice == 2:
            # Display the table data
            print "The entries in the employee table are as follows:"
            show_employee = ("select * from emp;")
            cursor.execute(show_employee)
            print "\nEmp Id   Name    Dept\n"
            for (name, dept, emp_id) in cursor:
                print ("{}        {}     {}".format(emp_id, name, dept))

        elif choice == 3:
            # Delete a record as per user input
            print "Enter employee name whose record is to be deleted"
            empname = raw_input('> ')
            del_employee = ("delete from emp where name = %s")
            cursor.execute(del_employee, (empname,))
            print "Deleted a entry\n"
            conn.commit()

        elif choice == 4:
            # Close the connection
            cursor.close()
            conn.close()
            exit(0)

        else:
            # Wrong user choice
            print "Enter the correct choice"
            continue

        print "Do you wish to continue (y/n)?"
        ch = raw_input('> ')


if __name__ == '__main__':
    connect()
