# Anthony George
# anthony.george@dixiesuccess.org
# 2015
# 
# Executes the gtkgui class that carries out the rest of the program
#
#
# October 8, 2015: Anthony George
# 	created everything


# importing required modules
import pygtk
pygtk.require("2.0")
import gtk
import gtkgui_users, userData_mysql

# main class to execute and start gtk
def main():
	gtk.main()

# creates class objects and starts the gui
if __name__ == "__main__":
	DATA = userData_mysql.Data()
	GUI = gtkgui_users.GTKGUI(DATA)
	main()
