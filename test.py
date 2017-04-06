import mysql.connector
from mysql.connector import Error
import getpass

try:
	conn = mysql.connector.connect(host='localhost', database='contact_manager', user='root', password='root')
	cursor = conn.cursor()
	if conn.is_connected():
		print('Connected to Contact Manager database\n')
except Error as e:
		print(e)


class contactmgr:
	b = 0
	user = " "
	pswrd = " "


	def register(self):
		# Get registration information
		print "Welcome to registration page:"
		user = raw_input('USER: ')
		pswrd = getpass.getpass('PASS: ')
		confirmpswrd = getpass.getpass('CONFIRM PASS: ')

		if pswrd != confirmpswrd:
			print "Passwords do not match"
		else:
			# Insert registration information to database
			query = ("""SELECT count(*) from logindetails WHERE username = %s""")
			cursor.execute(query, (user,))
			data = cursor.fetchone()
			print data
			if data != (0, ):
				print "User already registered\n"

				self.login()
			else:
				add_user = ("""INSERT into logindetails (username, password) VALUES (%s, %s)""")
				data_user = (user, pswrd)
				cursor.execute(add_user, data_user)
				print "Registration done successfully!\n"
				conn.commit()

				self.login ()


	def login(self):
		# Get login information
		print "Welcome to login page"
		user = raw_input('USER: ')
		pswrd = getpass.getpass('PASS: ')

		query = ("""SELECT username, password FROM logindetails WHERE username = %s and password = %s""")
		data = (user, pswrd)
		logon = cursor.execute(query, data)
		print logon
		if not logon:
			print "Username and password do not match!\n"
		else:
			if not cursor.execute('SELECT profile from logindetails where username = %s and password = %s', (user, pswrd)):
				self.profile(user, pswrd)
			else:
				self.contact_details(user)


	def profile(self, user, pswrd):
		# Input user details
		print "Welcome to profile page"
		print "Enter first name:"
		first = raw_input('> ')
		print "Enter last name:"
		last = raw_input('> ')
		b = 1
		add_profile = ("INSERT into logindetails (Fname, Lname, profile) values (%s, %s, %r) where username=%s and password =%s")
		data_profile = (first, last, b, user, pswrd)
		cursor.execute(add_profile, data_profile)
		print "Profile details for %s added successfully!\n" %(user)
		conn.commit()

		self.contact_details(user)


	def contact_details(self, user):
		#  	Input contact details
		print "Welcome to contact input page"
		print "Enter Name:"
		name = raw_input('> ')
		print "Enter Address:"
		add = raw_input('> ')
		print "Enter Mobile no:"
		mob = raw_input('> ')
		add_contact = ("INSERT into contactdetails (username, Name, mob, address) values (%s, %s, %s, %s)")
		data_contact = (user, name, mob, address)
		cursor.execute(add_contact, data_contact)
		print "Contact details for %s added successfully!\n" %(user)
		conn.commit()


a = contactmgr()
print "Do you wish to continue (y/n)?"
ch = raw_input('>')

while ch == 'Y' or ch == 'y':
    print "What do you wish to do in the database?"
    print "1. New user registration"
    print "2. User login"
    print "3. Exit"
    choice = int(raw_input('> '))

    if choice == 1:
        a.register()
    elif choice == 2:
        a.login()
    elif choice == 3:
        print "Thank you for using Contact Manager"
        #Close the connection
        conn.close()
        exit()
    else :
        print "Enter the correct choice"
