# New Relic Take Home Exercise: Filter and Search


Full stack app that allows you to filter a list of customers in two of three ways: Search by customer's first or last name via a text input field, Filter by a customer's company name via a dropdown, or sort by a customer's first name, last name, or company with both ascending and descending order. The system persists the text, company name, and sort in the URL as a query param. Include test coverage for both UI and BE

## Setup

Before you begin the setup and installation process below, you'll need to have
the following installed:

- Python 3.0 or above
- PostgreSQL 11


### Install Python dependencies

Create a virtual environment

```
python3 -m venv env

# Alternatively, if you have virtualenv installed
virtualenv env
```

Activate the environment and install dependencies from `requirements.txt`

```
source env/bin/activate
pip3 install -r requirements
```

### Initialize the database

Create a PostgreSQL database called `customers`

```
createdb customers
```

Run this command to create tables and test data

```
python3 model.py 
```
```
python3 seed.py
```

### Run Flask server

Now you can run the server with

```
python3 server.py
```

The site will be accessible at http://localhost:5000.

## File structure

static/
  Contains static assets. 
templates/
  Currently only has one HTML file called
  `homepage.html`
model.py
  Database schema and ORM classes written with SQLAlchemy
server.py
  Flask routes

## Flask routes

### `GET` /customers

Display the homepage




## Tech Stack
__Backend__: Python, Flask, PostgreSQL, SQLAlchemy <br/>
__Frontend__: Javascript, React, HTML, CSS <br/>


## Assumptions
 1) Assumed each customer could only have one company
 


