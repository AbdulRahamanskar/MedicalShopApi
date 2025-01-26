import sqlite3

def updateUsersAllFields(user_id,**kargs):
    conn = sqlite3.connect("medical_db.db")
    cursor = conn.cursor()
    for key,values in kargs.items():
        if key=="name":
         cursor.execute("UPDATE Users SET name=?  WHERE user_id=? ",(values,user_id))
        elif key=="email":
           cursor.execute("UPDATE Users SET email=? WHERE user_id=?",(values,user_id))
        elif key=="password":
           cursor.execute("UPDATE Users SET password=? WHERE user_id=?",(values,user_id))
        elif key=="mobile_no": 
           cursor.execute("UPDATE Users SET mobile_no=? WHERE user_id=?",(values,user_id))
        elif key=="level": 
           cursor.execute("UPDATE Users SET level=? WHERE user_id=?",(values,user_id))
        elif key=="date_of_joined": 
           cursor.execute("UPDATE Users SET date_of_joined=? WHERE user_id=?",(values,user_id))  
        elif key=="isApproved": 
           cursor.execute("UPDATE Users SET isApproved=? WHERE user_id=?",(values,user_id))  
        elif key=="block": 
           cursor.execute("UPDATE Users SET block=? WHERE user_id=?",(values,user_id))
        elif key=="address": 
           cursor.execute("UPDATE Users SET address=? WHERE user_id=?",(values,user_id))
        elif key=="pincode": 
           cursor.execute("UPDATE Users SET pincode=? WHERE user_id=?",(values,user_id))              
                
    conn.commit()
    conn.close()

#update products

def updateAllProducts(product_id,**kargs):
   conn = sqlite3.connect("medical_db.db")
   cursor=conn.cursor()
   for key,values in kargs.items():
      if key=="product_name":
         cursor.execute("UPDATE Products SET product_name=? WHERE product_id=?",(values,product_id))
   
      elif key=="stock":
         cursor.execute("UPDATE Products SET stock=? WHERE product_id=?",(values,product_id))
      elif key=="product_price":
         cursor.execute("UPDATE Products SET product_price=? WHERE product_id=?",(values,product_id))
      elif key=="product_category":
         cursor.execute("UPDATE Products SET product_category=? WHERE product_id=?",(values,product_id))
      elif key=="product_expiry_date":
         cursor.execute("UPDATE Products SET product_expiry_date=? WHERE product_id=?",(values,product_id))   
   conn.commit()
   conn.close()


#update order details


def updateAllOrders(order_id,**kargs):
   conn = sqlite3.connect("medical_db.db")
   cursor=conn.cursor()
   for key,values in kargs.items():
      if key=="order_status":
         cursor.execute("UPDATE Orders SET order_status=? WHERE order_id=?",(values,order_id))
   
      elif key=="payment_method":
         cursor.execute("UPDATE Orders SET payment_method=? WHERE order_id=?",(values,order_id))
      elif key=="payment_status":
         cursor.execute("UPDATE Orders SET payment_status=? WHERE order_id=?",(values,order_id))
      elif key=="expected_delivery_date":
         cursor.execute("UPDATE Orders SET expected_delivery_date=? WHERE order_id=?",(values,order_id))
      elif key=="order_quantity":
         cursor.execute("UPDATE Orders SET order_quantity=? WHERE order_id=?",(values,order_id))   
   conn.commit()
   conn.close()

    