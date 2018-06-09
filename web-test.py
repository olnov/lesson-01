from pymongo import MongoClient
from flask import Flask, render_template_string, render_template, jsonify, request
import json
from bson import json_util
app = Flask(__name__)

#DB Config

@app.route('/_add_numbers')
def add_numbers():
    a = request.args.get('a', 0, type=int)
    b = request.args.get('b', 0, type=int)
    return jsonify(result=a + b)

@app.route('/get-data')
def getdata():
    deployment = request.args.get('deployment', type=str)
    client = MongoClient("mongodb://192.168.1.201:27017")
    db = client.products
    collection=db.DeploymentType
    deptype = collection.find_one({"Name": deployment})
    return json.dumps(deptype, indent=4, default=json_util.default)

@app.route("/hello/<name>")
def hello(name):
    return render_template_string('<b>Hello {{ name }} </b>!', name=name)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/deployments")
def deployments():
    client = MongoClient("mongodb://192.168.1.201:27017")
    db=client.products
    collection=db.DeploymentType
    deptypes = list(collection.find())
    return render_template('deployments.html', deptypes=deptypes)

@app.route("/services")
def services():
    return render_template('services.html')

@app.route("/components")
def components():
    return render_template('components.html')


if __name__ == "__main__":
    app.run(host='localhost',port=8080)