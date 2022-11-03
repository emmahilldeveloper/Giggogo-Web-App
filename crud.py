"""CRUD operations for Giggogo app."""

from re import A
from model import User, Genre, Band, Venue, Gig, Band_Genre, Venue_Genre, connect_to_db, db

####### Functions to seed Giggogo database. #######

def create_user(first_name, last_name, email, password, band_id, venue_id, profile_photo):
    """Create and return a new user."""
    user = User(first_name = first_name, last_name = last_name, 
                email = email, password = password, band_id = band_id, 
                venue_id = venue_id, profile_photo = profile_photo)
    return user

def create_band(band_name, band_phone, band_payrate, band_logo, band_photo, band_video):
    """Create and return a new band."""
    band = Band(band_name = band_name, band_phone = band_phone, 
                band_payrate = band_payrate, band_logo = band_logo, 
                band_photo = band_photo, band_video = band_video)
    return band

def create_venue(venue_name, venue_phone, venue_address, venue_payrate, venue_logo, venue_photo):
    """Create and return a new venue."""
    venue = Venue(venue_name = venue_name, venue_phone = venue_phone, 
                venue_address = venue_address, venue_payrate = venue_payrate, 
                venue_logo = venue_logo, venue_photo = venue_photo)
    return venue

def create_gig(venue_id, band_id, gig_date, final_payrate, gig_complete, gig_paid):
    """Create and return a new gig."""
    gig = Gig(venue_id = venue_id, band_id = band_id, gig_date = gig_date, 
            final_payrate = final_payrate, gig_complete = gig_complete, gig_paid = gig_paid)
    return gig

def create_genre(genre_name):
    """Create and return a new genre."""
    genre = Genre(genre_name = genre_name)
    return genre

def create_band_genre(band_id, genre_id):
    """Create and return a new band genre."""
    band_genre = Band_Genre(band_id = band_id, genre_id = genre_id)
    return band_genre

def create_venue_genre(venue_id, genre_id):
    """Create and return a new venue genre."""
    venue_genre = Venue_Genre(venue_id = venue_id, genre_id = genre_id)
    return venue_genre

####### Functions for signup and login functionality. #######

def search_users_by_email(email):
    """Will return a Boolean answer to if the user-entered
        email is equivalent to an email already in the db."""

    if User.query.filter(User.email == email).first():
        return True
    else:
        return False

def search_users_by_password(password):
    """Will return a Boolean answer to if the user-entered
        password is equivalent to a password already in the db."""

    if User.query.filter(User.password == password).first():
        return True
    else:
        return False

def search_for_user_type(email):
    """Will return a Boolean answer to if the user-entered
        password is equivalent to a password already in the db."""

    user_info = User.query.all()

    for user in user_info:
        if user.email == email:
            band_id = user.band_id
            if band_id == None:
                venue_id = user.venue_id
                return "Venue" #venue_id
            return "Band" #band_id

def all_bands():
    """Will return all bands."""

    return Band.query.all()

def all_venues():
    """Will return all venues."""

    return Venue.query.all()

####### Functions for profile page #######

def all_users():
    """Will return all users."""

    return User.query.all()

if __name__ == '__main__':
    from server import app
    connect_to_db(app)