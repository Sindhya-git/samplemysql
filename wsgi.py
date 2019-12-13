from flask import Flask
import MySQLdb
import os
application = Flask(__name__)

@application.route("/")
def hello_world():

  storage = Storage()
  score = storage.score()
  return score

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
    for x in range(cur.rowcount):
      print(x)
      print(row)
      return x
    
if __name__ == "__main__":
    application.run()
