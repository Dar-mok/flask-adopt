"""Flask app for adopt app."""

import os

from flask import Flask, render_template, flash, redirect
from flask_debugtoolbar import DebugToolbarExtension

from models import connect_db, db, Pet
from forms import PetForm, EditPet

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
# call it pets
    all_pets = Pet.query.all()

    return render_template("homepage.html", pets=all_pets)


@app.route("/add", methods=["GET", "POST"])
def show_pet_form():
    """
    Accepts GET, POST
    GET: display the add a new pet form
    POST: process the add a new pet form
    """
    form = PetForm()

    if form.validate_on_submit():
        # access all of the data
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data

        new_pet = Pet(name=name, species=species,
                      photo_url=photo_url, age=age, notes=notes)
        db.session.add(new_pet)
        db.session.commit()

        flash('Pet Added')
        return redirect('/')

    return render_template("add_pet_form.html", form=form)


@app.route("/<int:pet_id>", methods=["GET", "POST"])
def show_pet_detail_and_edit_form(pet_id):
    """
    Accepts GET, Post

    GET: display current pet and show edit form
    POST: process edit form, redirect to home page

    """

    current_pet = Pet.query.get_or_404(pet_id)
    edit_form = EditPet(obj=current_pet)

    if edit_form.validate_on_submit():
        current_pet.photo_url = edit_form.photo_url.data
        current_pet.notes = edit_form.notes.data
        current_pet.available = edit_form.available.data

        db.session.commit()

        flash('Pet Edited')
        return redirect('/')

    return render_template("display_and_edit.html", form=edit_form, pet=current_pet)
