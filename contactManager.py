import mysql.connector
from mysql.connector import Error
import getpass

try:
	conn = mysql.connector.connect(host='localhost', database='contact_manager', user='root', password='root')
	cursor = conn.cursor()
	if conn.is_connected():
		print('Connected to Contact Manager database')
except Error as e:
		print(e)


class contactmgr:
	b = 0
	user = " "
	pswrd = " "


	def register(self):
		print cursor
		# Get registration information
		user = raw_input('USER: ')
		pswrd = getpass.getpass('PASS: ')
		confirmpswrd = getpass.getpass('CONFIRM PASS: ')

		if pswrd != confirmpswrd:
			print "Passwords do not match"
		else:
			# Insert registration information to database
			print type(user)
			query = ("""SELECT count(*)
						from logindetails
					   WHERE username = %s""")
			cursor.execute(query, (user,))
			print cursor
			if cursor.rowcount != 0:
				print "User already registered"
			else:
				b = 0
				add_user = ("INSERT into logindetails (username, password, profile) values (%s, %s, %d)")
				data_user = (user, pswrd, b)
				cursor.execute(add_user, data_user)
				print "Registration done successfully!\n"
				conn.commit()

	def login():
		# Get login information
		user = raw_input('USER: ')
		pswrd = getpass.getpass('PASS: ')

		query = 'SELECT username, password from logindetails where username = %s and password = %s'
		data = (user, pswrd)
		logon = cursor.execute(query, data)
		if not logon:
			print "Username and password do not match!"
		else:
			profile()


	def profile():
		# Input user details
		print "Enter first name:"
		first = raw_input('> ')
		print "Enter last name:"
		last = raw_input('> ')
		b = True
		add_profile = ("INSERT into logindetails (Fname, Lname, profile) values (%s, %s, %r) where username=%s and password =%s")
		data_profile = (first, last, b, user, pswrd)
		cursor.execute(add_profile, data_user)
		print "Profile details for %s added successfully!\n" %(user)
		conn.commit()


	# def contact_details():
	# 	Input contact details


a = contactmgr()
a.register()

# 	print "Do you wish to continue (y/n)?"
#     ch = raw_input('>')
#
# 	c = contactmgr
# 	c.connect()
#
#     while ch == 'Y' or 'y':
#         print "What do you wish to do in the database?"
#         print "1. New user registration"
#         print "2. User login and profile page"
#         print "3. Input contact details"
# 		print "4. Exit"
#         choice = int(raw_input('> '))
#
# 		if choice == 1:
# 			c.register()
# 		elif choice == 2:
# 			c.login()
# 		elif choice == 3:
# 			c.contact_details()
# 		elif choice == 4:
# 			print "Thank you for using Contact Manager"
# 			# Close the connection
#             cursor.close()
#             conn.close()
#             exit(0)
# 		else:
# 			print "Enter the correct choice"
