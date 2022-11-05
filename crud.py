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

def all_user_info_by_email(email):
    """Will return all of a user's information, searching by their email."""

    user = User.query.filter(User.email == email).first()

    return user

def all_bands():
    """Will return all bands."""

    return Band.query.all()

def all_venues():
    """Will return all venues."""

    return Venue.query.all()

def all_band_info_by_name(band_name):
    """Will return all of a band's information, searching by their name."""

    band = Band.query.filter(Band.band_name == band_name).first()

    return band

####### Functions for profile page #######

def all_users():
    """Will return all users."""

    return User.query.all()

def all_user_info_specific(user_id):
    """Returns all user info for specific user."""

    all_info = User.query.filter(User.user_id == user_id).first()

    return all_info

if __name__ == '__main__':
    from server import app
    connect_to_db(app)
