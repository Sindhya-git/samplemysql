from flask import Flask
import MySQLdb
import os
application = Flask(__name__)

@application.route("/")
def hello_world():

  storage = Storage()
  score = storage.score()
  print("score is ",score)
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
    row = cur.fetchone()
    db_out = {}
    print("Total number of row in PRODUCT_SKU is: ", cur.rowcount)
    print("type of row is :", type(row))
    print("Item  = ", row, )
    for i in range(0,cur.rowcount):
      print("row i",row[i])
      db_out["row_" + i] = row[i]
      print(db_out)
      print(db_out["row_1"])   #specific output -- pass dict keyname
    print("type of db_out is ", type(db_out))
    return db_out
    #print(row[0],"  ", row[1])
    #return row[0], row[1], row[2], row[3], row[4]
    
if __name__ == "__main__":
    application.run()
