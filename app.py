import os
from flask import (
    Flask,
    render_template,
    redirect,
    request,
    url_for,
    session,
    flash,
)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash

APP = Flask(__name__)

APP.config["MONGO_DBNAME"] = os.getenv("DBNAME")
APP.config["MONGO_URI"] = os.getenv("MONGO_URI")
APP.secret_key = os.getenv("SECRET_KEY")
MONGO = PyMongo(APP)

USERS = MONGO.db.users
HEROES = MONGO.db.heroes


@APP.route("/")
def index():
    """
    Renders the home page.
    """
    return render_template(
        "pages/index.html",
        title="Home",
        main_wrapper="index-main-wrapper",
        content_wrapper="index-content-wrapper",
    )


@APP.route("/heroes")
def heroes():
    """
    Renders the page to display all heroes. Checks if a user exists and if so,
    exposes data for the template.
    """
    try:
        user_profile = USERS.find_one({"name": session["username"]})
        raw_favourites = user_profile["favourites"]
        user_favourites = []
        for fav in raw_favourites:
            user_favourites.append(fav["hero"])
        return render_template(
            "pages/heroes.html",
            title="Heroes",
            heroes=HEROES.find(),
            user_favourites=user_favourites,
            main_wrapper="heroes-main-wrapper",
            content_wrapper="heroes-content-wrapper",
        )
    except:
        return render_template(
            "pages/heroes.html",
            title="Heroes",
            heroes=HEROES.find(),
            main_wrapper="heroes-main-wrapper",
            content_wrapper="heroes-content-wrapper",
        )


@APP.route("/add/<hero_id>")
def add_to_favourites(hero_id):
    """
    Adds a hero to the current user's list.
    """
    user_profile = USERS.find_one({"name": session["username"]})
    hero = HEROES.find_one({"_id": ObjectId(hero_id)})
    for key in hero:
        if key == "name":
            hero_name = hero[key]
    USERS.update_one(
        user_profile, {"$push": {"favourites": {"hero": ObjectId(hero_id)}}},
    )
    flash(f"{hero_name} added to your list.")
    return redirect(url_for("heroes"))


@APP.route("/remove/<hero_id>", methods=["GET", "POST"])
def remove_from_favourites(hero_id):
    """
    Removes a hero from the current user's list.
    """
    user_profile = USERS.find_one({"name": session["username"]})
    hero = HEROES.find_one({"_id": ObjectId(hero_id)})
    for key in hero:
        if key == "name":
            hero_name = hero[key]
    USERS.update_one(
        user_profile, {"$pull": {"favourites": {"hero": ObjectId(hero_id)}}}
    )
    flash(f"{hero_name} removed from your list.")
    if "from_profile" in request.form:
        return redirect(url_for("user_list"))
    return redirect(url_for("heroes"))


@APP.route("/note/add/<hero_id>", methods=["POST"])
def add_hero_note(hero_id):
    user_id = ""
    user_profile = USERS.find_one({"name": session["username"]})
    note = request.form.get("note")
    for key in user_profile:
        if key == "_id":
            user_id = user_profile[key]
    USERS.update_one(
        {"_id": ObjectId(user_id), "favourites.hero": ObjectId(hero_id)},
        {"$set": {"favourites.$.note": note}},
    )
    flash("Hero note updated.")
    return redirect(url_for("user_list"))


@APP.route("/note/remove/<hero_id>")
def remove_hero_note(hero_id):
    user_id = ""
    user_profile = USERS.find_one({"name": session["username"]})
    for key in user_profile:
        if key == "_id":
            user_id = user_profile[key]
    USERS.update_one(
        {"_id": ObjectId(user_id), "favourites.hero": ObjectId(hero_id)},
        {"$unset": {"favourites.$.note": ""}},
    )
    flash("Hero note removed.")
    return redirect(url_for("user_list"))


@APP.route("/favourites")
def user_list():
    """
    If a user is logged in, renders the page to show their list, otherwise
    redirects to create account page.
    """
    if session:
        user_profile = USERS.find_one({"name": session["username"]})
        raw_favourites = user_profile["favourites"]
        user_favourites = []
        for fav in raw_favourites:
            hero_id = fav["hero"]
            hero = HEROES.find_one({"_id": hero_id})
            try:
                note = fav["note"]
                hero["note"] = note
                user_favourites.append(hero)
            except KeyError:
                hero["note"] = ""
                user_favourites.append(hero)

        return render_template(
            "pages/user-list.html",
            title="Favourites",
            user_favourites=user_favourites,
            main_wrapper="favourites-main-wrapper",
            content_wrapper="favourites-content-wrapper",
        )

    return redirect(url_for("create_account"))


def set_password(password):
    """
    Encrypts user password.
    """
    return generate_password_hash(password)


