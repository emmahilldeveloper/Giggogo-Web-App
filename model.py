"""Models for Giggogo app."""

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
    user_type = db.Column(db.String, db.ForeignKey("user_type.user_type"))
    username = db.Column(db.String, unique = True, nullable = False)

    user_types = db.relationship("User_Type", back_populates = "users")
    bands = db.relationship("Band", back_populates = "users")
    venues = db.relationship("Venue", back_populates = "users")

    def __repr__(self):
        return f'<User user_id = { self.user_id } email = { self.email }>'

class User_Type(db.Model):
    """Table for user type (band or venue)."""

    __tablename__ = "user_types"

    user_type_id = db.Column(db.Integer, autoincrement = True, primary_key = True)
    user_type = db.Column(db.String, nullable = False)

    user = db.relationship("User", back_populates = "user_types")
    band = db.relationship("Band", back_populates = "user_types")
    venue = db.relationship("Venue", back_populates = "user_types")

    def __repr__(self):
        return f'<User_Type user_type_id = { self.user_type_id } user_type = { self.user_type }>'

class Genre(db.Model):
    """Table for possible genres."""

    __tablename__ = "genres"

    genre_id = db.Column(db.Integer, autoincrement = True, primary_key = True)
    genre_name = db.Column(db.String, nullable = True)

    def __repr__(self):
        return f'<Genre genre_id = { self.genre_id } genre_name = { self.genre_name }>'

class Band(db.Model):
    """Table for band information."""

    __tablename__ = "bands"

    band_id = db.Column(db.Integer, autoincrement = True, primary_key = True)
    username = db.Column(db.String, db.ForeignKey("user.username"))
    user_type = db.Column(db.String, db.ForeignKey("user_type.user_type"))
    band_name = db.Column(db.String, unique = True, nullable = False)
    band_phone = db.Column(db.String, unique = True, nullable = False)
    band_members = db.Column(db.String, db.ForeignKey("user.user_id"))
    band_genres = db.Column(db.String, db.ForeignKey("genre.genre_name"))
    band_payrate = db.Column(db.Integer, nullable = True)
    band_logo = db.Column(db.Text, nullable = True)
    band_photo = db.Column(db.Text, nullable = True)
    band_video = db.Column(db.Text, nullable = True)

    user_type = db.relationship("User_Type", back_populates = "bands")
    username = db.relationship("User", back_populates = "bands")

    def __repr__(self):
        return f'<Band band_id = { self.band_id } band_name = { self.band_name }>'

class Venue(db.Model):
    """Table for venue information."""

    __tablename__ = "venues"

    venue_id = db.Column(db.Integer, autoincrement = True, primary_key = True)
    username = db.Column(db.String, db.ForeignKey("user.username"))
    user_type = db.Column(db.String, db.ForeignKey("user_type.user_type"))
    venue_name = db.Column(db.String, unique = True, nullable = False)
    venue_phone = db.Column(db.String, unique = True, nullable = False)
    venue_address = db.Column(db.String, db.ForeignKey("user.user_id"))
    preferred_genres = db.Column(db.String, db.ForeignKey("genre.genre_name"))
    venue_payrate = db.Column(db.Integer, nullable = True)
    venue_logo = db.Column(db.Text, nullable = True)
    venue_photo = db.Column(db.Text, nullable = True)

    user_type = db.relationship("User_Type", back_populates = "venues")
    username = db.relationship("User", back_populates = "venues")

    def __repr__(self):
        return f'<Venue venue_id = { self.venue_id } venue_name = { self.venue_name }>'

class Gig(db.Model):
    """Table for scheduled gig details."""

    __tablename__ = "gigs"

    gig_id = db.Column(db.Integer, autoincrement = True, primary_key = True)
    venue_name = db.Column(db.String, db.ForeignKey("venue.venue_name"))
    band_name = db.Column(db.String, db.ForeignKey("band.band_name"))
    gig_date = db.Column(db.DateTime, unique = True, nullable = False)
    gig_time = db.Column(db.DateTime, unique = True, nullable = False)
    final_payrate = db.Column(db.Integer, nullable = False)
    gig_complete = db.Column(db.Boolean, nullable = False)
    gig_paid = db.Column(db.Boolean, nullable = False)

    def __repr__(self):
        return f'<Gig gig_id = { self.gig_id } venue_name = { self.venue_name } band_name = { self.band_name } gig_date = { self.gig_date }>'

def connect_to_db(flask_app, db_uri="postgresql:///giggogo", echo=True):
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)

if __name__ == "__main__":
    from server import app

    connect_to_db(app)
