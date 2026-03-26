from flask import Blueprint, render_template, url_for, redirect, request, session
import sqlite3


spectacle = Blueprint("spectacle", __name__)

@spectacle.route("/spectacles", methods = ["GET", "POST"])
def spec():
    if request.method == "GET":
    # fetching data from database
        connection = sqlite3.connect("users.db")
        cursor = connection.cursor()
                
        cursor.execute("SELECT * FROM spectacles;")
        data = cursor.fetchall()
        
        # counting the number of spectacles
        cursor.execute("SELECT COUNT(*) FROM spectacles;")
        spec_all = cursor.fetchone()
    
        return render_template("spectacles.html", data=data, spec_all = spec_all)
    
    elif request.method == "POST":
        seached_input = request.form.get("search")
        
        # fetching spectacles from database based on searched
        connection = sqlite3.connect("users.db")
        cursor = connection.cursor()
                
        cursor.execute("SELECT * FROM spectacles WHERE SPECTACLE_ID = ?;", (seached_input,))
        data = cursor.fetchone()
        data = [(data)]
        
        # counting the number of spectacles
        cursor.execute("SELECT COUNT(*) FROM spectacles;")
        spec_all = cursor.fetchone()
        
        return render_template("spectacles.html", data=data, spec_all = spec_all)


    
    