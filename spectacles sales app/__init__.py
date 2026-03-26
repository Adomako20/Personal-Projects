from flask import Flask, redirect, render_template, session, url_for
from auth import auth as auth_bp
from spectacles import spectacle
from database import database as database_bp
from add import add_bp
from case import case
from remove import remove_item


# creating flask app
app = Flask(__name__)
app.secret_key = "mylensaleapp"


# registering blueprints
app.register_blueprint(auth_bp, url_prefix="/auth")
app.register_blueprint(database_bp)
app.register_blueprint(spectacle, url_prefix="/cat")
app.register_blueprint(add_bp, url_prefix="/additems")
app.register_blueprint(case)
app.register_blueprint(remove_item, url_prefix="/removeitems")


@app.route("/")
def index():
    
    if not "user" in session:
        return redirect(url_for("auth.login"))
    
    return render_template("index.html")
 
 
if __name__ == "__main__":
     app.run(debug=True)