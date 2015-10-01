#!/usr/bin/env python

# example helloworld2.py

import pygtk
import gtk
from users import *

users = Users()

class Main:
	def delete_event(self, widget, event, data=None):
		print "delete_event occured!"
		gtk.main_quit()
		return False

	def save(self, widget):
		self.info = [self.firstName.get_text(), self.lastName.get_text(), self.phoneNum.get_text(), self.email.get_text()]
		users.add(self.info[0], self.info)
		users.save()
		self.firstName.set_text("")
		self.lastName.set_text("")
		self.phoneNum.set_text("")
		self.email.set_text("")
		print "Saving!"

	def delete(self, widget, data=None):
		try:
			users.remove(self.entryDelete.get_text())
			users.save()
			self.entryDelete.set_text("")
		except:
			self.entryDelete.set_text("")
			em = gtk.MessageDialog(None, gtk.DIALOG_DESTROY_WITH_PARENT, gtk.MESSAGE_ERROR, gtk.BUTTONS_CLOSE, "Invalid Username")
			em.set_position(gtk.WIN_POS_CENTER)
			em.run()
			em.destroy()

	def listDetails(self, widget):
		key = widget.get_text()
		widget.set_text("")
		try:
			self.firstNameLabel.set_text(users.lib[key][0])
			self.lastNameLabel.set_text(users.lib[key][1])
			self.phoneNumLabel.set_text(users.lib[key][2])
			self.emailLabel.set_text(users.lib[key][3])
		except:
			self.firstNameLabel.set_text("")
			self.lastNameLabel.set_text("")
			self.phoneNumLabel.set_text("")
			self.emailLabel.set_text("")
			em = gtk.MessageDialog(None, gtk.DIALOG_DESTROY_WITH_PARENT, gtk.MESSAGE_ERROR, gtk.BUTTONS_CLOSE, "The user " + key + " does not exist.")
			em.set_position(gtk.WIN_POS_CENTER)
			em.run()
			em.destroy()

	def enterPressed(self, widget, data):
		if data.keyval == 65293:
			print "Enter key pressed"
			self.listDetails(self.listDetailsEntry)
			return True
		return False

	def listCurUser(self, widget):
		print "you tried"
		dialog = gtk.AboutDialog()
		dialog.set_program_name("Users")
		dialog.set_border_width(10)
		dialog.set_size_request(500,250)
		dialog.set_position(gtk.WIN_POS_CENTER)
		for i in users.lib:
			label = gtk.Label(i)
			label.show()
			dialog.vbox.pack_start(label)
		dialog.run()
		dialog.destroy()

	def test(self, widget):
		widget.set_text("")

	def __init__(self):
		# Create a new window
		self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)

		# This is a new call, which just sets the title of our
		# new window to "Hello Buttons!"
		self.window.set_title("Dictionary")
		self.window.set_position(gtk.WIN_POS_CENTER)
		self.window.set_size_request(1300,130)

		# Here we just set a handler for delete_event that immediately
		# exits GTK.
		self.window.connect("delete_event", self.delete_event)
		self.window.connect("key-press-event", self.enterPressed)

		# Sets the border width of the window.
		self.window.set_border_width(10)

		#horizontal box storing all of the vertical boxes
		self.mainBox = gtk.HBox(True, 5)

		#Verticle box containing info for new users
		self.vBox = gtk.VBox(True, 5)

		#Horizontal box containing name info for new users
		self.box = gtk.HBox(True)

		self.label = gtk.Label("	First name:	")
		self.box.pack_start(self.label)

		self.firstName = gtk.Entry()
		self.box.pack_start(self.firstName)

		self.label = gtk.Label("	Last name:	")
		self.box.pack_start(self.label)

		self.lastName = gtk.Entry()
		self.box.pack_start(self.lastName)

		#packing the name info before resetting the horizontal box value
		self.vBox.pack_start(self.box)
		self.box = gtk.HBox()

		#The horizontal box for phone number info
		self.label = gtk.Label("Phone Number:")
		self.box.pack_start(self.label)

		self.phoneNum = gtk.Entry()
		self.box.pack_start(self.phoneNum)

		#packing the phone info before resetting the horizontal box value
		self.vBox.pack_start(self.box)
		self.box = gtk.HBox()

		self.label = gtk.Label("Email:")
		self.box.pack_start(self.label)

		self.email = gtk.Entry()
		self.box.pack_start(self.email)

		self.vBox.pack_start(self.box)
		self.box = gtk.HBox()

		#The button that calls the function that takes all the data the new user inputted
		#and saves it to the user library
		self.button = gtk.Button("Sign Up")
		self.button.connect("clicked", self.save)
		self.box.pack_start(self.button)

		self.vBox.pack_start(self.box)
		self.mainBox.pack_start(self.vBox)
		
		#Vertical box for delete user and list user data
		self.vBox = gtk.VBox(False, 10)

		#Horizontal box for delete user label and combo box
		self.box = gtk.HBox()

		self.label = gtk.Label("	Delete User:	")
		self.box.pack_start(self.label)

		#vertical box for the combo and delete button
		self.deleteBox = gtk.VBox()

		self.entryDelete = gtk.Entry()
		self.deleteBox.pack_start(self.entryDelete)

		self.deleteButton = gtk.Button("Delete")
		self.deleteButton.connect("clicked", self.delete)
		self.deleteBox.pack_start(self.deleteButton)

		self.box.pack_start(self.deleteBox)

		self.vBox.pack_start(self.box)
		self.box = gtk.HBox()

		self.label = gtk.Label("	List Details of User:	")
		self.box.pack_start(self.label)

		self.listDetailsEntry = gtk.Entry()
		self.box.pack_start(self.listDetailsEntry)

		self.vBox.pack_start(self.box)
		self.box = gtk.HBox()

		self.button = gtk.Button("List Current Users")
		self.button.connect("clicked", self.listCurUser)
		self.box.pack_start(self.button)

		self.vBox.pack_start(self.box)

		self.mainBox.pack_start(self.vBox)
		self.vBox = gtk.VBox()

		self.box = gtk.HBox()

		self.label = gtk.Label("	First Name:	")
		self.box.pack_start(self.label)

		self.firstNameLabel = gtk.Label("")
		self.box.pack_start(self.firstNameLabel)

		self.label = gtk.Label("	Last Name:	")
		self.box.pack_start(self.label)

		self.lastNameLabel = gtk.Label("")
		self.box.pack_start(self.lastNameLabel)

		self.vBox.pack_start(self.box)
		self.box = gtk.HBox()

		self.label = gtk.Label("	Phone Number:	")
		self.box.pack_start(self.label)


		self.phoneNumLabel = gtk.Label("")
		self.box.pack_start(self.phoneNumLabel)

		self.label = gtk.Label("	Email:	")
		self.box.pack_start(self.label)

		self.emailLabel = gtk.Label("")
		self.box.pack_start(self.emailLabel)

		#Packing like we're moving to Kansas
		self.vBox.pack_start(self.box)
		self.mainBox.pack_start(self.vBox)

		self.vBox = gtk.VBox()
		
		self.window.add(self.mainBox)
		self.window.show_all()


def main():
	gtk.main()

if __name__ == "__main__":
	hello = Main()
	main()