import mysql.connector

class Data:

    def __init__(self):
        self.conn = mysql.connector.connect(user="root", password="Anthony1", database="data")
        self.cur = self.conn.cursor()
        self.refreshList()

    def refreshList(self):
        self.userList = []
        self.cur.execute("SELECT * FROM users;")
        for i in self.cur:
            self.userList.append(i)
        self.conn.commit()

    def addUser(self, values):
        self.cur.execute("INSERT INTO users VALUES (%s, %s, %s, %s)", (values))
        self.refreshList()

    def remUser(self, values):
        self.cur.execute("DELETE FROM users WHERE firstName = %s AND lastName = %s AND phoneNumber = %s AND email = %s", (values))
        self.refreshList()
