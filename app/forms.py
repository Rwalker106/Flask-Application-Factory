from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField, BooleanField
from wtforms.validators import DataRequired, URL

class CafeForm(FlaskForm):
    name = StringField('Cafe Name', validators=[DataRequired()])
    map_url = URLField('Map URL', validators=[DataRequired(), URL()])
    img_url = URLField('Image URL', validators=[DataRequired(), URL()])
    location = StringField('Location', validators=[DataRequired()])
    has_sockets = BooleanField('Has Sockets?')
    has_toilet = BooleanField('Has Toilet?')
    has_wifi = BooleanField('Has WiFi?')
    can_take_calls = BooleanField('Can Take Calls?')
    seats = StringField('Seats', validators=[DataRequired()])
    coffee_price = StringField('Coffee Price', validators=[DataRequired()])
    submit = SubmitField('Submit')
