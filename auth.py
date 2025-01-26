import sqlite3

def userLogin(email,password):
    conn = sqlite3.connect("medical_db.db")
    cursor= conn.cursor()
    cursor.execute("SELECT * FROM Users where email=? AND password=?",(email,password))
    user=cursor.fetchone()
    conn.close()
    return user
