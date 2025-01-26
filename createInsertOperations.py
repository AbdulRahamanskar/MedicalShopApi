import sqlite3
from datetime import date
import uuid
#create users
def createInsertUsers(name,mobile_no,email,password,address,pincode):
    conn = sqlite3.connect("medical_db.db")
    cursor = conn.cursor()

    user_id=str(uuid.uuid4())
    date_of_joined = date.today()

    cursor.execute('''
    INSERT INTO Users(user_id,name,mobile_no,email,password,level,date_of_joined,isApproved,block,address,pincode)
    VALUES(?,?,?,?,?,?,?,?,?,?,?)       
    ''',(user_id,name,mobile_no,email,password,1,date_of_joined,0,0,address,pincode))
    conn.commit()
    conn.close()

    return user_id

#add products

def insertProductsInfo(product_name,stock,product_price,product_category,product_expiry_date):
    conn=sqlite3.connect("medical_db.db")
    cursor = conn.cursor()
    product_id=str(uuid.uuid4())
    cursor.execute('''INSERT INTO Products(product_id,product_name,stock,product_price,product_category,product_expiry_date)
                   VALUES(?,?,?,?,?,?)
                   ''',(product_id,product_name,stock,product_price,product_category,product_expiry_date))
    
    conn.commit()
    conn.close()
    return product_id

#create orders
def insertOrdersInfo(total_amount,user_name,product_price,product_name,order_status,payment_method,
                     payment_status,expected_delivery_date,order_quantity):
    conn = sqlite3.connect("medical_db.db")
    cursor = conn.cursor()
    order_id=str(uuid.uuid4())
    user_id=str(uuid.uuid4())
    product_id = str(uuid.uuid4())
    order_date=date.today()
    cursor.execute('''INSERT INTO Orders
                   (order_id,user_id,product_id,isApproved,total_amount,product_price,user_name,
                   product_name,order_status,payment_method,payment_status,expected_delivery_date,
                   order_date,order_quantity) VALUES
                   (?,?,?,?,?,?,?,?,?,?,?,?,?,?);
                   ''',(order_id,user_id,product_id,0,total_amount,user_name,product_price,product_name,
                        order_status,payment_method,payment_status,
                        expected_delivery_date,order_date
                        ,order_quantity))
    conn.commit()
    conn.close()


#insert sell history

def insertSellHistory(sell_id,product_id,quantity,remaining_stock,price,total_amount,product_name,user_name
                      ,user_id):
    conn=sqlite3.connect("medical_db.db")
    cursor = conn.cursor()
    sell_id=str(uuid.uuid4())
    cursor.execute('''INSERT INTO sellHistory(
                   sell_id,product_id,quantity,remaining_stock,price,total_amount,product_name,user_name,
                   user_id) VALUES (?,?,?,?,?,?,?,?,?)
                   
                   ''',(sell_id,product_id,quantity,remaining_stock,price,total_amount,product_name,user_name,
                        user_id))
    conn.commit()
    conn.close()






