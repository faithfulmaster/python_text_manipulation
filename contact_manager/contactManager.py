#!/usr/bin/python

import MySQLdb
import re
import getpass
from bcrypt import hashpw, gensalt

# Open database connection ( If database is not created don't give dbname)
conn = MySQLdb.connect("localhost","root","root")

# Prepare a cursor object using cursor() method
cursor = conn.cursor()

# Below line  is to hide the warning
cursor.execute("SET sql_notes = 0; ")

# create database here
cursor.execute("create database IF NOT EXISTS contactmanager")
cursor.execute("use contactmanager;")

# Create tables
cursor.execute("SET sql_notes = 0; ")
cursor.execute("""create table IF NOT EXISTS logindetails
				(username varchar(20), password text, profile varchar(2),
                Fname varchar(10), Lname varchar(10),
				PRIMARY KEY (username));""")
cursor.execute("SET sql_notes = 1; ")

cursor.execute("SET sql_notes = 0; ")
cursor.execute("""create table IF NOT EXISTS contactdetails
                (username varchar(20), Name varchar(20),
                mob varchar(15), address varchar(30),
                FOREIGN KEY (username) REFERENCES logindetails(username));""")
cursor.execute("SET sql_notes = 1; ")

# Commit your changes in the database
conn.commit()

# Create a class
class ContactMgr:
	user = " "
	pswrd = " "


	def register(self):

		# Get registration information
		print "\nWelcome to registration page:"
		user = raw_input('USER: ')
		pswrd = getpass.getpass('PASS: ')

		# Check if password is alphanumeric
		valpass = self.passwordcheck(pswrd)
		if valpass == True:
			self.register()

		# Encrypt the password
		hashed = hashpw(pswrd, gensalt())
		confirmpswrd = getpass.getpass('CONFIRM PASS: ')

		if pswrd != confirmpswrd:
			print "Passwords do not match"
			self.register()
		else:
			# Insert registration information if username is not registered already
			query = ("""SELECT count(*) from logindetails WHERE username = %s""")
			cursor.execute(query, (user,))
			data = cursor.fetchone()
			if data != (0, ):
				print "User already registered\n"
				self.login()
			else:
				# Insert registration information to database
				add_user = ("""INSERT into logindetails (username, password) VALUES (%s, %s)""")
				data_user = (user, hashed)
				cursor.execute(add_user, data_user)
				print "Registration done successfully!"
				conn.commit()
				self.login ()

	def passwordcheck(self, pswrd):

		# Function to check if password entered is alphanumeric and does not have whitespace characters
		x = True
		while x:
		    if (len(pswrd)<6 or len(pswrd)>12):
		        break
		    elif not (re.search("[a-z]",pswrd) or re.search("[A-Z]",pswrd)):
		        break
		    elif not re.search("[0-9]",pswrd):
		        break
		    elif re.search("\s",pswrd):
		        break
		    else:
		        return False
		        break
		if x:
			print "Not a Valid Password"
			print "Password should be alphanumeric of length 6 to 12 characters"
			return True

	def login(self):

		# Get login information
		print "\nWelcome to login page"
		user = raw_input('USER: ')
		pswrd = getpass.getpass('PASS: ')

		# Check if username exists in database
		query = ("""SELECT username FROM logindetails WHERE username = %s""")
		cursor.execute(query, (user,))
		data = cursor.fetchone()
		if data == None:
			print "This username does not exist"
			return

		# Login to database if username and password entered match
		query = ("""SELECT password FROM logindetails WHERE username = %s""")
		cursor.execute(query, (user,))
		hashed = cursor.fetchone()
		if hashpw(pswrd, hashed[0]) != hashed[0]:
			print "Username and password do not match!\n"
			return
		else:
			cursor.execute('SELECT profile from logindetails WHERE username = %s', (user,))
			data = cursor.fetchone()

			# Check if user profile details are available in database
			if data == (0,) or data == (None,):
				print "You are successfully logged in\n"
				self.profile(user)
			else:
				print "You are successfully logged in\n"
				self.contact_details(user)


	def profile(self, user):

		# Input user profile details
		print "Welcome to your profile page %s" %(user)
		print "Enter first name:"
		first = raw_input('> ')
		print "Enter last name:"
		last = raw_input('> ')
		add_profile = ("""UPDATE logindetails SET Fname = %s, Lname = %s, profile = 1 WHERE username=%s""")
		data_profile = (first, last, user)
		cursor.execute(add_profile, data_profile)
		print "Profile details for %s added successfully!\n" %(user)
		conn.commit()
		self.contact_details(user)

	def contact_details(self, user):

		# Input contact details
		print "Hi %s ! Welcome to your contact page \n" %(user)

		ch = 'Y'
		while ch == 'y' or ch == 'Y':
			print "Your options:"
			print "1. Enter a new contact"
			print "2. Display all contacts"
			print "3. Logout"
			inp = int(raw_input('>'))

			# Input a new contact
			if inp == 1:
				print "Enter Name:"
				name = raw_input('> ')
				print "Enter Address:"
				add = raw_input('> ')
				print "Enter Mobile no:"
				mob = raw_input('> ')
				add_contact = ("INSERT into contactdetails (username, Name, mob, address) VALUES (%s, %s, %s, %s)")
				data_contact = (user, name, mob, add)
				cursor.execute(add_contact, data_contact)
				print "Contact details for %s added successfully!\n" %(name)
				conn.commit()

			# Display all contacts
			elif inp == 2:
				cursor.execute('SELECT Name, mob, address from contactdetails WHERE username = %s', (user,))
				print "\nName   		Mob no.    		Address\n"
				for (Name, mob, address) in cursor:
  					print("{}        {}     {}".format(Name, mob, address))

			# Logout of contact page
			elif inp == 3:
				return

			print "\nWanna continue? (y/n)"
			ch = raw_input('>')

		if ch == 'n' or ch =='N':
				return


# Creating an instance of a class
a = ContactMgr()
ch = 'y'

while ch == 'Y' or ch == 'y':
    print "\nWhat do you wish to do in the database?"
    print "1. New user registration"
    print "2. User login"
    print "3. Exit"
    choice = int(raw_input('> '))

	# Invoking functions with the help of class object for registration and login
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

	print "Do you wish to continue (y/n)?"
	ch = raw_input('>')
