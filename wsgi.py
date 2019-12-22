from flask import Flask, render_template, json, request, session, redirect
from flask_mysqldb import MySQL
from wtforms import Form, StringField, TextAreaField, PasswordField, validators, SelectField
from functools import wraps
import os

#Initialize flask
application = Flask(__name__)
# Config MySQL
mysql = MySQL()
application.config['MYSQL_HOST']  = "custom-mysql.gamification.svc.cluster.local"
application.config['MYSQL_USER']  = "xxuser"
application.config['MYSQL_PASSWORD'] = "welcome1"
application.config['MYSQL_DB']    = "sampledb"
application.config['MYSQL_PORT']  = int('3306')
application.config['MYSQL_CURSORCLASS'] = 'DictCursor'

# Initialize the app for use with this MySQL class
mysql.init_app(application)

@application.route("/")
def home_page():
  if 'view' in request.args:
    item_number= request.args['view']
    print ("item number is :", item_number)
    cur2 = mysql.connection.cursor()
    cur2.execute("SELECT s.ITEM_NUMBER, s.DESCRIPTION,s.LONG_DESCRIPTION, s.SKU_ATTRIBUTE_VALUE1,s.SKU_ATTRIBUTE_VALUE2,p.LIST_PRICE,p.DISCOUNT FROM XXIBM_PRODUCT_SKU s INNER JOIN XXIBM_PRODUCT_PRICING p WHERE s.ITEM_NUMBER=%s LIMIT 1", (item_number,))
    product1 = cur2.fetchall()
    print("product1 is :",product1)
    return render_template('product_detail.html', prdtdetail=product1)
  else:
    print("inside home page",)  
    cur1 = mysql.connection.cursor()
    values = 'Clothing'
    cur1.execute("SELECT s.ITEM_NUMBER, s.DESCRIPTION,s.LONG_DESCRIPTION, s.SKU_ATTRIBUTE_VALUE1,s.SKU_ATTRIBUTE_VALUE2,p.LIST_PRICE,p.DISCOUNT FROM XXIBM_PRODUCT_SKU s INNER JOIN XXIBM_PRODUCT_PRICING p WHERE s.ITEM_NUMBER=p.ITEM_NUMBER LIMIT 25")
    shirts = cur1.fetchall()
 # Close Connection
    cur1.close()
    return render_template('home.html', shirts=shirts)

  

    
if __name__ == "__main__":
    application.run()
