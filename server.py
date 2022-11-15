from flask import Flask, redirect, render_template, session, request, flash, url_for, jsonify
from itsdangerous import json
from jinja2 import StrictUndefined
from model import connect_to_db, db
import crud

app = Flask(__name__)
app.config.update(TESTING=True, SECRET_KEY='DEV')
app.jinja_env.undefined = StrictUndefined
app.jinja_env.auto_reload = True

####### Homepage #################################################################################################

@app.route("/")
def index():
    """Returns the homepage."""
    return render_template("homepage.html")

####### User Log In #################################################################################################

@app.route("/login", methods = ["GET", "POST"])
def login():
    """Allows established users to log into their accounts."""

    #Get data from login form
    #Get all of user's data (from searching by entered email)
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        user = crud.all_user_info_by_email(email)

        #Create session cookie for that user's information
        session["user_id"] = user.user_id

    #If the user doesn't exist, ERROR
    #If the user's password is not equal to the saved password, ERROR
        if user is None:
            flash("ERROR: Incorrect credentials. Try again.", category='danger')
            return redirect("/login")
        if user.password != password:
            flash("ERROR: Incorrect credentials. Try again.", category='danger')
            return redirect("/login")
        if user:
            return redirect("/profile")

    #Load the page
    else:
        return render_template("login.html")

####### User Sign Up #################################################################################################

@app.route("/signup", methods = ["GET", "POST"])
def sign_up():
    """Shows sign up form to create a new user."""

    #Get data from siginup form
    if request.method == "POST":
        first_name = request.form.get("signup-first-name")
        last_name = request.form.get("signup-last-name")
        email = request.form.get("signup-email")
        password = request.form.get("signup-password")
        profile_photo = request.form.get("profile-photo")
        band_id = None
        venue_id = None
        email_check = crud.all_user_info_by_email(email)

        #Check if email is already in the db
        if email_check:
            flash("ERROR: Email already exists. Please login.", category='danger')
            return redirect("/login")

        #Create user, will set the band id or venue id in later steps
        user = crud.create_user(first_name, last_name, email, password, band_id, venue_id, profile_photo)
        db.session.add(user)
        db.session.commit()
        flash("SUCCESS: Please log in.", category='success')
        return redirect("/login")

    #Load the page
    else:
        bands = crud.all_bands()
        venues = crud.all_venues()
        return render_template("signup.html", bands = bands, venues = venues)

####### Who Are You #################################################################################################

@app.route("/whoareyou")
def who_are_you():
    """User selects a user type."""
    return render_template("whoareyou.html")

@app.route("/band")
def band():
    """User creates a band or joins a band."""
    return render_template("/Band/band.html")

@app.route("/newband", methods = ["GET", "POST"])
def new_band():
    """Let's user create a new band."""

    #Get form info to create a band
    if request.method == "POST":
        band_name = request.form.get("create-band-name")
        band_phone = request.form.get("create-band-phone")
        band_payrate = request.form.get("create-band-payrate")
        band_logo = request.form.get("create-band-logo")
        band_photo = None
        band_video = None

        #Create new band to db
        band = crud.create_band(band_name, band_phone, band_payrate, band_logo, band_photo, band_video)
        db.session.add(band)
        db.session.commit()

        return redirect("/findband")

    #Load the page
    else:
        return render_template("/Band/newband.html")

@app.route("/findband", methods = ["GET", "POST"])
def find_band():
    """Let's user find an existing band."""

    #Get form info to find a band, assign that band id to the user's info and save it to the db
    if request.method == "POST":
        band_id = request.form.get("band-dropdown")
        user_id = session["user_id"]
        user_info = crud.all_user_info_specific(user_id)
        user_info.band_id = band_id
        db.session.commit()
        return redirect('/profile')

    #Load the page
    else:
        bands = crud.all_bands()
        return render_template("/Band/findband.html", bands = bands)

@app.route("/venue")
def venue():
    """User creates a venue or joins a venue."""
    return render_template("/Venue/venue.html")

