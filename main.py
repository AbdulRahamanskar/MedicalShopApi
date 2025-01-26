
# A very simple Flask Hello World app for you to get started with...

from flask import Flask,jsonify,request
from db.createTableOperationss import createUsersTables,createProductsTables,createOrdersTable,createSellHistory
from db.createInsertOperations import createInsertUsers,insertProductsInfo,insertOrdersInfo
from db.readOperations import getAllUsers,getSpecificProduct,getAllProducts,getSpecificUser,getAllOrders,gettingOfSellHistory
from db.updateOperations import updateUsersAllFields, updateAllProducts,updateAllOrders
from db.auth import userLogin
from db.deleteOperations import deleteSpecificUser,deleteSpecificProduct

app = Flask(__name__)

@app.route('/',methods=['GET'])
def home():
    return jsonify({"name":"Abdul Rahaman","age":20})

#signup
@app.route('/signUp',methods=['POST'])
def signup():
    try:
        name = request.form['name']
        mobile_no = request.form['mobile_no']
        email = request.form['email']
        password = request.form['password']
        address = request.form['address']
        pincode = request.form['pincode']

        data = createInsertUsers(name=name,mobile_no=mobile_no,email=email,password=password,address=address,pincode=pincode)
        if data:
          return jsonify({"status":200,"message":"Your account has been Created..."})
        else:
          return jsonify({"status":400,"message":"Something went wrong"})
    except Exception as e:
     return jsonify({"status":400, "message":str(e)})

    # return jsonify(data)

 #get specific user

@app.route('/getSpecifiUser',methods=['POST'])
def getSpecificUserMain():
   try:
      user_id=request.form['user_id']
      userInfo= getSpecificUser(user_id=user_id)
      return userInfo
   except Exception as e:
      return jsonify({"status":404,"message":str(e)})

#addproducts
@app.route('/addProducts',methods=['POST'])
def addProductsMain():
    try:
       product_name = request.form['product_name']
       stock = request.form['stock']
       product_price = request.form['product_price']
       product_category = request.form['product_category']
       product_expiry_date = request.form['product_expiry_date']
       product_data = insertProductsInfo(product_name=product_name,stock=stock,product_price=product_price,product_category=product_category,product_expiry_date=product_expiry_date)
       if product_data:
        return jsonify({"status":200,"message":"Products added...!"})
       else:
        return jsonify({"status":400,"message":"something went wrong"})
    except  Exception as e:
       return jsonify({"status":400,"message":str(e)})

#update users
@app.route('/updateUser',methods=['PATCH'])
def updateUserMain():
   try:
      user_id=request.form['user_id']
      fields=request.form.items()
      updateUserDict={}

      for key, values in fields:
         if key!='user_id':
            updateUserDict[key]=values
      updateUsersAllFields(user_id=user_id,**updateUserDict)
      return jsonify({"status":200,"message":"User Updated"})
   except Exception as e:
      return jsonify({"status":404,"message":str(e)})

#delete specific user
@app.route('/deleteSpecificUser',methods=['DELETE'])
def deleteSpecificUserMain():
   try:
      user_id=request.form['user_id']
      deleteUser=deleteSpecificUser(user_id=user_id)
      if user_id != None:
       return jsonify({"status":200,"message":"User deleted successfully","user":deleteUser})
      else:
       return jsonify({"status":200,"message":"Something went wrong"})

   except Exception as e:
      return jsonify({"status":400,"message":str(e)})

#addproducts
@app.route('/getAllUsers',methods=['GET'])
def getAllUsersMain():
    try:
       return getAllUsers()
    except Exception as e:
       return jsonify({"status":400,"message":str(e)})

#getspecificproducts

@app.route('/getspecificproduct',methods=['POST'])
def getSpecificProductMain():
   try:
    product_id=request.form['product_id']
    get_specific_product_here=getSpecificProduct(product_id=product_id)
    return get_specific_product_here
   except Exception as e:
    return jsonify({"status":404,"message":str(e)})


