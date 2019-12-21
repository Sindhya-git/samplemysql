from flask import Flask, render_template, json, request, session, redirect
from flask_mysqldb import MySQL
from wtforms import Form, StringField, TextAreaField, PasswordField, validators, SelectField
import os

#Initialize flask
app = Flask(__name__)
# Config MySQL
mysql = MySQL()
app.config['MYSQL_HOST']  = "custom-mysql.gamification.svc.cluster.local"
app.config['MYSQL_USER']  = "xxuser"
app.config['MYSQL_PASSWORD'] = "welcome1"
app.config['MYSQL_DB']    = "sampledb"
app.config['MYSQL_PORT']  = int('3306')
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

# Initialize the app for use with this MySQL class
mysql.init_app(app)


@application.route("/")
def home_page():
  
 #form = LoadForm(request.form)
  print("inside home page",)  
  cur = mysql.connection.cursor()
  values = 'Shirts'
  cur.execute("SELECT * FROM XXIBM_PRODUCT_CATALOGUE WHERE FAMILY_NAME=%s LIMIT 4", (values,))
  shirts = cur.fetchall()
 # Close Connection
  cur.close()
  return render_template('home.html', shirts=shirts)


def get_dbdata():
  db = dbget()
  
class dbget():

  def __init__(self):

    self.db = MySQLdb.connect(
      user   = "xxuser",
      passwd = "welcome1",
      db     ="sampledb",
      host   = "custom-mysql.gamification.svc.cluster.local",
      port   = int('3306')
    )
    cur = self.db.cursor()

  def score(self):
    cur = self.db.cursor()
    print("in score",)
    values = 'Clothing'
    cur.execute("SELECT COMMODITY,COMMODITY_NAME INTO @commodity , @commodity_name FROM XXIBM_PRODUCT_CATALOGUE WHERE FAMILY_NAME=%s LIMIT 1", (values,))
    row = cur.fetchall()
    print("row is:", row )
    return str(row)

if __name__ == "__main__":
    app.run()
