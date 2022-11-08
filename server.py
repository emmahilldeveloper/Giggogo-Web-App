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

####### Band User Profile #################################################################################################

@app.route("/profile")
def profile():
    """Shows profile of user."""

    # user_info

    #If the user has logged in and their cookies are saved, get all their data
    if "user_id" in session:
        user_id = session["user_id"]
        user_info = crud.all_user_info_specific(user_id)
        
    #Kick them back to the homepage
    else:
        return redirect("/")

    if (user_info.band_id is None) and (user_info.venue_id is None):
        return redirect("/whoareyou")

    return render_template("profile.html", user_info = user_info)

@app.route("/home")
def band_or_venue_homepage():
    """Shows profile of band/venue."""

    #If the user has logged in and their cookies are saved, get all their data
    if "user_id" in session:
        user_id = session["user_id"]
        user_info = crud.all_user_info_specific(user_id)
        
    #Kick them back to the homepage
    else:
        return redirect("/")

    #Show band homepage
    if user_info.venue_id is None:
        band_info = crud.all_band_info(user_info.band_id)

        return render_template("bandhome.html", band_info = band_info)
    
    #Show venue homepage
    else:
        venue_info = crud.all_venue_info(user_info.venue_id)
        return render_template("venuehome.html", venue_info = venue_info)

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

    if request.method == "POST":

        #Show band homepage
        if user_info.venue_id is None:
            return render_template("bandsearch.html")

        #Show venue homepage
        else:
        #Get values from checked payrate boxes
            payrate = request.args.getlist("payrate")
            print(payrate)
    
    #Load the page
    else:
        return render_template("venuesearch.html")

@app.route('/api/search', methods=['POST'])
def venue_search():
    """Returns results from search form."""

    low = request.json['low']
    med = request.json['med']
    medhigh = request.json['medhigh']
    high = request.json['high']

    low_bands = []
    med_bands = []
    medhigh_bands = []
    high_bands = []

    if low is True:
        all_low_bands = crud.low_band_payrate()
        for i in range(len(all_low_bands)):
            band_name = all_low_bands[i].band_name
            low_bands.append(band_name)
            band_logo = all_low_bands[i].band_logo
            low_bands.append(band_logo)
            payrate = f'${all_low_bands[i].band_payrate}/hr'
            low_bands.append(payrate)
    if med is True:
        all_med_bands = crud.med_band_payrate()
        for i in range(len(all_med_bands)):
            band_name = all_med_bands[i].band_name
            med_bands.append(band_name)
            band_logo = all_med_bands[i].band_logo
            med_bands.append(band_logo)
            payrate = f'${all_med_bands[i].band_payrate}/hr'
            med_bands.append(payrate)
    if medhigh is True:
        all_medhigh_bands = crud.medhigh_band_payrate()
        for i in range(len(all_medhigh_bands)):
            band_name = all_medhigh_bands[i].band_name
            medhigh_bands.append(band_name)
            band_logo = all_medhigh_bands[i].band_logo
            medhigh_bands.append(band_logo)
            payrate = f'${all_medhigh_bands[i].band_payrate}/hr'
            medhigh_bands.append(payrate)
    if high is True:
        all_high_bands = crud.high_band_payrate()
        for i in range(len(all_high_bands)):
            band_name = all_high_bands[i].band_name
            high_bands.append(band_name)
            band_logo = all_high_bands[i].band_logo
            high_bands.append(band_logo)
            payrate = f'${all_high_bands[i].band_payrate}/hr'
            high_bands.append(payrate)

    return jsonify({'low': low_bands, 'med': med_bands, 'medhigh': medhigh_bands, 'high': high_bands})

if __name__ == "__main__":

    connect_to_db(app)

    app.run(
        host="0.0.0.0",
        use_reloader=True,
        use_debugger=True,
    )