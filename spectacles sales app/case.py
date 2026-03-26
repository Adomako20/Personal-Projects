from flask import Blueprint, render_template, request, flash
import sqlite3
from datetime import date

# date variable
current_date = date.today()

case = Blueprint("case", __name__)


@case.route("/lense_case", methods = ["POST", "GET"])
def lense_case():
    
    if request.method == "GET":
    # fetching data from database
        connection = sqlite3.connect("users.db")
        cursor = connection.cursor()
                
        cursor.execute("SELECT * FROM lense_case;")
        data = cursor.fetchall()
    
    # counting the number of spectacles
        cursor.execute("SELECT COUNT(*) FROM lense_case;")
        case_all = cursor.fetchone()
        
        
        return render_template("lense_case.html", case_all=case_all, data=data)
        
    elif request.method == "POST":
        seached_input = request.form.get("search")
        
        # fetching spectacles from database based on searched
        connection = sqlite3.connect("users.db")
        cursor = connection.cursor()
                
        cursor.execute("SELECT * FROM lense_case WHERE CASE_ID = ?;", (seached_input,))
        data = cursor.fetchone()
        data = [(data)]
        
        # counting the number of spectacles
        cursor.execute("SELECT COUNT(*) FROM spectacles;")
        case_all = cursor.fetchone()
  
        return render_template("lense_case.html", case_all=case_all, data=data)