#getallproducts
@app.route('/getAllProducts',methods=['GET'])
def getAllProductsMain():

   return getAllProducts()

@app.route('/login',methods=['POST'])
def loginMain():
   try:
      email=request.form['email']
      password=request.form['password']
      authLogin= userLogin(email=email,password=password)
      if authLogin:
         return jsonify({"Status":200,"message":authLogin[1]})
      else:
         return jsonify({"status":400,"message":"Incorrect email or password"})
   except Exception as e:
      return jsonify({"status":400,"message":str(e)})

#update products
@app.route('/updateProducts',methods=['PATCH'])
def updateAllProductsMain():
   try:
         product_id=request.form['product_id']
         allFields=request.form.items()

         updateProductsDict={}
         for key, values in allFields:
          if key!="product_id":
           updateProductsDict[key]=values
           updateAllProducts(product_id=product_id,**updateProductsDict)
           return jsonify({"Status":200,"message":"Product Updated..."})

   except Exception as e:
    return jsonify({"status":400,"message":str(e)})

#delete specific product
@app.route('/deleteSpecficProduct',methods=['DELETE'])
def deleteSpecificProductMain():
   try:
      product_id=request.form['product_id']
      delete_specific_product=deleteSpecificProduct(product_id=product_id)
      deleted_product_details= getSpecificProduct(product_id=product_id)
      if product_id!=None:
         return jsonify({"status":200,
                         "Product Deleted":delete_specific_product,
                         "Product Details": deleted_product_details})
   except Exception as e:
      return jsonify({"status":400,"message":str(e)})

 #add orders details
@app.route('/insertOrdersDetails',methods=['POST'])
def insertOrdersMain():
   try:
      total_amount=request.form['total_amount']
      user_name=request.form['user_name']
      product_name=request.form['product_name']
      product_price=request.form['product_price']
      order_status=request.form['order_status']
      payment_method = request.form['payment_method']
      payment_status = request.form['payment_status']
      expected_delivery_date = request.form['expected_delivery_date']
      order_quantity = request.form['order_quantity']
      insert_order_data = insertOrdersInfo(total_amount=total_amount,user_name=user_name,product_name=product_name,
                                           product_price=product_price,order_status=order_status,
                                           payment_method= payment_method,payment_status=payment_status,
                                           expected_delivery_date=expected_delivery_date,order_quantity=order_quantity)
      return jsonify({"status":200,"message":insert_order_data})
   except Exception as e:
      return jsonify({"status":400,"message":str(e)})


# get all orders

@app.route('/getOrders',methods=['GET'])
def getAllOrdersMain():
   try:
      getallorders=getAllOrders()
      return jsonify({"status":200,"message":getallorders})
   except Exception as e:
      return jsonify({"status":400,"message:":str(e)})

#update order details
@app.route('/updateOrders',methods=['PATCH'])
def updateAllOrdersMain():
   try:
         order_id=request.form['order_id']
         allFields=request.form.items()
         updateOrdersDict={}

         for key, values in allFields:
           if key!="order_id":
            updateOrdersDict[key]=values
            updateAllOrders(order_id==order_id,**updateOrdersDict)
            return jsonify({"Status":200,"message":"Order Updated..."})

   except Exception as e:
    return jsonify({"status":400,"message":str(e)})

#getting of sales history

@app.route('/getSalesHistory',methods=['GET'])
def gettSalesHistoryMain():
   try:
    user_id=request.form['user_id']
    get_salesHistory=gettingOfSellHistory(user_id=user_id)
    return jsonify({"Message":get_salesHistory,})
   except Exception as e:
      return jsonify({"status":400,"message":str(e)})


#main
if __name__ == "__main__":
    createUsersTables()
    createProductsTables()
    createOrdersTable()
    createSellHistory()
    app.run(debug= True)
