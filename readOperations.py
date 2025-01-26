import sqlite3
import json

def getAllUsers():
    conn = sqlite3.connect("medical_db.db")
    cursor=conn.execute("SELECT * FROM Users")
    getUsers = cursor.fetchall()
    conn.close()

    newUserJson=[]

    for users in getUsers:
        tempUser={
            "id":users[0],
            "user_id":users[1],
            "name":users[2],
            "mobile_no":users[3],
            "email":users[4],
            "password":users[5],
            "level":users[6],
            "date_of_joined":users[7],
            "isApproved":users[8],
            "block":users[9],
            "address":users[10],
            "pincode":users[11]


        }
        newUserJson.append(tempUser)


    return json.dumps(newUserJson)

def getSpecificUser(user_id):
    conn=sqlite3.connect("medical_db.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Users WHERE user_id=?",(user_id,))
    user = cursor.fetchall()
    conn.close()

    specifiUserJson=[]

    for userinfo in user:
        tempuserInfo={
            "id":userinfo[0],
            "user_id":userinfo[1],
            "name":userinfo[2],
            "mobile_no":userinfo[3],
            "email":userinfo[4],
            "password":userinfo[5],
            "level":userinfo[6],
            "date_of_joined":userinfo[7],
            "isApproved":userinfo[8],
            "block":userinfo[9],
            "address":userinfo[10],
            "pincode":userinfo[11]
        }
        specifiUserJson.append(tempuserInfo)

    return json.dumps(specifiUserJson)



#get specific product

def getSpecificProduct(product_id):
    conn=sqlite3.connect("medical_db.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Products WHERE product_id=?",(product_id,))
    product = cursor.fetchall()
    conn.close()

    specifiProductJson=[]

    for productInfo in product:
        tempProductInfo={
             "id":productInfo[0],
            "product_id":productInfo[1],
            "product_name":productInfo[2],
            "stock":productInfo[3],
            "product_price":productInfo[4],
            "product_category":productInfo[5],
            "product_expiry_date":productInfo[6]
        }
        specifiProductJson.append(tempProductInfo)

    return json.dumps(specifiProductJson)



def getAllProducts():
    conn = sqlite3.connect("medical_db.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Products")
    conn.close
    getProducts=cursor.fetchall()
    productJson = []
    for getproduct in getProducts:
        tempProducts={
            "id":getproduct[0],
            "product_id":getproduct[1],
            "product_name":getproduct[2],
            "stock":getproduct[3],
            "product_price":getproduct[4],
            "product_category":getproduct[5],
            "product_expiry_date":getproduct[6]

        }
        productJson.append(tempProducts)
        return json.dumps(productJson)
#get all orders    
def getAllOrders():
    conn = sqlite3.connect("medical_db.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Orders")
    conn.close
    getOrders=cursor.fetchall()
    orderJson = []
    for getOrder in getOrders:
        tempOrders={
            "id":getOrder[0],
            "order_id":getOrder[1],
            "order_status":getOrder[2],
            "payment_method":getOrder[3],
            "payment_status":getOrder[4],
            "expected_delivery_date":getOrder[5],
            "order_date":getOrder[6],
            "order_quantity":getOrder[7]

        }
        orderJson.append(tempOrders)
        return json.dumps(orderJson)
    
#getting of sell History

def gettingOfSellHistory(user_id):
    conn=sqlite3.connect("medical_db.db")
    cursor=conn.cursor()
    # cursor.fetchall()
    cursor.execute('''    
        SELECT sellHistory.*,Users.user_id,Users.name FROM sellHistory
                   INNER JOIN USERS ON sellHistory.user_id=Users.user_id
                   WHERE Users.user_id=?
                  ''',(user_id,))
        # Fetch all rows from the result
    result = cursor.fetchall()

    # Close the database connection
    conn.close()

    return result