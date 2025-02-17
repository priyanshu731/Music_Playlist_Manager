from app import create_app
from models import db, Playlist, Song

def init_database():
    app = create_app()
    with app.app_context():
        # Drop all existing tables
        db.drop_all()
        
        # Create all tables
        db.create_all()
        
        # Create sample data (optional)
        sample_playlist = Playlist(
            name="My First Playlist",
            description="A collection of my favorite songs"
        )
        
        db.session.add(sample_playlist)
        db.session.commit()
        
        print("Database initialized successfully!")

if __name__ == "__main__":
    init_database()