import sqlite3

class Database:

    def __init__(self,db):
        self.conn=sqlite3.connect(db)
        self.cur=self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS passwords (id INTEGER PRIMARY KEY, Name text,Password text)")
        self.conn.commit()
       

    def insert(self,name,password):
        self.cur.execute("INSERT INTO passwords VALUES (NULL,?,?)",(name,password))
        self.conn.commit()
        
    def view(self):
        self.cur.execute("SELECT * FROM passwords")
        rows=self.cur.fetchall()
        return rows

    def delete(self,id):
        self.cur.execute("DELETE FROM passwords WHERE id=?",(id,))
        self.conn.commit()
            
    def __del__(self):
        self.conn.close()
