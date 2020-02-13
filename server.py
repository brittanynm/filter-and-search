from flask import Flask, render_template, request, flash, redirect, session, jsonify
from model import connect_to_db, Customer, Company

app = Flask(__name__)

app.secret_key = "ABC"


@app.route("/customers", methods=["GET"])
def search():
    customer_name = request.args.get("name")
    q = Customer.query
    customers = q.filter(
        (Customer.first_name.ilike(f"%{customer_name}%"))
        | (Customer.last_name.ilike(f"%{customer_name}%"))
    ).all()
    return render_template("homepage.html", customers=customers)


@app.route("/live_search", methods=["GET"])
def index():
    """Filter search results"""
    name = request.args.get("name")
    company = request.args.get("company")

    q = Customer.query

    if name:
        q = q.filter(
            (Customer.first_name.ilike(f"%{name}%"))
            | (Customer.last_name.ilike(f"%{name}%"))
        )
    if company:
        q = q.filter((Customer.company_id == company))

    customers = q.limit(20).all()

    results = {}
    for customer in customers:
        results[customer.customer_id] = {
            "first_name": customer.first_name,
            "last_name": customer.last_name,
            "company_id": customer.company_id,
            "company_name": customer.company.name,
        }

    return jsonify(results)


@app.route("/companies", methods=["GET"])
def display_companies():

    companies = Company.query.all()

    results = {}
    for company in companies:
        results[company.id] = company.name

    return jsonify(results)


if __name__ == "__main__":
    app.debug = False
    connect_to_db(app)
    app.run(host="0.0.0.0")
