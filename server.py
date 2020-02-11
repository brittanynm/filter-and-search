
from flask import Flask, render_template, request, flash, redirect, session, jsonify
from model import connect_to_db, Customer, Company

app = Flask(__name__)

app.secret_key = "ABC"


@app.route("/", methods = ["GET"])
def index():

    customers = Customer.query.limit(200).all()

    return render_template("homepage.html", customers=customers)
