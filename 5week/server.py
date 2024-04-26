"""Server for movie ratings app."""

from flask import Flask, render_template, redirect, request, flash, session
import crud, pdb
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

# @app.route("/login")
# def login():
#     return render_template("login.html")

# @app.route("/create_account")
# def create_account():
#     return render_template("create_account.html")

@app.route("/all_users")
def show_users():
    user_list = crud.show_all_users()
    return render_template("all_users.html", user_list = user_list)

@app.route("/user_details/<user_id>")
def user_details(user_id):
    user = crud.get_user_by_id(user_id)
    rating_list = crud.get_user_ratings(user_id)
    return render_template("user_profile.html", user = user, rating_list = rating_list)

#######################

@app.route("/all_movies")                                                           ### view all movies
def show_movies():
    movie_list = crud.show_all_movies()
    return render_template("all_movies.html", movie_list = movie_list)

@app.route("/movie_detail/<movie_id>")                                                         ### view a single movie
def movie_details(movie_id):
    movie = crud.get_movie_by_id(movie_id)
    rating_list = crud.get_ratings_by_id(movie_id)
    average_rating = crud.get_rating_stats(movie_id)
    return render_template("movie_detail.html", movie = movie, rating_list = rating_list, average_rating = average_rating)

#######################

@app.route("/all_actors")
def show_actors():
    actor_list = crud.show_all_actors()
    return render_template("all_actors.html", actor_list = actor_list)

@app.route("/actor_details/<actor_id>")
def actor_details(actor_id):
    actor = crud.get_actor_by_id(actor_id)
    work_list = actor.cast_list
    return render_template("actor_detail.html", actor = actor, work_list = work_list)

#######################

# @app.route("/add_rating")
# def add_rating():
#     return render_template("add_rating.html")





if __name__ == "__main__":

    connect_to_db(app)
    app.run(host = "localhost", port = 4040, debug=True)
