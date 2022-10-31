"""CRUD operations for Giggogo app."""

from model import User, Genre, Band, Venue, Gig, Band_Genre, Venue_Genre, connect_to_db

def create_user(first_name, last_name, email, password, band_id, venue_id):
    """Create and return a new user."""

    user = User(first_name = first_name, last_name = last_name, 
                email = email, password = password, band_id = band_id, venue_id = venue_id)

    return user

def create_band(band_name, band_phone, band_payrate, band_logo, band_photo, band_video):

    band = Band(band_name = band_name, band_phone = band_phone, 
                band_payrate = band_payrate, band_logo = band_logo, 
                band_photo = band_photo, band_video = band_video)

    return band

def create_venue(venue_name, venue_phone, venue_address, venue_payrate, venue_logo, venue_photo):

    venue = Venue(venue_name = venue_name, venue_phone = venue_phone, 
                venue_address = venue_address, venue_payrate = venue_payrate, 
                venue_logo = venue_logo, venue_photo = venue_photo)

    return venue

def create_gig(venue_id, band_id, gig_date, gig_time, final_payrate, gig_complete, gig_paid):

    gig = Gig(venue_id = venue_id, band_id = band_id, gig_date = gig_date, gig_time = gig_time, final_payrate = final_payrate, gig_complete = gig_complete, gig_paid = gig_paid)

    return gig

def create_genre(genre_name):

    genre = Genre(genre_name = genre_name)

    return genre

def create_band_genre(band_id, genre_id):

    band_genre = Band_Genre(band_id = band_id, genre_id = genre_id)

    return band_genre

def create_venue_genre(venue_id, genre_id):

    venue_genre = Venue_Genre(venue_id = venue_id, genre_id = genre_id)

    return venue_genre

if __name__ == '__main__':
    from server import app
    connect_to_db(app)