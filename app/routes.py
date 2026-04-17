from flask import Blueprint, render_template
from flask import current_app as app
from app.models import Cafe, db
from app.extension import db  # ← same here
from app.forms import CafeForm
from flask import redirect, url_for

bp = Blueprint('main', __name__)

# [START] Flask Routes
@bp.route('/')
def home():
    cafes = db.session.execute(db.select(Cafe)).scalars().all() # python data objects
    return render_template('index.html', cafes=cafes)


@bp.route('/about')
def about():
    return render_template('about.html')

@bp.route('/edit/<int:id>', methods=["GET", "POST"])
def edit(id):
    cafe = db.get_or_404(Cafe, id)
    
    # Passing obj=cafe tells WTForms to grab the data from your db object
    # and preload it into the form fields!
    form = CafeForm(obj=cafe)
    
    if form.validate_on_submit():
        # Using populate_obj grabs all the submitted form data and saves it back
        # into the 'cafe' object, making saving incredibly easy.
        form.populate_obj(cafe)
        db.session.commit()
        return redirect(url_for('main.home'))
        
    return render_template('edit.html', cafe=cafe, form=form)

@bp.route('/add', methods=["GET", "POST"])
def add():
    form = CafeForm()
    if form.validate_on_submit():
        new_cafe = Cafe()
        form.populate_obj(new_cafe)
        db.session.add(new_cafe)
        db.session.commit()
        return redirect(url_for('main.home'))
    return render_template('add.html', form=form)

@bp.route('/delete/<int:id>', methods=["POST", "GET"])
def delete(id):
    cafe = db.get_or_404(Cafe, id)
    db.session.delete(cafe)
    db.session.commit()
    return redirect(url_for('main.home'))
