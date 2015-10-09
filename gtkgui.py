# Anthony George
# anthony.george@dixiesuccess.org
# 2015
#
# Makes a gui using gtk that connects to dict.py and does database stuff using sqlite
#
#
# Sometime in the past: Anthony George
# 	created everything without documentation
#
#
# October 8, 2015: Anthony George
# 	add comments and documentation
#
#
# October 9, 2015: Anthony George
# 	fully implement sqlite3


# importing required modules
import pygtk
pygtk.require("2.0")
import gtk

# declaring the gtkgui class
class GTKGUI:

	# handles the delete event and exits the program
	def delete_event(self, widget, event, data=None):
		gtk.main_quit()
		return False

	# checks to see if all the feilds are filled out then saves them if they are, otherwise, 
	# a dialog box comes up telling them they didn't fill out all the feilds.
	def save(self, widget, data):
		if data and self.firstNameEntry.get_text() != "" \
		and self.lastNameEntry.get_text() != "" \
		and self.phoneNumEntry.get_text() != "" \
		and self.emailEntry.get_text() != "":
			self.DATA.add(self.firstNameEntry.get_text(), (self.firstNameEntry.get_text(), 
				self.lastNameEntry.get_text(), self.phoneNumEntry.get_text(), self.emailEntry.get_text()))

		elif data:
			dialog = gtk.Dialog("Error")
			dialog.set_position(gtk.WIN_POS_CENTER)
			dialog.set_size_request(200, 100)

			label = gtk.Label("Please fill all the boxes.")
			dialog.vbox.pack_start(label)

			dialog.add_button("Close", 1)

			dialog.vbox.show_all()

			dialog.run()
			dialog.destroy()

	# checks to see if the user wanted to delete
	# deletes if they wanted to, doesn't if they didn't
	def delAnswer(self, widget, data):
		if data == "yes":
			self.DATA.remove(self.DATA.userList[self.curUser][1])
			self.next(None)
		else:
			pass

	# changes the data to the previous feild in the database
	def previous(self, widget):
		try:
			self.curUser -= 1
			self.firstNameLabel.set_text(self.DATA.userList[self.curUser][1])
		except:
			self.curUser = len(self.DATA.userList)-1
			self.firstNameLabel.set_text(self.DATA.userList[self.curUser][1])
		self.lastNameLabel.set_text(self.DATA.userList[self.curUser][2])
		self.phoneNumLabel.set_text(self.DATA.userList[self.curUser][3])
		self.emailLabel.set_text(self.DATA.userList[self.curUser][4])

	# dialog box asking the user if they're sure they mean't to press delete
	def delete(self, widget):
		dialog = gtk.Dialog("Are you sure?")
		dialog.set_position(gtk.WIN_POS_CENTER)
		dialog.set_size_request(250, 75)

		label = gtk.Label("Are you sure you want to delete this user?")
		dialog.vbox.pack_start(label)

		button = dialog.add_button("Yes", 1)
		button.connect("clicked", self.delAnswer, "yes")

		button = dialog.add_button("No", 1)
		button.connect("clicked", self.delAnswer, "no")

		dialog.vbox.show_all()

		dialog.run()
		dialog.destroy()

	# dialog box with feilds to fill out to add a user
	def add(self, widget):

		# initiating the dialog box
		dialog = gtk.Dialog("Add User")
		dialog.set_border_width(10)
		dialog.set_size_request(500, 200)
		dialog.set_position(gtk.WIN_POS_CENTER)
		dialog.vbox.set_spacing(5)
		hBox = gtk.HBox()    
		box = gtk.VBox(True, 5)

		# creating and adding labels
		label = gtk.Label("First Name:")
		box.pack_start(label)

		label = gtk.Label("Last Name:")
		box.pack_start(label)

		label = gtk.Label("Phone Number:")
		box.pack_start(label)

		label = gtk.Label("Email Address:")
		box.pack_start(label)

		# packing everything into the hbox and reseting the value of the vbox
		hBox.pack_start(box)
		box = gtk.VBox(True, 5)

		# creating and adding entry boxes
		self.firstNameEntry = gtk.Entry()
		box.pack_start(self.firstNameEntry)

		self.lastNameEntry = gtk.Entry()
		box.pack_start(self.lastNameEntry)

		self.phoneNumEntry = gtk.Entry()
		box.pack_start(self.phoneNumEntry)

		self.emailEntry = gtk.Entry()
		box.pack_start(self.emailEntry)

		# packing everything into the hbox and then the hbox into the dialog box
		hBox.pack_start(box)
		dialog.vbox.pack_start(hBox)

		# adding buttons for the dialog box
		button = dialog.add_button("Cancel", 1)
		button.connect("clicked", self.save, False)

		test = dialog.add_button("Sign Up!", 1)
		test.connect("clicked", self.save, True)

		# running the dialog before destroying it
		dialog.vbox.show_all()
		dialog.run()
		dialog.destroy()

	# display the next entry in the database
	def next(self, widget):
		try:
			self.curUser += 1
			self.firstNameLabel.set_text(self.DATA.userList[self.curUser][1])
		except:
			self.curUser = 0
			self.firstNameLabel.set_text(self.DATA.userList[self.curUser][1])
		self.lastNameLabel.set_text(self.DATA.userList[self.curUser][2])
		self.phoneNumLabel.set_text(self.DATA.userList[self.curUser][3])
		self.emailLabel.set_text(self.DATA.userList[self.curUser][4])

	# the main method
	def __init__(self, DATA):

		# gets the dictionary off of the data class
		self.DATA = DATA

		# initiate variables and window object
		self.curUser = 0
		self.window = gtk.Window()
		self.window.set_title("Dictionary")
		self.window.set_position(gtk.WIN_POS_CENTER)
		#self.window.set_size_request(400,125)
		self.window.connect("delete_event", self.delete_event)
		self.window.set_border_width(10)

		# declaring box variables
		self.vBox = gtk.VBox(False, 7)
		self.hBox = gtk.HBox(True, 0)
		self.box = gtk.VBox(True, 5)

		# creating and adding labels to self.box
		self.label = gtk.Label("First Name:")
		self.box.pack_start(self.label)

		self.label = gtk.Label("Last Name:")
		self.box.pack_start(self.label)

		self.label = gtk.Label("Phone Number:")
		self.box.pack_start(self.label)

		self.label = gtk.Label("Email:")
		self.box.pack_start(self.label)

		# packing self.box into hbox then hbox into vbox and reseting the value of self.box
		self.hBox.pack_start(self.box)
		self.vBox.pack_start(self.hBox)
		self.box = gtk.VBox()

		# initiatlly setting the values for each label
		self.firstNameLabel = gtk.Label(self.DATA.userList[self.curUser][1])
		self.box.pack_start(self.firstNameLabel)

		self.lastNameLabel = gtk.Label(self.DATA.userList[self.curUser][2])
		self.box.pack_start(self.lastNameLabel)

		self.phoneNumLabel = gtk.Label(self.DATA.userList[self.curUser][3])
		self.box.pack_start(self.phoneNumLabel)

		self.emailLabel = gtk.Label(self.DATA.userList[self.curUser][4])
		self.box.pack_start(self.emailLabel)

		# packing and reseting the value of self.box
		self.hBox.pack_start(self.box)
		self.box = gtk.HBox(True, 5)

		# making the buttons, connecting them to their respecting methods and packing to self.box
		self.button = gtk.Button("<< Previous")
		self.button.connect("clicked", self.previous)
		self.box.pack_start(self.button)

		self.button = gtk.Button("Delete")
		self.button.connect("clicked", self.delete)
		self.box.pack_start(self.button)

		self.button = gtk.Button("Add")
		self.button.connect("clicked", self.add)
		self.box.pack_start(self.button)

		self.button = gtk.Button("Next >>")
		self.button.connect("clicked", self.next)
		self.box.pack_start(self.button)

		#packing everything up and showing it
		self.vBox.pack_start(self.box)
		self.window.add(self.vBox)
		self.window.show_all()