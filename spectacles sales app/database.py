from flask import Blueprint
import sqlite3
from werkzeug.security import generate_password_hash
from datetime import date


# variables
current_date = date.today()


# creating a database blueprint
database = Blueprint("database", __name__)


# creating a database
def create_database():
    connection = sqlite3.connect("users.db")
    cursor = connection.cursor()
    
    # creating a table for users database
    cursor.execute("""
                   CREATE TABLE IF NOT EXISTS users (
                       USER_ID INTEGER PRIMARY KEY AUTOINCREMENT,
                       USERNAME TEXT NOT NULL,
                       PASSWORD TEXT NOT NULL,
                       DATE_CREATED TEXT NOT NULL
                   );
                   """)
    connection.commit()
    connection.close()

create_database()


# creating an admin user by default
def create_admin():
    username = "admin"
    password = "admin"
    
    
    # harsing password
    harshed_password = generate_password_hash(password)
    
    
    # checking for users
    connection = sqlite3.connect("users.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users where USERNAME = ?", (username,))
    data = cursor.fetchone()
    
    
    # inserting an admin user
    if not data:
        
        # inserting into a database
        connection = sqlite3.connect("users.db")
        cursor = connection.cursor()
        
        # creating a table for users database
        cursor.execute("""
                    INSERT INTO users (USERNAME, PASSWORD, DATE_CREATED) VALUES (?, ?, ?)""", (username, harshed_password, current_date))
        
        connection.commit()
        connection.close()

create_admin()


# creating spectacles table
def create_spec_table():
    connection = sqlite3.connect("users.db")
    cursor = connection.cursor()
    
    # creating a table for users database
    cursor.execute("""
                   CREATE TABLE IF NOT EXISTS spectacles (
                       SPECTACLE_ID INTEGER PRIMARY KEY AUTOINCREMENT,
                       GENDER TEXT NOT NULL,
                       PRICE REAL NOT NULL,
                       COLOUR TEXT NOT NULL,
                       STRENGTH REAL NOT NULL,
                       DATE_CREATED TEXT NOT NULL
                   );
                   """)
    connection.commit()
    connection.close()

create_spec_table()


# working on lense case db
def create_lense_table():
    connection = sqlite3.connect("users.db")
    cursor = connection.cursor()
    # creating a table for users database
    cursor.execute("""
                   CREATE TABLE IF NOT EXISTS lense_case (
                       CASE_ID INTEGER PRIMARY KEY AUTOINCREMENT,
                       PRICE REAL NOT NULL,
                       COLOUR TEXT NOT NULL,
                       DATE_CREATED TEXT NOT NULL
                   );
                   """)
    connection.commit()
    connection.close()

create_lense_table()

