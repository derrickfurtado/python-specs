"""Crud Operations"""

from model import User, Movie, Rating, Cast_Film_Index, Cast, db, connect_to_db





def create_user(first_name, last_name, email, password):
    new_user = User(first_name, last_name, email, password)
    return new_user

def create_movie(title, description, release_date, img_url):
    new_movie = Movie(title, description, release_date, img_url)
    return new_movie

def create_rating(user_id, movie_id, rating, description):
    new_rating = Rating(user_id, movie_id, rating, description)
    return new_rating

def create_cast(full_name, dob, bio):
    new_actor = Cast(full_name, dob, bio)
    return new_actor

def create_actor_movie_index(cast_id, movie_id):
    new_pairing = Cast_Film_Index(cast_id, movie_id)
    return new_pairing

if __name__ == "__main__":
    from server import app
    connect_to_db(app)