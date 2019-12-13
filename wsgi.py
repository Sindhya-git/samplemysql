from flask import Flask
import MySQLdb
import os
application = Flask(__name__)

@application.route("/")
def hello_world():

  storage = Storage()
  a,b,c,d,e = storage.score()
  print(a)
  return a,b,c,d,e

class Storage():

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
    cur.execute("SELECT * FROM XXIBM_PRODUCT_STYLE")
    row = cur.fetchall()
    print("Total number of row in PRODUCT_SKU is: ", cur.rowcount)
    print("Item Number = ", row, )
    print(row[0],"  ", row[1])
    return row[0], row[1], row[2], row[3], row[4]
    
if __name__ == "__main__":
    application.run()
