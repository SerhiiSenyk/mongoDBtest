from flask import  Flask ,render_template ,url_for
from pymongo import MongoClient

import pymongo
app = Flask(__name__)

connect = pymongo.MongoClient('localhost',27017)
db = connect.mymongodb
collection = db.events

#def writeInDB() :
    #events = mongo.db.collection
    #events = {"self" : "Serhii", "checkpoint_id" : "123", "tag": "run" , "time": "12:00"}
    #{"self" : " Andrii", "checkpoint_id" : "321", "tag": "stop" , "time": "18:00"}
    #collection.save(events)
@app.route("/")
def read() :
     list = []
     for events in collection.find() :
        list.append(events)
     return render_template("table.html",events = list)

if __name__ == '__main__':
   app.run(debug = True)
