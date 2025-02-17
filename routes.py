
from flask import Blueprint, render_template, request, redirect, url_for, flash
from models import db, Playlist, Song
from forms import PlaylistForm, SongForm
import os
from werkzeug.utils import secure_filename
from datetime import datetime

main = Blueprint('main', __name__)

@main.route('/')
def index():
    playlists = Playlist.query.all()
    return render_template('index.html', playlists=playlists)

@main.route('/playlist/new', methods=['GET', 'POST'])
def create_playlist():
    form = PlaylistForm()
    if form.validate_on_submit():
        playlist = Playlist(
            name=form.name.data,
            description=form.description.data
        )
        db.session.add(playlist)
        db.session.commit()
        flash('Playlist created successfully!', 'success')
        return redirect(url_for('main.index'))
    return render_template('playlist.html', form=form, title='New Playlist')

@main.route('/playlist/<int:playlist_id>')
def view_playlist(playlist_id):
    playlist = Playlist.query.get_or_404(playlist_id)
    return render_template('playlist.html', playlist=playlist)

@main.route('/song/new/<int:playlist_id>', methods=['GET', 'POST'])
def upload_song(playlist_id):
    form = SongForm()
    if form.validate_on_submit():
        file = form.file.data
        filename = secure_filename(file.filename)
        file_path = os.path.join('uploads', filename)
        file.save(os.path.join('static', file_path))
        
        song = Song(
            title=form.title.data,
            artist=form.artist.data,
            file_path=file_path,
            playlist_id=playlist_id
        )
        db.session.add(song)
        db.session.commit()
        flash('Song uploaded successfully!', 'success')
        return redirect(url_for('main.view_playlist', playlist_id=playlist_id))
    return render_template('song.html', form=form, title='Upload Song')