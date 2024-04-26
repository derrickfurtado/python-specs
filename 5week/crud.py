"""Crud Operations"""

from model import User, Movie, Rating, Cast_Film_Index, Cast, db, connect_to_db





def create_user(first_name, last_name, email, password):
    new_user = User(first_name, last_name, email, password)
    return new_user

#######################

def create_movie(title, description, release_date, img_url):
    new_movie = Movie(title, description, release_date, img_url)
    return new_movie

def show_all_movies():
    return Movie.query.order_by(Movie.title).all()

def get_movie_by_id(id):
    return Movie.query.get(id)

#######################

def create_rating(user, movie, score, description):
    new_rating = Rating(user = user, movie = movie, score = score, description = description)
    return new_rating

#######################

def create_cast(full_name, dob, bio):
    new_actor = Cast(full_name, dob, bio)
    return new_actor

def show_all_actors():
    return Cast.query.order_by(Cast.full_name).all()

def get_actor_by_id(id):
    return Cast.query.get(id)

def create_actor_movie_index(cast_id, movie_id):
    new_pairing = Cast_Film_Index(cast_id, movie_id)
    return new_pairing





if __name__ == "__main__":
    from server import app
    connect_to_db(app)