@app.route("/newvenue", methods = ["GET", "POST"])
def new_venue():
    """Let's user create a new venue."""

    #Get form info to create a venue
    if request.method == "POST":
        venue_name = request.form.get("create-venue-name")
        venue_phone = request.form.get("create-venue-phone")
        venue_payrate = request.form.get("create-venue-payrate")
        venue_address = request.form.get("create-venue-address")
        venue_logo = request.form.get("create-venue-logo")
        venue_photo = None

        #Create new venue to db
        venue = crud.create_venue(venue_name, venue_phone, venue_address, venue_payrate, venue_logo, venue_photo)
        db.session.add(venue)
        db.session.commit()

        return redirect("/findvenue")

    #load the page
    else:
        return render_template("/Venue/newvenue.html")

@app.route("/findvenue", methods = ["GET", "POST"])
def find_venue():
    """Let's user find an existing venue."""

    #Get form info to find a venue, assign that venue id to the user's info and save it to the db
    if request.method == "POST":
        venue_id = request.form.get("venue-dropdown")
        user_id = session["user_id"]
        user_info = crud.all_user_info_specific(user_id)
        user_info.venue_id = venue_id
        db.session.commit()
        return redirect('/profile')

    #Load the page
    else:
        venues = crud.all_venues()
        return render_template("/Venue/findvenue.html", venues = venues)

####### User Profile ########################################################################################################

def user_determination():
    """Helps server determine user type and route to correct homepage."""
    
    #Gets user session details
    if "user_id" in session:
        user_id = session["user_id"]
        user_info = crud.all_user_info_specific(user_id)

        #If there is no band or venue id, kick the user out
        #If there's a value for venue id, send user to venue page
        #If there's a value for band id, send user to band page
        if (user_info.band_id is None) and (user_info.venue_id is None):
            return redirect("/whoareyou")
        elif user_info.venue_id:
            return redirect(url_for("venue_homepage", venue_id = user_info.venue_id))
        elif user_info.band_id:
            return redirect(url_for("band_homepage", band_id = user_info.band_id))

    #Kick them back to the homepage is there are no user cookies
    else:
        return redirect("/")

@app.route("/profile")
def user_routes_to_home_profile():
    """Redirects to band or venue homepage."""

    #This just redirects the user to the right page
    return user_determination()

@app.route("/user/<user_id>")
def user_profile(user_id):
    """Shows profile of user."""

    #If the user has logged in and their cookies are saved, get all their data
    if "user_id" in session:
        user_id = session["user_id"]
        user_info = crud.all_user_info_specific(user_id)
        band_id = user_info.band_id
        band_info = crud.all_band_info(band_id)

    #Kick them back to the homepage
    else:
        return redirect("/")

    return render_template("profile.html", user_info = user_info, band_info = band_info)

@app.route("/edituser", methods = ["GET", "POST"])
def edit_user_data():
    """Allows user to edit their user data."""

    #If the user has logged in and their cookies are saved, get all their data
    if "user_id" in session:
        user_id = session["user_id"]

    #Kick them back to the homepage
    else:
        return redirect("/")

    #Get data from siginup form
    if request.method == "POST":
        first_name = request.form.get("first-name")
        last_name = request.form.get("last-name")
        email = request.form.get("email")
        password = request.form.get("password")
        profile_photo = request.form.get("profile-photo")

        user = crud.all_user_info_specific(user_id)

        if first_name:
            user.first_name = first_name
        if last_name:
            user.last_name = last_name
        if email:
            user.email = email
        if password:
            user.password = password
        if profile_photo:
            user.profile_photo = profile_photo
        db.session.commit()
        flash("User Information Successfully Updated.", category='success')
        return redirect("/user/<user_id>")

    #Load the page
    else:
        return render_template("edituserdata.html")

####### Band/Venue Home Profile ##################################################################################################

