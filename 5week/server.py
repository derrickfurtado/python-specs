"""Server for movie ratings app."""

from flask import Flask, render_template, redirect, request, flash, session
from crud import create_rating, create_user, show_all_movies
from model import connect_to_db
from jinja2 import StrictUndefined
from key import server_key

app = Flask(__name__)
# app.app_context().push()              # only used for interactive
app.secret_key = server_key
app.jinja_env.undefined = StrictUndefined



@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/actor_details")
def actor_details():
    return render_template("actor_detail.html")

@app.route("/add_rating")
def add_rating():
    return render_template("add_rating.html")

@app.route("/all_actors")
def show_actors():
    return render_template("all_actors.html")

@app.route("/all_movies")
def show_movies():
    movie_list = show_all_movies()
    return render_template("all_movies.html", movie_list = movie_list)

@app.route("/all_users")
def show_users():
    return render_template("all_users.html")

@app.route("/create_account")
def create_account():
    return render_template("create_account.html")

@app.route("/movie_details")
def movie_details():
    return render_template("movie_detail.html")

@app.route("/user_details")
def user_details():
    return render_template("user_profile.html")



if __name__ == "__main__":

    connect_to_db(app)
    app.run(host = "localhost", port = 4040, debug=True)
