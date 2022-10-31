"""Sample data for Giggogo app."""

import os
import json
from random import choice, randint
from datetime import datetime

import crud
import model
import server

os.system("dropdb ratings")

os.system("createdb ratings")

model.connect_to_db(server.app)

model.db.create_all()

bands_in_db = []
venues_in_db = []
gigs_in_db = []
genres_in_db = []

