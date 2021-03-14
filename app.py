from flask import Flask, request, render_template, redirect, flash
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import AddPetForm, EditPetForm

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adoption_agency'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "notverysecret"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)

db.create_all()

@app.route('/')
def list_pets():
    """Shows list of pets"""
    pets = Pet.query.order_by(Pet.id).all()
    return render_template('petslist.html', pets=pets)

@app.route('/add', methods=["GET", "POST"])
def add_pet():
    """show add pet form (GET) or handles pet form submissions (POST)"""
    form = AddPetForm()
    
    if form.validate_on_submit():
        name = form.pet_name.data
        species = form.species.data
        photo = form.photo_url.data
        age = form.age.data
        note = form.note.data

        new_pet = Pet(name=name, species=species, photo_url=photo, age=age, notes=note)

        db.session.add(new_pet)
        db.session.commit()
        return redirect('/')
    else:
        return render_template('newpetform.html', form=form)
    
@app.route('/<int:id>', methods=["GET", "POST"])
def pet_info_edit(id):
    """show pet information and edit pet form"""
    pet = Pet.query.get_or_404(id)
    form = EditPetForm(obj=pet)

    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.notes = form.note.data
        pet.available = form.available.data
        db.session.commit()
        flash(f"{pet.name} updated!")
        return redirect(f"/{pet.id}")

    else:
        return render_template("petdetails.html", pet=pet, form=form)