@app.route("/venuehome/<venue_id>")
def venue_homepage(venue_id):
    """Shows profile of venue."""

    #If the user has logged in and their cookies are saved, get all their data
    if "user_id" in session:
        user_id = session["user_id"]
        user_info = crud.all_user_info_specific(user_id)
        
    #Kick them back to the homepage
    else:
        return redirect("/")

    # #Show venue homepage
    venue_info = crud.all_venue_info(venue_id)
    gig_info = crud.all_gigs_by_venue(venue_id)

    bands = []

    for gig in gig_info:
        band_id = gig.band_id
        band_info = crud.all_band_info(band_id)
        bands_dict = {}
        bands_dict["band_name"] = band_info.band_name
        bands_dict["gig_date"] = gig.gig_date
        bands_dict["gig_id"] = gig.gig_id
        bands_dict["band_id"] = band_info.band_id
        bands.append(bands_dict)

    return render_template("venuehome.html", venue_info = venue_info, user_info = user_info, gig_info = gig_info, bands = bands)

@app.route("/bandhome/<band_id>")
def band_homepage(band_id):
    """Shows profile of band."""

    #If the user has logged in and their cookies are saved, get all their data
    if "user_id" in session:
        user_id = session["user_id"]
        user_info = crud.all_user_info_specific(user_id)
        
    #Kick them back to the homepage
    else:
        return redirect("/")

    #Show band homepage
    band_info = crud.all_band_info(band_id)
    gig_info = crud.all_gigs_by_band(band_id)
    all_members = crud.all_band_members(band_id)

    venues = []
    members = []

    for band_member in all_members:
        user_id = band_member.user_id
        band_member_info = crud.all_user_info_specific(user_id)
        members_dict = {}
        members_dict["member_id"] = band_member_info.user_id
        members_dict["member_name"] = band_member_info.first_name + " " + band_member_info.last_name
        members_dict["member_photo"] = band_member_info.profile_photo
        members.append(members_dict)

    for gig in gig_info:
        venue_id = gig.venue_id
        venue_info = crud.all_venue_info(venue_id)
        venues_dict = {}
        venues_dict["venue_name"] = venue_info.venue_name
        venues_dict["venue_id"] = venue_info.venue_id
        venues_dict["gig_date"] = gig.gig_date
        venues_dict["gig_id"] = gig.gig_id
        venues.append(venues_dict)

    return render_template("bandhome.html", band_info = band_info, user_info = user_info, gig_info = gig_info, venues = venues, members = members)

####### Search Page #############################################################################################################

@app.route("/search", methods=['GET', 'POST'])
def band_or_venue_search():
    """Allows band/venue to search for the opposite."""

    #If the user has logged in and their cookies are saved, get all their data
    if "user_id" in session:
        user_id = session["user_id"]
        user_info = crud.all_user_info_specific(user_id)
    #Kick them back to the homepage
    else:
        return redirect("/")

    genres = []

    if user_info.venue_id is None:
        all_genres = crud.all_genres()
        for genre in all_genres:
            genres_dict = {}
            genres_dict["genre_name"] = genre.genre_name
            genres_dict["genre_id"] = genre.genre_id
            genres.append(genres_dict)

        return render_template("bandsearch.html", user_info = user_info, genres = genres)
    elif user_info.band_id is None:
        all_genres = crud.all_genres()
        band_count = ["1","2","3","4","5","6","7","8","9","10"]
        for genre in all_genres:
            genres_dict = {}
            genres_dict["genre_name"] = genre.genre_name
            genres_dict["genre_id"] = genre.genre_id
            genres.append(genres_dict)

        return render_template("venuesearch.html", user_info = user_info, genres = genres, band_count = band_count)

####### Search for Bands JSON response compiler #########################

