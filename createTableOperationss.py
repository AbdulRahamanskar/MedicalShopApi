import sqlite3


def createUsersTables():
    conn = sqlite3.connect("medical_db.db")
    cursor = conn.cursor()
    cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   user_id VARCHAR(255),
                   name VARCHAR(255),
                   mobile_no VARCHAR(50),
                   email VARCHAR(255),
                   password VARCHAR(255),
                   level INT,
                   date_of_joined DATE,
                   isApproved BOOLEAN,
                   block BOOLEAN,
                   address VARCHAR(255),
                   pincode VARCHAR(10)

                   );
''')
    
    conn.commit()
    conn.close()

#create products table
def createProductsTables():
    conn = sqlite3.connect("medical_db.db")
    cursor= conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS Products(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   product_id VARCHAR(255),
                   product_name VARCHAR(255),
                   stock VARCHAR(255),
                   product_price VARCHAR(100),
                   product_category VARCHAR(255),
                   product_expiry_date DATE);
                   ''')
    conn.commit()
    conn.close()

#create orders table
def createOrdersTable():
    conn=sqlite3.connect("medical_db.db")
    cursor = conn.cursor()

    cursor.execute('''
                   CREATE TABLE IF NOT EXISTS Orders(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   order_id VARCHAR(255),
                   user_id VARCHAR(255),
                   product_id VARCHAR(255),
                   isApproved BOOLEAN,
                   total_amount VARCHAR(255),
                   product_price VARCHAR(255),
                   user_name VARCHAR(255),
                   product_name VARCHAR(255),
                   order_status VARCHAR(255),
                   payment_method VARCHAR(255),
                   payment_status VARCHAR(255),
                   expected_delivery_date DATE,
                   order_date DATE,
                   order_quantity INT
                   ); 
                   ''')
    conn.commit()
    conn.close()


#Create sell History

def createSellHistory():
    conn=sqlite3.connect("medical_db.db")
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS sellHistory(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   sell_id VARCHAR(255),
                   product_id VARCHAR(255),
                   quantity VARCHAR(255),
                   remaining_stock VARCHAR(255),
                   price VARCHAR(255),
                   total_amount VARCHAR(255),
                   product_name VARCHAR(255),
                   user_name VARCHAR(255),
                   user_id VARCHAR(255)) 
                   ''')
    conn.commit()
    conn.close()            