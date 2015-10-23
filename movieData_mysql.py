import mysql.connector

class Data:

    def __init__(self):
        self.conn = mysql.connector.connect(user="root", password="Anthony1", database="data")
        self.cur = self.conn.cursor()
        self.refreshList()

    def refreshList(self):
        self.movieList = []
        self.cur.execute("SELECT * FROM movies;")
        for i in self.cur:
            self.movieList.append(i)
        self.conn.commit()

    def addMovie(self, values):
        self.cur.execute("INSERT INTO movies VALUES (%s, %s, %s, %s)", (values))
        self.refreshList()

    def remMovie(self, values):
        self.cur.execute("DELETE FROM movies WHERE movieName = %s AND genre = %s AND releaseDate = %s AND rating = %s", (values))
        self.refreshList()
