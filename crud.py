"""CRUD operations for Giggogo app."""

from re import A
from model import User, Genre, Band, Venue, Gig, Band_Genre, Venue_Genre, Message, connect_to_db, db

####### Functions to seed Giggogo database. #####################################################################################

def create_user(first_name, last_name, email, password, band_id, venue_id, profile_photo):
    """Create and return a new user."""
    user = User(first_name = first_name, last_name = last_name, 
                email = email, password = password, band_id = band_id, 
                venue_id = venue_id, profile_photo = profile_photo)
    return user

def create_band(band_name, band_phone, band_payrate, band_logo, band_photo, band_video, band_website, band_spotify):
    """Create and return a new band."""
    band = Band(band_name = band_name, band_phone = band_phone, 
                band_payrate = band_payrate, band_logo = band_logo, 
                band_photo = band_photo, band_video = band_video, band_website = band_website, band_spotify = band_spotify)
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

####### Functions for signup and login functionality. ##########################################################################

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

####### Functions for profile page ##############################################################################################

def all_users():
    """Will return all users."""

    return User.query.all()

def all_user_info_specific(user_id):
    """Returns all user info for specific user."""

    return User.query.filter(User.user_id == user_id).first()

####### Functions for Home Venue/Band Page ########################################################################################

def all_band_info(band_id):
    """Will return all of band info by band id."""

    return Band.query.filter(Band.band_id == band_id).first()

def all_venue_info(venue_id):
    """Will return all of user info by venue id."""

    return Venue.query.filter(Venue.venue_id == venue_id).first()

def all_band_members(band_id):
    """Will return all of the members in a band."""

    return User.query.filter(User.band_id == band_id).all()

####### Functions for Venue Search Page #################################################################################################

def low_band_payrate():
    """Returns band payrates between $0 and $700"""

    return Band.query.filter(Band.band_payrate < 700).all()

def med_band_payrate():
    """Returns band payrates between $701 and $2000"""

    return Band.query.filter(Band.band_payrate < 2000, Band.band_payrate > 700).all()

def medhigh_band_payrate():
    """Returns band payrates between $2001 and $5000"""

    return Band.query.filter(Band.band_payrate < 5000, Band.band_payrate > 2001).all()

def high_band_payrate():
    """Returns band payrates over $5000"""

    return Band.query.filter(Band.band_payrate > 5000).all()

def all_bands_by_genre(genre_id):
    """Returns all bands with a certain genre preference."""

    return Band_Genre.query.filter(Band_Genre.genre_id == genre_id).all()

def all_users_in_band(band_id):
    """Returns the number of users in a band."""

    specific_band = User.query.filter(User.band_id == band_id).all()
    user_ids = []

    for member in specific_band:
        user_ids.append(member.user_id)

    return len(user_ids)

####### Functions for Band Search Page #################################################################################################

def low_venue_payrate():
    """Returns venue payrates between $0 and $700"""

    return Venue.query.filter(Venue.venue_payrate < 700).all()

def med_venue_payrate():
    """Returns venue payrates between $701 and $2000"""

    return Venue.query.filter(Venue.venue_payrate < 2000, Venue.venue_payrate > 700).all()

def medhigh_venue_payrate():
    """Returns venue payrates between $2001 and $5000"""

    return Venue.query.filter(Venue.venue_payrate < 5000, Venue.venue_payrate > 2001).all()

def high_venue_payrate():
    """Returns venue payrates over $5000"""

    return Venue.query.filter(Venue.venue_payrate > 5000).all()

def all_genres():
    """Returns all genres info."""

    return Genre.query.all()

def all_venues_by_genre(genre_id):
    """Returns all venues with a certain genre preference."""

    return Venue_Genre.query.filter(Venue_Genre.genre_id == genre_id).all()

####### Functions for Booking a Gig Page #################################################################################################

def all_gigs_by_band(band_id):
    """Returns all gigs for a specific band."""

    return Gig.query.filter(Gig.band_id == band_id).all()

def all_gigs_by_venue(venue_id):
    """Returns all gigs for a specific venue."""

    return Gig.query.filter(Gig.venue_id == venue_id).all()

def all_gig_info(gig_id):
    """Returns all gig info for specific gig by gig id."""

    return Gig.query.filter(Gig.gig_id == gig_id).all()

####### Functions for Messaging Page #################################################################################################

def create_message(venue_id, band_id, message_text, sender_type):
    """Create and return a new user."""
    message = Message(venue_id = venue_id, 
                        band_id = band_id, message_text = message_text, sender_type = sender_type)
    return message

def all_messages_between_gig_parties(band_id, venue_id):
    """Returns all messages from band to venue."""

    return Message.query.filter(Message.band_id == band_id, Message.venue_id == venue_id).all()

def all_messages_between_band_members(band_id):
    """Returns all messages between badn members."""

    return Message.query.filter(Message.band_id == band_id).all()

def find_band_by_user(user_id):
    """Returns band_id by user_id."""

    user = User.query.filter(User.user_id == user_id).all()

    return user[0]

def find_venue_by_user(user_id):
    """Returns venue_id by user_id."""

    user = User.query.filter(User.user_id == user_id).all()

    return user[0]

if __name__ == '__main__':
    from server import app
    connect_to_db(app)
