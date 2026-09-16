import os
import re
import random


from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session, jsonify
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
import datetime

from helpers import apology, login_required, lookup

# Configure application
app = Flask(__name__)


# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///project.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")
        if not username:
            return apology("USERNAME CANT BE BLANK")
        if not password:
            return apology("PLEASE TYPE IN A PASSWORD")
        if len(password) < 8:
            return apology("PASSWORD NEEDS TO BE AS LEAST 8 CHARACTERS LONG")
        elif re.search('[0-9]',password) is None:
            return apology("PASSWORD NEEDS TO CONTAIN AT LEAST 1 NUMBER")
        elif re.search('[^a-zA-Z0-9]',password) is None:
            return apology("PASSWORD NEEDS TO CONTAIN AT LEAST 1 SYMBOL")
        if not confirmation:
            return apology("PLEASE TYPE IN A CONFIRMATION")
        if password!= confirmation:
            return apology("PASSWORDS DO NOT MATCH")

        hash = generate_password_hash(password)

        try:
            new_user = db.execute("INSERT INTO users (username, hash) VALUES (?, ?)", username, hash)
        except:
            return apology("USERNAME ALREADY EXISTS")
        session["user_id"] = new_user

        flash("Registered!")
        return redirect("/")

    else:
        return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        return redirect("/")

    # User reached route via GET
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get movie quote."""
    if request.method == "GET":
        return render_template("quote.html")
    else:
        title = request.form.get("title")

        if not title:
            return apology("You must type a title")

        movies = lookup(title)

        if movies == None:
            return apology("Movie does not exist")

        return render_template("quoted.html", movies=movies)


@app.route("/add-to-favorites", methods=["POST"])
@login_required
def add_to_favorites():
    favorite = request.get_json()
    movie_title = favorite['title']
    movie_image = favorite['image']
    movie_url = favorite['url']

    user_id = session["user_id"]

    check = db.execute("SELECT * FROM favoriteMovies WHERE user_id = ? AND title = ?", user_id, movie_title)
    if check :
        return jsonify({ 'success': False, 'error': "This movie is already your favorite" })
    else:
        try:
            db.execute("INSERT INTO favoriteMovies (user_id, title, url, image) VALUES (?, ?, ?, ?)", user_id, movie_title, movie_url, movie_image)
            return jsonify({ 'success': True})
        except Exception as e:
            return jsonify({ 'success': False, 'error': str(e) })


@app.route("/")
@login_required
def index():
    user_id = session["user_id"]
    favorite_movies = db.execute("SELECT * FROM favoriteMovies WHERE user_id = ?", user_id)
    k = min(4, len(favorite_movies))
    random_movies = random.sample(favorite_movies, k)
    return render_template("index.html", movies=random_movies)


@app.route("/favorites")
@login_required
def favorites():
    """Show favorites"""
    user_id = session["user_id"]
    return render_template("favorites.html", favoritemovies= db.execute("SELECT * FROM favoriteMovies WHERE user_id = :id", id = user_id))



