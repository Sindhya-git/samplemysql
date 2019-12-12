import os
import flask
import MySQLdb

application = flask.Flask(__name__)
application.debug = True

@application.route('/')
def hello_world():
  print("start hello")
  storage = Storage()
  score = storage.score()
  print("end hello")
  return "Hello PRODUCT DB !" % score

class Storage():
  def __init__(self):
    self.db = MySQLdb.connect(
      user   = os.getenv('MYSQL_USER', "xxuser"),
      passwd = os.getenv('MYSQL_PASSWORD', "welcome1")
      db     = os.getenv('MYSQL_DATABASE',"sampledb"),
      host   = os.getenv('MYSQL_SERVICE_HOST', "custom-mysql.gamification.svc.cluster.local"),
      port   = int(os.getenv('MYSQL_SERVICE_PORT',"3306"))
    )
    print(" init successfull")
    cur = self.db.cursor()
    
  def score(self):
    cur = self.db.cursor()
    cur.execute("SELECT * FROM XXIBM_PRODUCT_CATALOG")
                   print(" inside fetch")
    row = cur.fetchone()
    return row[0]

if __name__ == "__main__":
  application.run(host='0.0.0.0', port=3000)