@app.route('/api/venuesearch', methods=['POST'])
def venue_search():
    """Returns results from search form."""

    low = request.json['low']
    med = request.json['med']
    medhigh = request.json['medhigh']
    high = request.json['high']
    genres = request.json['genre']
    sizes = request.json['size']

    matching_bands = []

    for size in sizes:
        all_bands = crud.all_bands()
        band_ids = []

        for i in range(len(all_bands)):
            band_id = all_bands[i].band_id
            band_ids.append(band_id)

        for band_id in band_ids:
            count_members = crud.all_users_in_band(band_id)
            all_band_info = crud.all_band_info(band_id)

            if int(size) == count_members:
                bands_dict = {}
                bands_dict['band_name'] = all_band_info.band_name
                bands_dict['band_logo'] = all_band_info.band_logo
                bands_dict['band_payrate'] = all_band_info.band_payrate
                bands_dict['band_id'] = all_band_info.band_id
                matching_bands.append(bands_dict)

    for genre in genres:
        bands = crud.all_bands_by_genre(genre)

        for band in bands:
            band_id = band.band_id
            band_details = crud.all_band_info(band_id)
            bands_dict = {}
            bands_dict['band_name'] = band_details.band_name
            bands_dict['band_logo'] = band_details.band_logo
            bands_dict['band_payrate'] = band_details.band_payrate
            bands_dict['band_id'] = band.band_id
            matching_bands.append(bands_dict)

    if low is True:
        all_low_bands = crud.low_band_payrate()
        for band in all_low_bands:
            low_band = {}
            low_band['band_name'] = band.band_name
            low_band['band_logo'] = band.band_logo
            low_band['band_payrate'] = band.band_payrate
            low_band['band_id'] = band.band_id
            matching_bands.append(low_band)

    if med is True:
        all_med_bands = crud.med_band_payrate()
        for band in all_med_bands:
            med_band = {}
            med_band['band_name'] = band.band_name
            med_band['band_logo'] = band.band_logo
            med_band['band_payrate'] = band.band_payrate
            med_band['band_id'] = band.band_id
            matching_bands.append(med_band)

    if medhigh is True:
        all_medhigh_bands = crud.medhigh_band_payrate()
        for band in all_medhigh_bands:
            medhigh_band = {}
            medhigh_band['band_name'] = band.band_name
            medhigh_band['band_logo'] = band.band_logo
            medhigh_band['band_payrate'] = band.band_payrate
            medhigh_band['band_id'] = band.band_id
            matching_bands.append(medhigh_band)

    if high is True:
        all_high_bands = crud.high_band_payrate()
        for band in all_high_bands:
            high_band = {}
            high_band['band_name'] = band.band_name
            high_band['band_logo'] = band.band_logo
            high_band['band_payrate'] = band.band_payrate
            high_band['band_id'] = band.band_id
            matching_bands.append(high_band)

    #makes sure there are not duplicates in my search results
    results = []
    for i in range(len(matching_bands)):
        if matching_bands[i] not in matching_bands[i + 1:]:
            results.append(matching_bands[i])

    return jsonify({'matches': results})

####### Search for Venues JSON response compiler #########################

