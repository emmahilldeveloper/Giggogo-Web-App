from flask import Flask, redirect, render_template, session, request, flash, url_for
from jinja2 import StrictUndefined
from model import connect_to_db, db
import crud

app = Flask(__name__)
app.config.update(TESTING=True, SECRET_KEY='DEV')
app.jinja_env.undefined = StrictUndefined
app.jinja_env.auto_reload = True

####### Homepage #######

@app.route("/")
def index():
    """Returns the homepage."""
    return render_template("homepage.html")

####### User Log In #######

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

    #Redirect the user based on user's profile type
        # if user.band_id is None:
        #     return redirect("venueprofile")
        # if user.venue_id is None:
        #     return redirect("/bandprofile")

    #Load the page
    else:
        return render_template("login.html")

####### User Sign Up #######

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
        # user_type = request.form.get("signup-user-type")
        email_check = crud.all_user_info_by_email(email)

        #Check if email is already in the db
        if email_check:
            flash("ERROR: Email already exists. Please login.", category='danger')
            return redirect("/login")

        # #If the new user is a band, create a band profile
        # if user_type == "Band":
        #     band_user_type = request.form.get("band-dropdown")
        #     venue_user_type = None

            # #If their band isn't in the db, create their band in the db
            # if band_user_type is None:
            #     band_name = request.form.get("create-band-name")
            #     band_phone = request.form.get("create-band-phone")
            #     band_payrate = request.form.get("create-band-payrate")
            #     band_logo = request.form.get("create-band-logo")
            #     band_photo = None
            #     band_video = None

            #     band = crud.create_band(band_name, band_phone, band_payrate, band_logo, band_photo, band_video)
            #     db.session.add(band)
            #     db.session.commit()

            #     band_info = crud.all_band_info_by_name(band_name)
            #     band_id = band_info.band_name
            #     venue_id = None

        user = crud.create_user(first_name, last_name, email, password, band_id, venue_id, profile_photo)
        db.session.add(user)
        db.session.commit()
        flash("SUCCESS: Please log in.", category='success')
        return redirect("/login")

            #Create a user with an existing band
        #     band_id = band_user_type
        #     venue_id = None
        #     user = crud.create_user(first_name, last_name, email, password, band_id, venue_id, profile_photo)
        #     db.session.add(user)
        #     db.session.commit()
        #     flash("SUCCESS: Please log in.", category='success')
        #     return redirect("/login")
        # #If the new user is a venue, create a venue profile
        # else:
        #     band_user_type = None
        #     venue_user_type = request.form.get("venue-dropdown")\

            # #If their venue isn't in the db, create their venue in the db
            # if venue_user_type is None:
            #     venue_name = request.form.get("create-venue-name")
            #     venue_phone = request.form.get("create-venue-phone")
            #     venue_payrate = request.form.get("create-venue-payrate")
            #     venue_address = request.form.get("create-venue-address")
            #     venue_logo = request.form.get("create-venue-logo")
            #     venue_photo = None

            #     venue = crud.create_venue(venue_name, venue_phone, venue_address, venue_payrate, venue_logo, venue_photo)
            #     db.session.add(venue)
            #     db.session.commit()
            #     flash("SUCCESS: Please log in.", category='success')
            #     return redirect("/login")

            #Create a user with an existing venue
            # user = crud.create_user(first_name, last_name, email, password, band_id, venue_id, profile_photo)
            # db.session.add(user)
            # db.session.commit()
            # flash("SUCCESS: Please log in.", category='success')
            # return redirect("/login")

    #Load the page
    else:
        bands = crud.all_bands()
        venues = crud.all_venues()
        return render_template("signup.html", bands = bands, venues = venues)

####### Who Are You #######

@app.route("/whoareyou")
def who_are_you():
    """User selects a user type."""
    return render_template("whoareyou.html")

@app.route("/band")
def band():
    """User creates a band or joins a band."""
    return render_template("band.html")

@app.route("/newband", methods = ["GET", "POST"])
def new_band():
    """Let's user create a new band."""

    if request.method == "POST":
        band_name = request.form.get("create-band-name")
        band_phone = request.form.get("create-band-phone")
        band_payrate = request.form.get("create-band-payrate")
        band_logo = request.form.get("create-band-logo")
        band_photo = None
        band_video = None

        band = crud.create_band(band_name, band_phone, band_payrate, band_logo, band_photo, band_video)
        db.session.add(band)
        db.session.commit()

        return redirect("/findband")

    else:
        return render_template("newband.html")

@app.route("/findband", methods = ["GET", "POST"])
def find_band():
    """Let's user find an existing band."""

    bands = crud.all_bands()

    return render_template("findband.html", bands = bands)




@app.route("/venue")
def venue():
    """User creates a band or joins a band."""
    return render_template("venue.html")

####### Band User Profile #######

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

@app.route("/bandhomepage")
def band_homepage():
    """Shows profile of band."""

    return None

@app.route("/bandsearch")
def band_search():
    """Allows band to search for venues."""

    return None

####### Venue User Profile #######

@app.route("/venuehomepage")
def venue_homepage():
    """Shows profile of venue."""

    return None

@app.route("/venuesearch")
def venue_search():
    """Allows venues to search for bands."""

    return None

if __name__ == "__main__":

    connect_to_db(app)

    app.run(
        host="0.0.0.0",
        use_reloader=True,
        use_debugger=True,
    )