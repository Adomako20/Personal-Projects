from flask import Blueprint, render_template, request, redirect, url_for, flash
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import date

# date variable
current_date = date.today()


# creating blueprint app
add_bp = Blueprint("add", __name__)


# routes
@add_bp.route("/add")
def additem():
    return render_template("add.html")


# spectacles routes
@add_bp.route("/add_spectacle")
def add_spec():
    
    return render_template("add/add_spectacles.html")


@add_bp.route("/added_spectacle", methods=["GET", "POST"])
def added_spec():
    if request.method == "POST":
        gender = request.form.get("gender")
        price = request.form.get("price")
        colour = request.form.get("colour")
        strength = request.form.get("strength")
        
        if gender and price and colour and strength:
            
            # inserting data input into the database
            connection = sqlite3.connect("users.db")
            cursor = connection.cursor()
            
            cursor.execute("""
                   INSERT INTO spectacles (GENDER, PRICE, COLOUR, STRENGTH, DATE_CREATED) 
                   VALUES (?, ?, ?, ?, ?)
                   """, (gender, price, colour, strength, current_date))
            
            connection.commit()
            connection.close()
            
            # flashing a message
            flash("Spectacle added sucessfully!", "sucess")
            return render_template("add/add_spectacles.html")
        
    
    # flashing and error message
    flash("Fill all field!", "error")
    return render_template("add/add_spectacles.html")
    
    


# lense case routes
@add_bp.route("/add_lense_case", methods = ["POST", "GET"])
def add_case():
    
    if request.method == "POST":
        case_price = request.form.get("price")
        case_colour = request.form.get("colour")
            
        if case_price and case_colour:
            # inserting into database
            connection = sqlite3.connect("users.db")
            cursor = connection.cursor()
                
            cursor.execute("INSERT INTO lense_case (PRICE, COLOUR, DATE_CREATED) VALUES (?, ?, ?)", (case_price, case_colour, current_date))
            connection.commit()
            connection.close()
            
            flash("Case added sucessfully!", "sucess")
            return render_template("add/add_lense_case.html")
        
        else:
            flash("Fill all filed!", "error")
            return render_template("add/add_lense_case.html")
            
    return render_template("add/add_lense_case.html")


# user routes
@add_bp.route("/users")
def users():
    return render_template("add/users.html")


# new user route
@add_bp.route("/new_user")
def new_user():
    
    return render_template("add/user_folder/new_user.html")

#receiving data from new users page
@add_bp.route("/create_user", methods = ["POST", "GET"])
def create_user():
    
    if request.method == "POST":
        user_name = request.form.get("user_name")
        first_password = request.form.get("first_password")
        confirm_password = request.form.get("second_password")
        
        # harshing password
        if first_password == confirm_password:
            harshed_password = generate_password_hash(first_password)
            
            # connecting to database
            connection = sqlite3.connect("users.db")
            cursor = connection.cursor()
        
        # creating a table for users database
            cursor.execute("""
                        INSERT INTO users (USERNAME, PASSWORD, DATE_CREATED) VALUES (?, ?, ?)""", (user_name, harshed_password, current_date))
            
            connection.commit()
            connection.close()
            
            flash("harsh generated", "sucess")
            return redirect(url_for("add.new_user"))
        
        else:
            flash("Wrong inputs. Try again!", "error")
            return render_template("add/user_folder/new_user.html")
