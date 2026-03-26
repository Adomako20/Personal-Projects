from flask import Flask, url_for, redirect, render_template, request, session, Blueprint, flash
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3


# creating a blueprint
auth = Blueprint("auth", __name__)


@auth.route("/login", methods=["POST", "GET"])
def login():
    return render_template("login.html")


@auth.route("/loggedin", methods=["GET", "POST"])
def loggedIn():
    username = request.form.get("username")
    user_password = request.form.get("password")
    
    # checking the username in the database
    connection = sqlite3.connect("users.db")
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users where USERNAME = ?", (username,))
    data = cursor.fetchone()
    
    
    if data:
        if username == data["USERNAME"] and check_password_hash(data["PASSWORD"], user_password):
            session["user"] = username
            return redirect(url_for("index"))
        
        
    flash("Wrong input. Try again", "error")
    
    
    return redirect(url_for("auth.login"))


# logout route
@auth.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("auth.login"))