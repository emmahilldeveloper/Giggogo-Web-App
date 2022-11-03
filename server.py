from flask import Flask, redirect, render_template, session, request, flash
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

    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        user_email = crud.search_users_by_email(email)
        user_password = crud.search_users_by_password(password)

        if 'user' in session: 
            email = request.form.get("email") 
            user_id = crud.search_user_by_id(email) 
            session['user'] = user_id # 
        else: 
            user_id = session['user'] = {}

        if user_email and user_password == True:
            if crud.search_for_user_type(email) == 'Band':
                return redirect("/bandprofile")
            else:
                return redirect("/venueprofile")
        else:
            flash("ERROR: Incorrect credentials. Try again.", category='danger')
            return render_template("login.html")
    else:
        return render_template("login.html")

####### User Sign Up #######

@app.route("/signup", methods = ["GET", "POST"])
def sign_up():
    """Shows sign up form to create a new user."""

    if request.method == "POST":
        first_name = request.form.get("signup-first-name")
        last_name = request.form.get("signup-last-name")
        email = request.form.get("signup-email")
        password = request.form.get("signup-password")
        profile_photo = request.form.get("profile-photo")
        user_type = request.form.get("signup-user-type")

        user_check = crud.search_users_by_email(email)

        if user_check == True:
            flash("ERROR: An account already exists with that email. Please login.", category='danger')
            return redirect("/login")
        else:
            if user_type == "Band":
                band_id = request.form.get("band-dropdown")
                venue_id = None

                user = crud.create_user(first_name, last_name, email, password, band_id, venue_id, profile_photo)
                db.session.add(user)
                db.session.commit()
                flash("SUCCESS: Please log in.", category='success')
                return redirect("/login")
            else:
                band_id = None
                venue_id = request.form.get("venue-dropdown")

                user = crud.create_user(first_name, last_name, email, password, band_id, venue_id, profile_photo)
                db.session.add(user)
                db.session.commit()
                flash("SUCCESS: Please log in.", category='success')
                return redirect("/login")
    else:
        bands = crud.all_bands()
        venues = crud.all_venues()
        return render_template("signup.html", bands = bands, venues = venues)

####### Band User Profile #######

@app.route("/bandprofile")
def band_profile():
    """Shows profile of user."""

    bands = crud.all_bands()
    users = crud.all_users()

    user_id = session.get("user")
    print(user_id) #this is empty

    return render_template("bandprofile.html", bands = bands, users = users)

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