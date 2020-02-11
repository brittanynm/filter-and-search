import csv
from model import Customer, Company, connect_to_db, db
from server import app


def load_customers():
    print("Customers")

    for row in open("customers.csv", encoding="cp1252"):
        row = row.rstrip()
        customer_id, first_name, last_name, company_id = row.split(",")

        customer = Customer(
            customer_id=customer_id,
            first_name=first_name,
            last_name=last_name,
            company_id=company_id,
        )

        db.session.add(customer)

    db.session.commit()


def load_companies():
    print("Companies")

    for row in open("companies.csv", encoding="cp1252"):
        row = row.rstrip()
        id, name = row.split(",")

        company = Company(id=id, name=name)

        db.session.add(company)

    db.session.commit()


if __name__ == "__main__":
    connect_to_db(app)
    db.create_all()
    load_companies()
    load_customers()
