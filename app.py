from flask import Flask, render_template, request, send_file
from flask_sqlalchemy import SQLAlchemy
from distance import getDistance
from exportCsv import createCsv
from calculations import calculateExpense, calculateMileage
from configparser import ConfigParser

config = ConfigParser()
config.read('config.ini')

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']= config['keys']['db_config']
db=SQLAlchemy(app)

class Data(db.Model):
    __tablename__="treatmentInfo"
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String)
    address=db.Column(db.String)
    treatment=db.Column(db.String)
    place=db.Column(db.String)
    sessions=db.Column(db.Integer)
    cost=db.Column(db.Float)
    mileage=db.Column(db.Float)
    expense=db.Column(db.Float)

    def __init__(self, name, address, treatment, place, sessions, cost, mileage, expense):
        self.name=name
        self.address=address
        self.treatment=treatment
        self.place=place
        self.sessions=sessions
        self.cost=cost
        self.mileage=mileage
        self.expense=expense

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/results", methods=['POST'])
def results():
    if request.method=="POST":
        name=request.form["form_name"]
        address=request.form["form_address"]
        treatment=request.form["form_treatment"]
        place=request.form["form_place"]
        sessions=request.form["form_sessions"]
        cost=request.form["form_costs"]
        mileage=calculateMileage(getDistance(address, place))
        expense=calculateExpense(sessions, cost, getDistance(address, place))

        data=Data(name, address, treatment, place, sessions, cost, mileage, expense)
        db.session.add(data)
        db.session.commit()
        createCsv(Data.query.all())
        return render_template("results.html", result=expense)

@app.route('/download', methods=["POST"])
def fileDownload():
    try: 
      return send_file('treatments.csv',
                     attachment_filename='Treatments.csv',
                     as_attachment=True)
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    app.run(debug=True)
