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

    #If the user doesn't exist, ERROR
    #If the user's password is not equal to the saved password, ERROR
        if user is None:
            flash("ERROR: Incorrect credentials. Try again.", category='danger')
            return redirect("/login")
        if user.password != password:
            flash("ERROR: Incorrect credentials. Try again.", category='danger')
            return redirect("/login")

    #Create session cookie for that user's information
        session["user_id"] = user.user_id
    
    #Redirect the user based on user's profile type
        if user.band_id is None:
            return redirect("venueprofile")
        if user.venue_id is None:
            return redirect("/bandprofile")

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
        user_type = request.form.get("signup-user-type")

        #If the new user is a band, create a band profile
        if user_type == "Band":
            band_id = request.form.get("band-dropdown")
            venue_id = None

            user = crud.create_user(first_name, last_name, email, password, band_id, venue_id, profile_photo)
            db.session.add(user)
            db.session.commit()
            flash("SUCCESS: Please log in.", category='success')
            return redirect("/login")
        #If the new user is a venue, create a venue profile
        else:
            band_id = None
            venue_id = request.form.get("venue-dropdown")

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

####### Band User Profile #######

@app.route("/bandprofile")
def band_profile():
    """Shows profile of user."""

    #If the user has logged in and their cookies are saved, get all their data
    if "user_id" in session:
        user_id = session["user_id"]
        user_info = crud.all_user_info_specific(user_id)
        
    #Kick them back to the homepage
    else:
        return redirect("/")

    return render_template("bandprofile.html", user_info = user_info)

@app.route("/bandhomepage")
def band_homepage():
    """Shows profile of band."""

    return None

@app.route("/bandsearch")
def band_search():
    """Allows band to search for venues."""

    return None

####### Venue User Profile #######

@app.route("/venueprofile")
def venue_profile():
    """Shows profile of user."""

    venues = crud.all_venues()
    users = crud.all_users()

    return render_template("venueprofile.html", venues = venues, users = users)

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