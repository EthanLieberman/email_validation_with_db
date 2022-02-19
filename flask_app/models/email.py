from pickle import FALSE
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import MyCustomDB
from flask import flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class Email:                         # singular instance of...
    def __init__(self,data):
        self.id = data['id']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']



    @staticmethod
    def validate_email(data):
        is_valid = True

        if not EMAIL_REGEX.match(data['email']): 
            flash("Invalid email address!")
            is_valid = False

        for row in Email.get_all():
            if data['email'] in row.email:
                print("row checking email")
                flash("email already in use")
                is_valid = False
            

        return is_valid



    @classmethod
    def save(cls, data):
        query = "INSERT INTO emails ( email , created_at , updated_at) VALUES ( %(email)s , NOW() , NOW() );"
        return connectToMySQL(MyCustomDB).query_db( query, data )


    @classmethod
    def get_all(cls):
        query = "SELECT * FROM emails;"
    # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL(MyCustomDB).query_db(query)
    # Create an empty list to append our instances of users
        my_emails = []
    # Iterate over the db results and create instances of users with cls.
        for row in results:
            my_emails.append( cls(row) )
        print('from the get all method')
        return my_emails


    @classmethod
    def delete_email(cls, data):
        print("delete is running")
        query = "DELETE FROM emails WHERE id = %(id)s"
        return connectToMySQL(MyCustomDB).query_db( query, data )