@app.route('/api/bandsearch', methods=['POST'])
def band_search():
    """Returns results from search form."""

    low = request.json['low']
    med = request.json['med']
    medhigh = request.json['medhigh']
    high = request.json['high']
    genres = request.json['genre']

    matching_venues = []

    for genre in genres:
        venues = crud.all_venues_by_genre(genre)

        for venue in venues:
            venue_id = venue.venue_id
            venue_details = crud.all_venue_info(venue_id)
            venues_dict = {}
            venues_dict['venue_name'] = venue_details.venue_name
            venues_dict['venue_logo'] = venue_details.venue_logo
            venues_dict['venue_payrate'] = venue_details.venue_payrate
            venues_dict['venue_id'] = venue.venue_id
            matching_venues.append(venues_dict)

    if low is True:
        all_low_venues = crud.low_venue_payrate()
        for venue in all_low_venues:
            low_venue = {}
            low_venue['venue_name'] = venue.venue_name
            low_venue['venue_logo'] = venue.venue_logo
            low_venue['venue_payrate'] = venue.venue_payrate
            low_venue['venue_id'] = venue.venue_id
            matching_venues.append(low_venue)

    if med is True:
        all_med_venues = crud.med_venue_payrate()
        for venue in all_med_venues:
            med_venue = {}
            med_venue['venue_name'] = venue.venue_name
            med_venue['venue_logo'] = venue.venue_logo
            med_venue['venue_payrate'] = venue.venue_payrate
            med_venue['venue_id'] = venue.venue_id
            matching_venues.append(med_venue)

    if medhigh is True:
        all_medhigh_venues = crud.medhigh_venue_payrate()
        for venue in all_medhigh_venues:
            medhigh_venue = {}
            medhigh_venue['venue_name'] = venue.venue_name
            medhigh_venue['venue_logo'] = venue.venue_logo
            medhigh_venue['venue_payrate'] = venue.venue_payrate
            medhigh_venue['venue_id'] = venue.venue_id
            matching_venues.append(medhigh_venue)

    if high is True:
        all_high_venues = crud.high_venue_payrate()
        for venue in all_high_venues:
            high_venue = {}
            high_venue['venue_name'] = venue.venue_name
            high_venue['venue_logo'] = venue.venue_logo
            high_venue['venue_payrate'] = venue.venue_payrate
            high_venue['venue_id'] = venue.venue_id
            matching_venues.append(high_venue)

    #makes sure there are not duplicates in my search results
    results = []
    for i in range(len(matching_venues)):
        if matching_venues[i] not in matching_venues[i + 1:]:
            results.append(matching_venues[i])

    return jsonify({'matches': results})

####### Gig Book Page #############################################################################################################

@app.route("/bookband/<band_id>", methods = ["GET", "POST"])
def venue_book_band(band_id):
    """A venue can book a band."""

    #If the user has logged in and their cookies are saved, get all their data
    if "user_id" in session:
        user_id = session["user_id"]
        user_info = crud.all_user_info_specific(user_id)
    #Kick them back to the homepage
    else:
        return redirect("/")

    band_info = crud.all_band_info(band_id)

    if request.method == "POST":
        request_date = request.form.get("request-date")
        request_time = request.form.get("request-time")
        gig_date = request_date + " " + request_time
        venue_id = user_info.venue_id
        final_payrate = request.form.get("request-payrate")
        gig_complete = False
        gig_paid = False
        band_id = band_info.band_id

        gig = crud.create_gig(venue_id, band_id, gig_date, final_payrate, gig_complete, gig_paid)
        db.session.add(gig)
        db.session.commit()
        flash("SUCCESS: Gig request sent.", category='success')
        return redirect(url_for("venue_homepage", venue_id = user_info.venue_id))

    else:
        return render_template("bookband.html", user_info = user_info, band_info = band_info)

@app.route("/bookvenue/<venue_id>", methods = ["GET", "POST"])
def band_book_venue(venue_id):
    """A band can book a venue."""

    #If the user has logged in and their cookies are saved, get all their data
    if "user_id" in session:
        user_id = session["user_id"]
        user_info = crud.all_user_info_specific(user_id)
    #Kick them back to the homepage
    else:
        return redirect("/")

    venue_info = crud.all_venue_info(venue_id)

    if request.method == "POST":
        request_date = request.form.get("request-date")
        request_time = request.form.get("request-time")
        gig_date = request_date + " " + request_time
        venue_id = venue_info.venue_id
        final_payrate = request.form.get("request-payrate")
        gig_complete = False
        gig_paid = False
        band_id = user_info.band_id

        gig = crud.create_gig(venue_id, band_id, gig_date, final_payrate, gig_complete, gig_paid)
        db.session.add(gig)
        db.session.commit()
        flash("SUCCESS: Gig request sent.", category='success')
        return redirect(url_for("band_homepage", band_id = user_info.band_id))

    else:
        return render_template("bookvenue.html", user_info = user_info, venue_info = venue_info)

if __name__ == "__main__":

    connect_to_db(app)

    app.run(
        host="0.0.0.0",
        use_reloader=False,
        use_debugger=False,
        passthrough_errors=True,
    )