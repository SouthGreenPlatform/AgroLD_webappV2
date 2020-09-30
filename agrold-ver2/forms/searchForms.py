from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

from wtforms.validators import DataRequired
class SearchForm(FlaskForm):
    search = StringField('search', [DataRequired()])
    submit = SubmitField('Search', render_kw={'class': 'btn btn-success btn-block'})
