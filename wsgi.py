from flask import Flask, render_template, json, request, session, redirect
import MySQLdb
import os

#Initialize flask
application = Flask(__name__)

@application.route("/")
def home_page():
  return render_template("home.html")

@application.route("/data")
def get_dbdata():
  storage = Storage()
  score = storage.score()
  return score

class Storage():

  def __init__(self):
    
    print("initializing DB")
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
    print("row is ", row)
    return str(row)

if __name__ == "__main__":
    application.run()
