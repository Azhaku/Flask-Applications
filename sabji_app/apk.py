import os
from flask import Flask,render_template,request
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
## step - 1: set up flask
app=Flask(__name__)

####################  setp - 1.2 SQL Alchemy setup  #####################

basedir = os.path.abspath(os.path.dirname(__file__))   ###abspath means whole directory from c:...
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')  ##were creating a database for this app
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

## step - 1.3: pass application into sqlalchemy

db =SQLAlchemy(app)   
migrate = Migrate(app, db)   ##It will connect the database to frontend

#############################################################
## step -2: create a model in Flask app
## a) create a model class
## b) inherit from db model
## c) provide table name
## d) add columns
## e) create __init__ && __repr__

#########################  Create a Model  ###################################

class Sabji(db.Model):
    __tablename__ = 'sabjis'
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.Text)
    mrp = db.Column(db.Integer)

    def __init__(self, name, mrp):
        self.name = name
        self.mrp = mrp
    def __repr__(self):
        return "Sabji Name = {} and MRP = {}".format(self.name,self.mrp)

## 3 command for first time run
## a) flask db init
## b) flask db migrate -m "message"
## c) flask db upgrade
##############################################3


@app.route('/',)
def index():
    return render_template("index.html")

@app.route("/add" , methods=["GET","POST"])
def add():
    if request.method == "POST":
        name = request.form.get("in_1")
        mrp = request.form.get("in_2")
        new_sabji = Sabji(name, mrp)   ##create a object
        db.session.add(new_sabji)   ## add the values into db
        db.session.commit()    ## save the db

    return render_template('add.html')

@app.route("/search")
def search():
    name = request.args.get("in_1")
    sabji = Sabji.query.filter_by(name=name).first()
    return render_template('search.html',sabji=sabji)

@app.route("/display")
def display():
    sabjis = Sabji.query.all()
    return render_template('display.html', sabjis = sabjis)


if __name__ == '__main__':
    app.run(debug = True)
