# __init__.py
from flask import Flask
app = Flask(__name__)
app.secret_key = "shhhhhh"

MyCustomDB = 'email_validation_with_db_schema'