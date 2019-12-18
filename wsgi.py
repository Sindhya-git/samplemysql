from flask import Flask, render_template, json, request, session, redirect
#from wtforms import Form, BooleanField, StringField, PasswordField, validators
import MySQLdb
import os

#Initialize flask
app = Flask(__name__)
app.config['IMAGES_DEST'] = 'static/images'

# Config MySQL
mysql = MySQL()
app.config['MYSQL_HOST'] = "custom-mysql.gamification.svc.cluster.local"
app.config['MYSQL_USER'] = "xxuser"
app.config['MYSQL_PASSWORD'] = "welcome1"
app.config['MYSQL_DB'] = "sampledb"
app.config['MYSQL_PORT'] = int('3306')

# Initialize the app for use with this MySQL class
mysql.init_app(app)


@app.route("/")
def home_page():
  #form = LoadForm(request.form)
  print("inside home page")  
  cur = mysql.connection.cursor()
  values = 'Shirts'
  cur.execute("SELECT COMMODITY_NAME FROM XXIBM_PRODUCT_CATALOGUE WHERE CLASS_NAME=%s ORDER BY RAND() LIMIT 1", (values,))
  shirts = cur.fetchall()
  print("shirt fetched:", shirts)
  values = 'Shoes'
  cur.execute("SELECT COMMODITY_NAME FROM XXIBM_PRODUCT_CATALOGUE WHERE CLASS_NAME=%s ORDER BY RAND() LIMIT 1", (values,))
  shoes = cur.fetchall()
  print("shoes fetched:", shoes)
  values = 'Luggage'
  cur.execute("SELECT COMMODITY_NAME FROM XXIBM_PRODUCT_CATALOGUE WHERE CLASS_NAME=%s ORDER BY RAND() LIMIT 1", (values,))
  luggage = cur.fetchall()
  print("luggage  fetched:", luggage)
  return render_template('home.html')

@app.route("/search",methods=['GET', 'POST'])
def get_dbdata():
  db = db_init()
  score = storage.score()
  return score

class dbinit():

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
    cur.execute("SELECT * FROM XXIBM_PRODUCT_SKU")
    row = cur.fetchall()

    return row[0]

if __name__ == "__main__":
    application.run()
