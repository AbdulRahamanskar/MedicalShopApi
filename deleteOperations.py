import sqlite3

def deleteSpecificUser(user_id):
    conn = sqlite3.connect("medical_db.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Users WHERE user_id=?",(user_id,))
    conn.commit()
    conn.close()

def deleteSpecificProduct(product_id):
    conn = sqlite3.connect("medical_db.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Products WHERE product_id=?",(product_id,))
    conn.commit()
    conn.close()    