# New Relic Take Home Exercise: Filter and Search


A full stack app that allows you to filter a list of customers in two ways: Search by customer's first or last name via a text input field and filter by a customer's company via a dropdown. Includes test coverage for the BE.

## Setup

Before you begin the setup and installation process below, you'll need to have
the following installed:

- Python 3.0 or above
- PostgreSQL


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
 


