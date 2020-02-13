# New Relic Take Home Exercise: Filter and Search


A full stack app that allows you to filter a list of customers in two ways: Search by customer's first or last name via a text input field and filter by a customer's company via a dropdown. Includes test coverage for the BE.

## Setup

Before you begin the setup and installation process below, you'll need to have
the following installed:

- Python 3.0 or above
- PostgreSQL

To run this app on your own machine:


1. Create a virtual environment

```python3 -m venv env

# Alternatively, if you have virtualenv installed
virtualenv env```

2. Activate the environment and install dependencies from `requirements.txt`

```
source env/bin/activate
pip3 install -r requirements
```

3. Create a PostgreSQL database called `customers`

```
createdb customers
```

4. Run these commands to create tables and test data

```
python3 model.py 
```
```
python3 seed.py
```

5. Now you can run the server with

```
python3 server.py
```

6. The site will be accessible at http://localhost:5000.



## Technologies
__Backend__: Python, Flask, PostgreSQL, SQLAlchemy <br/>
__Frontend__: Javascript, React, HTML <br/>


## Assumptions
- Assumed each customer could only have one company
 
 ## If I had more time...
 1) I would learn how to use React Router to include the filters in the URL parameters
 2) Learn and write front end testing
 3) Added some styling


