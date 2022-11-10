"""Sample data for Giggogo app."""

import os
import json
from datetime import datetime

import crud
import model
import server

os.system("dropdb giggogo")

os.system("createdb giggogo")

model.connect_to_db(server.app)

model.db.create_all()

####### Creating bands in Giggogo database. #######

bands_in_db = []

with open('data/bands.json') as f:
    bands_data = json.loads(f.read())

for band in bands_data:
    band_name = band["band_name"]
    band_phone = band["band_phone"]
    band_payrate = band["band_payrate"]
    band_logo = band["band_logo"]
    band_photo = band["band_photo"]
    band_video = band["band_video"]

    db_band = crud.create_band(band_name, band_phone, band_payrate, band_logo, band_photo, band_video)
    bands_in_db.append(db_band)

model.db.session.add_all(bands_in_db)

# ####### Creating venues in Giggogo database. #######

venues_in_db = []

with open('data/venues.json') as f:
    venues_data = json.loads(f.read())

for venue in venues_data:
    venue_name = venue["venue_name"]
    venue_phone = venue["venue_phone"]
    venue_address = venue["venue_address"]
    venue_payrate = venue["venue_payrate"]
    venue_logo = venue["venue_logo"]
    venue_photo = venue["venue_photo"]

    db_venue = crud.create_venue(venue_name, venue_phone, venue_address, venue_payrate, venue_logo, venue_photo)
    venues_in_db.append(db_venue)

model.db.session.add_all(venues_in_db)

# ####### Creating users in Giggogo database. #######

users_in_db = []

with open('data/users.json') as f:
    users_data = json.loads(f.read())

for user in users_data:
    first_name = user["first_name"]
    last_name = user["last_name"]
    email = user["email"]
    password = user["password"]
    band_id = user["band_id"]
    venue_id = user["venue_id"]
    profile_photo = user["profile_photo"]

    db_user = crud.create_user(first_name, last_name, email, password, band_id, venue_id, profile_photo)
    users_in_db.append(db_user)

model.db.session.add_all(users_in_db)

# ####### Creating genres in Giggogo database. #######

genres_in_db = []

with open('data/genres.json') as f:
    genres_data = json.loads(f.read())

for genre in genres_data:
    genre_name = genre["genre_name"]

    db_genre = crud.create_genre(genre_name)
    genres_in_db.append(db_genre)

model.db.session.add_all(genres_in_db)

# ####### Creating band genres in Giggogo database. #######

band_genres_in_db = []

with open('data/band_genres.json') as f:
    band_genres_data = json.loads(f.read())

for band_genre in band_genres_data:
    band_id = band_genre["band_id"]
    genre_id = band_genre["genre_id"]

    db_band_genre = crud.create_band_genre(band_id, genre_id)
    band_genres_in_db.append(db_band_genre)

model.db.session.add_all(band_genres_in_db)

# ####### Creating venue genres in Giggogo database. #######

venue_genres_in_db = []

with open('data/venue_genres.json') as f:
    venue_genres_data = json.loads(f.read())

for venue_genre in venue_genres_data:
    venue_id = venue_genre["venue_id"]
    genre_id = venue_genre["genre_id"]

    db_venue_genre = crud.create_venue_genre(venue_id, genre_id)
    venue_genres_in_db.append(db_venue_genre)

model.db.session.add_all(venue_genres_in_db)

# ####### Save everything. #######
model.db.session.commit()