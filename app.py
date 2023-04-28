"""Flask app for adopt app."""

import os

from flask import Flask, render_template, flash
from flask_debugtoolbar import DebugToolbarExtension

from models import connect_db, db, Pet

app = Flask(__name__)

app.config['SECRET_KEY'] = "secret"

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    "DATABASE_URL", "postgresql:///adopt")

connect_db(app)

# Having the Debug Toolbar show redirects explicitly is often useful;
# however, if you want to turn it off, you can uncomment this line:
#
# app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

toolbar = DebugToolbarExtension(app)

@app.get("/")
def show_homepage():
    """Grab all pets from DB, pass pets to the render tamplate and diplay """

    all_pets = Pet.query.all()

    return render_template("homepage.html", pets=all_pets)

@app.route("/add", methods=["GET", "POST"])
def show_pet_form():
    """render the pet intake form"""
    form = Pet()

    if form.validate_on_submit():
        #probs add data from form to DB and then redirect user
        redirect

    else:
        return render_template("add_pet_form.html", form=form)




