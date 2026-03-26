from flask import Blueprint, render_template, request, flash
import sqlite3

# creating a blueprint
remove_item = Blueprint("remove_item", __name__)


# creating routes
@remove_item.route("/remove")
def remove():
    return render_template("remove.html")


# remove spectacles route
@remove_item.route("/remove_spectacle", methods=["POST", "GET"])
def remove_spec():
    if request.method == "POST":
        del_spec = request.form.get("id")
        
        # fetching from the database
        connection = sqlite3.connect("users.db")
        cursor = connection.cursor()
        cursor.execute("DELETE FROM spectacles WHERE SPECTACLE_ID = ?;", (del_spec,))
        connection.commit()
        connection.close()
    
        flash("Spectacle Removed Sucessfully!", "sucess")
        return render_template("remove/remove_spectacles.html")
    
    return render_template("remove/remove_spectacles.html")


# remove lense case routes
@remove_item.route("/remove_lense_case", methods=["POST", "GET"])
def remove_case():
    if request.method == "POST":
        del_case = request.form.get("id")
        
        # fetching from the database
        connection = sqlite3.connect("users.db")
        cursor = connection.cursor()
        cursor.execute("DELETE FROM lense_case WHERE CASE_ID = ?;", (del_case,))
        connection.commit()
        connection.close()
    
        flash("Case Removed Sucessfully!", "sucess")
        return render_template("remove/remove_lense_case.html")
    
    return render_template("remove/remove_lense_case.html")