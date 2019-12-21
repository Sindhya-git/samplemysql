from flask import Flask, render_template, json, request, session, redirect
from flask_mysqldb import MySQL
from wtforms import Form, StringField, TextAreaField, PasswordField, validators, SelectField
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
  
 #form = LoadForm(request.form)
  print("inside home page",)  
  cur = mysql.connection.cursor()
  values = 'Clothing'
  cur.execute("SELECT * FROM XXIBM_PRODUCT_CATALOGUE WHERE FAMILY_NAME=%s LIMIT 4", (values,))
  shirts = cur.fetchall()
 # Close Connection
  cur.close()
  return render_template('home.html', shirts=shirts)


    
if __name__ == "__main__":
    application.run()
