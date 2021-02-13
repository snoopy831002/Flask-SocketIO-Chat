from flask_wtf import FlaskForm
from wtforms.fields import StringField, SubmitField
from wtforms.validators import Required

class LoginForm(FlaskForm):
    """Accepts a nickname and a room."""
    name = StringField('', validators=[Required()])
    room = StringField('')
    submit = SubmitField('')
    
