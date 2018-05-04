from pymongo import MongoClient
from flask import Flask, render_template_string, render_template
app = Flask(__name__)

#DB Config


@app.route("/hello/<name>")
def hello(name):
    return render_template_string('<b>Hello {{ name }} </b>!', name=name)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/deployments")
def deployments():
    client = MongoClient("mongodb://localhost:27017")
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