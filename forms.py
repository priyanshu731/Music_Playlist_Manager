from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, FileField, SubmitField
from wtforms.validators import DataRequired, Length

class PlaylistForm(FlaskForm):
    name = StringField('Playlist Name', validators=[DataRequired(), Length(min=1, max=100)])
    description = TextAreaField('Description', validators=[Length(max=200)])
    submit = SubmitField('Create Playlist')

class SongForm(FlaskForm):
    title = StringField('Song Title', validators=[DataRequired(), Length(min=1, max=100)])
    artist = StringField('Artist', validators=[Length(max=100)])
    file = FileField('Audio File', validators=[DataRequired()])
    submit = SubmitField('Upload Song')