from flask import Flask, render_template
from flask_pymongo import PyMongo
import KEYS
import random

app = Flask(__name__, instance_relative_config=True)
app.config["MONGO_URI"] = KEYS.MONGO_URI
mongo = PyMongo(app)

@app.route("/")
def index():
    listRolls = mongo.db.cluster0.xd6x35z.mongodb.net.find({ },{'_id': False}) 
    return render_template("index.html", listOfResults = list(listRolls))

@app.route("/roll/", methods=['POST'])
def rollDice():
    result = random.randint(1,6)
    mongo.db.cluster0.xd6x35z.mongodb.net.insert_one({"number": result})
    listRolls = mongo.db.cluster0.xd6x35z.mongodb.net.find({ },{'_id': False}) 
    return render_template("index.html",result = result, listOfResults = list(listRolls))

@app.route("/delete/", methods=['GET'])
def deleteListOfResults():
    listRolls = mongo.db.cluster0.xd6x35z.mongodb.net.find({ },{'_id': False}) 
    mongo.db.cluster0.xd6x35z.mongodb.net.drop()
    return render_template("index.html" ,listOfResults = list(listRolls))

if __name__ == '__main__':
    app.run()