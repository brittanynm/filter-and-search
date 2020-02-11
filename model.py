from flask_sqlalchemy import SQLAlchemy
import json


db = SQLAlchemy()


class Company(db.Model):

    __tablename__ = "companies"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250))
    customer = db.relationship("Customer")

    def __repr__(self):

        return f"<Company id={self.id} name={self.name}>"


class Customer(db.Model):

    __tablename__ = "customers"

    customer_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(20))
    last_name = db.Column(db.String(20))
    company_id = db.Column(db.Integer, db.ForeignKey("companies.id"))
    company = db.relationship("Company")

    def __repr__(self):

        return f"<Customer customer_id={self.customer_id}>"


def connect_to_db(app):
    app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///customers"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SQLALCHEMY_ECHO"] = False

    db.app = app
    db.init_app(app)


if __name__ == "__main__":

    from server import app

    connect_to_db(app)
    print("Connected to DB.")
