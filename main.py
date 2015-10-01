from __future__ import print_function

from users import *
import os

users = Users()

def main():
	running = True
	clr = lambda: os.system('cls')
	while running:
		print("What would you like to do?\n1. List current users\n2. Add User\n3. Delete User\n4. List Details of a User\n5. Login\n6. Nothing\n7. Nothing\n8. Nothing\n9. Exit")
		user_input = raw_input()

		if user_input == "1":
			clr()
			for key in users.lib:
				print(key)
			print("\nPress enter to continue")
			asdf = raw_input()
			clr()

		elif user_input == "2":
			clr()
			print "Enter First Name"
			user_firstName = raw_input()
			clr()
			print "Enter Last Name"
			user_lastName = raw_input()
			clr()
			print "Enter Age"
			user_age = raw_input()
			clr()
			print "Enter Hair Color"
			user_hairColor = raw_input()
			clr()
			print "Enter Phone Number"
			user_phoneNum = raw_input()
			clr()
			print "Create Password"
			user_password = raw_input()
			user_keyname = user_lastName[:3].upper()+str(user_phoneNum[6:])
			users.add(user_keyname, [user_firstName, user_lastName, user_age, user_hairColor, user_password])
			clr()
			users.save()

		elif user_input == "3":
			clr()
			print "Enter Keyname (First three letters of last name, last four digits of phone number)"
			try:
				users.remove(raw_input())
				users.save()
				clr90
			except:
				print "Invalid Keyname"
			clr()

		elif user_input == "4":
			clr()
			print "Enter keyname (First three letters of last name, last four digits of phone number)"
			user_request = raw_input()
			found = False
			for key in users.lib:
				if user_request == key:
					print users.lib[key]
					found = True

			if not found:
				print "Invalid keyname"
			print "\nPress enter to continue"
			asdf = raw_input()
			clr()

		elif user_input == "5":
			clr()
			print "Enter Username"
			user_username = raw_input()
			clr()
			print "Enter Password"
			user_password = raw_input()
			if user_password == users.lib[user_username][3]:
				print "Success!"
			else:
				print "Incorrect username or password"
			clr()

		elif user_input == "9":
			users.save()
			running = False

		else:
			clr()

main()