def check_password(hash_pw, password):
    """
    Decrypts user password.
    """
    return check_password_hash(hash_pw, password)


def check_user(username):
    """
    Check if user exists in database.
    """
    return USERS.find_one({"name": username})


def create_user(username, password):
    """
    Create new user in database.
    """
    USERS.insert_one(
        {
            "name": username,
            "password": password,
            "favourites": [],
            "primary_role": "",
            "region": "",
            "best_rank": "",
            "current_rank": "",
            "avatar": "../static/images/no_avatar.jpg",
            "biography": "",
        }
    )


@APP.route("/user/create", methods=["GET", "POST"])
def create_account():
    """
    If a user is logged in, renders the page to show their list, otherwise
    renders the page to create account and creates a new user in the database
    upon form submission.
    """
    if session:
        return redirect(url_for("user_list"))

    if request.method == "POST":
        username = request.form["username"].lower()
        user_exists = check_user(username)
        password = request.form["password"]
        password_confirm = request.form["password_confirm"]
        if password == password_confirm:
            if user_exists is None:
                hash_pw = set_password(password)
                create_user(username, hash_pw)
                session["username"] = username
                return redirect(url_for("profile", username=username))
            flash("Username is taken, please try another one.")
        else:
            flash("Password does not match, please re-enter.")

    return render_template(
        "pages/account.html",
        title="Create Account",
        create_account=True,
        main_wrapper="account-main-wrapper",
        content_wrapper="account-content-wrapper",
    )


@APP.route("/user/login", methods=["GET", "POST"])
def login():
    """
    If a user is logged in, renders the page to show their list, otherwise
    renders the page to login and handles requests.
    """
    if session:
        return redirect(url_for("user_list"))

    if request.method == "POST":
        username = request.form["username"].lower()
        password = request.form["password"]
        user_profile = USERS.find_one({"name": username})
        if user_profile:
            user_pw = user_profile["password"]
            check_pw = check_password_hash(user_pw, password)
            if check_pw:
                session["username"] = request.form["username"]
                return redirect(url_for("profile", username=username))

            flash("Incorrect password, please try again.")
        else:
            flash("That username does not exist.")

    return render_template(
        "pages/account.html",
        title="Login",
        create_account=False,
        main_wrapper="account-main-wrapper",
        content_wrapper="account-content-wrapper",
    )


@APP.route("/user/logout")
def logout():
    """
    Logs user out by clearing the session and redirects to home page.
    """
    session.clear()
    return redirect(url_for("index"))


@APP.route("/user/<username>")
def profile(username):
    user_profile = USERS.find_one({"name": username})

    return render_template(
        "pages/user-profile.html",
        title="Profile",
        edit_profile=False,
        main_wrapper="account-main-wrapper",
        content_wrapper="account-content-wrapper",
        user_profile=user_profile,
    )


@APP.route("/edit/<username>", methods=["GET", "POST"])
def edit_profile(username):
    user_profile = USERS.find_one({"name": username})
    user_id = user_profile["_id"]
    current_role = user_profile["primary_role"]
    current_region = user_profile["region"]
    current_brank = user_profile["best_rank"]
    current_crank = user_profile["current_rank"]
    current_avatar = user_profile["avatar"]
    current_biography = user_profile["biography"]

    if request.method == "POST":
        USERS.update_one(
            {"_id": user_id},
            {
                "$set": {
                    "primary_role": request.form.get("primary_role", current_role),
                    "region": request.form.get("region", current_region),
                    "best_rank": request.form.get("best_rank", current_brank),
                    "current_rank": request.form.get("current_rank", current_crank),
                    "avatar": request.form.get("avatar", current_avatar),
                    "biography": request.form.get("biography", current_biography),
                }
            },
        )
        flash("Profile updated.")
        return redirect(url_for("profile", username=user_profile["name"]))

    return render_template(
        "pages/user-profile.html",
        title="Edit Profile",
        edit_profile=True,
        main_wrapper="account-main-wrapper",
        content_wrapper="account-content-wrapper",
        user_profile=user_profile,
        heroes=HEROES.find(),
    )


@APP.errorhandler(404)
def error_page_not_found(error):
    """
    Renders a 404 error page.
    """
    error = str(error)
    return (
        render_template(
            "pages/error.html",
            error=error,
            main_wrapper="index-main-wrapper",
            content_wrapper="error-content-wrapper",
        ),
        404,
    )


@APP.errorhandler(500)
def error_internal_server(error):
    """
    Renders a 500 error page.
    """
    error = str(error)
    return (
        render_template(
            "pages/error.html",
            error=error,
            main_wrapper="index-main-wrapper",
            content_wrapper="error-content-wrapper",
        ),
        500,
    )


if __name__ == "__main__":
    APP.run(host=os.getenv("IP"), port=os.getenv("PORT"), debug=True)
