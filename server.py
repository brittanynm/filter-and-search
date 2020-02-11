
from flask import Flask, render_template, request, flash, redirect, session, jsonify
from model import connect_to_db, Customer, Company

app = Flask(__name__)

app.secret_key = "ABC"



@app.route("/search", methods=["GET"])
def search():
    customer_name = request.args.get("query")
    q = Customer.query
    customers = q.filter(
        (Customer.first_name.ilike(f"%{customer_name}%"))
        | (Customer.last_name.ilike(f"%{customer_name}%"))
    ).all()
    return render_template("homepage.html", customers=customers)



@app.route("/live_search", methods = ["GET"])
def index():

    # customers = Customer.query.limit(200).all()

    # return render_template("homepage.html", customers=customers)



    '''Filter search results'''
    search = request.args.get("query")
    q = Customer.query
    customers = (
        q.filter(
            (Customer.first_name.ilike(f"%{search}%"))
            | (Customer.last_name.ilike(f"%{search}%"))
        )
        .limit(20)
        .all()
    )
    results = {}
    for customer in customers:
        results[customer.customer_id] = {
            "first_name": customer.first_name,
            "last_name": customer.last_name,
            "customer_id": customer.customer_id,
        }

    return jsonify(results)





if __name__ == "__main__":
    app.debug = False
    connect_to_db(app)
    app.run(host="0.0.0.0")