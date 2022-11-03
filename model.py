"""Models for Giggogo app."""

from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    """Table for user information."""

    __tablename__ = "users"

    user_id = db.Column(db.Integer, autoincrement = True, primary_key = True)
    first_name = db.Column(db.String, nullable = False)
    last_name = db.Column(db.String, nullable = False)
    email = db.Column(db.String, unique = True, nullable = False)
    password = db.Column(db.String, nullable = False)
    band_id = db.Column(db.Integer, db.ForeignKey("bands.band_id"))
    venue_id = db.Column(db.Integer, db.ForeignKey("venues.venue_id"))
    profile_photo = db.Column(db.String, unique = False, nullable = True)

    #foreign keys used by "users" table
    bands = db.relationship("Band", back_populates = "users")
    venue = db.relationship("Venue", back_populates = "users")

    def __repr__(self):
        return f'<User user_id = { self.user_id } band_id = { self.band_id } venue_id = { self.venue_id } email = { self.email }>'

class Genre(db.Model):
    """Table for possible genres."""

    __tablename__ = "genres"

    genre_id = db.Column(db.Integer, autoincrement = True, primary_key = True)
    genre_name = db.Column(db.String, nullable = True)

    #tables using "genres" table data as foreign key
    band_genres = db.relationship("Band_Genre", back_populates = "genre")
    venue_genres = db.relationship("Venue_Genre", back_populates = "genre")

    def __repr__(self):
        return f'<Genre genre_id = { self.genre_id } genre_name = { self.genre_name }>'

class Gig(db.Model):
    """Table for scheduled gig details."""

    __tablename__ = "gigs"

    gig_id = db.Column(db.Integer, autoincrement = True, primary_key = True)
    venue_id = db.Column(db.Integer, db.ForeignKey("venues.venue_id"))
    band_id = db.Column(db.Integer, db.ForeignKey("bands.band_id"))
    gig_date = db.Column(db.DateTime, unique = True, nullable = False)
    final_payrate = db.Column(db.Integer, nullable = False)
    gig_complete = db.Column(db.Boolean, nullable = False)
    gig_paid = db.Column(db.Boolean, nullable = False)

    #foreign keys used by "gigs" table
    venue = db.relationship("Venue", back_populates = "gigs")
    bands = db.relationship("Band", back_populates = "gigs")

    def __repr__(self):
        return f'<Gig gig_id = { self.gig_id } venue_id = { self.venue_id } band_id = { self.band_id } gig_date = { self.gig_date }>'

####### Band information. #######

class Band(db.Model):
    """Table for band information."""

    __tablename__ = "bands"

    band_id = db.Column(db.Integer, autoincrement = True, primary_key = True)
    band_name = db.Column(db.String, unique = True, nullable = False)
    band_phone = db.Column(db.String, unique = False, nullable = False)
    band_payrate = db.Column(db.Integer, nullable = True)
    band_logo = db.Column(db.Text, nullable = True)
    band_photo = db.Column(db.Text, nullable = True)
    band_video = db.Column(db.Text, nullable = True)

    #tables using "bands" table data as foreign key
    gigs = db.relationship("Gig", back_populates = "bands")
    users = db.relationship("User", back_populates = "bands")
    band_genres = db.relationship("Band_Genre", back_populates = "bands")

    def __repr__(self):
        return f'<Band band_id = { self.band_id } band_name = { self.band_name }>'

class Band_Genre(db.Model):
    """Table for band genres."""

    __tablename__ = "band_genres"

    band_genre_id = db.Column(db.Integer, autoincrement = True, primary_key = True)
    band_id = db.Column(db.Integer, db.ForeignKey("bands.band_id"))
    genre_id = db.Column(db.Integer, db.ForeignKey("genres.genre_id"))

    #foreign keys used by "Band Genres" table
    bands = db.relationship("Band", back_populates = "band_genres")
    genre = db.relationship("Genre", back_populates = "band_genres")

    def __repr__(self):
        return f'<Band_Genre band_genre_id = { self.band_genre_id } band_id = { self.band_id } genre_id = { self.genre_id }>'

####### Venue information. #######

class Venue(db.Model):
    """Table for venue information."""

    __tablename__ = "venues"

    venue_id = db.Column(db.Integer, autoincrement = True, primary_key = True)
    venue_name = db.Column(db.String, unique = True, nullable = False)
    venue_phone = db.Column(db.String, unique = False, nullable = False)
    venue_address = db.Column(db.Text, unique = True, nullable = False)
    venue_payrate = db.Column(db.Integer, nullable = True)
    venue_logo = db.Column(db.Text, nullable = True)
    venue_photo = db.Column(db.Text, nullable = True)

    #tables using "venues" table data as foreign key
    gigs = db.relationship("Gig", back_populates = "venue")
    users = db.relationship("User", back_populates = "venue")
    venue_genres = db.relationship("Venue_Genre", back_populates = "venue")

    def __repr__(self):
        return f'<Venue venue_id = { self.venue_id } venue_name = { self.venue_name }>'

class Venue_Genre(db.Model):
    """Table for venue genres."""

    __tablename__ = "venue_genres"

    venue_genre_id = db.Column(db.Integer, autoincrement = True, primary_key = True)
    venue_id = db.Column(db.Integer, db.ForeignKey("venues.venue_id"))
    genre_id = db.Column(db.Integer, db.ForeignKey("genres.genre_id"))

    #foreign keys used by "Venue Genres" table
    venue = db.relationship("Venue", back_populates = "venue_genres")
    genre = db.relationship("Genre", back_populates = "venue_genres")

    def __repr__(self):
        return f'<Venue_Genre venue_genre_id = { self.venue_genre_id } venue_id = { self.venue_id } genre_id = { self.genre_id }>'

def connect_to_db(flask_app, db_uri="postgresql:///giggogo", echo=False):
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)

if __name__ == "__main__":
    from server import app

    connect_to_db(app)