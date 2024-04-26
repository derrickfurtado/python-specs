"""Crud Operations"""

from model import User, Movie, Rating, Cast_Film_Index, Cast, db, connect_to_db
import pdb





def create_user(first_name, last_name, email, password):
    new_user = User(first_name, last_name, email, password)
    return new_user

def user_check_by_email(email):
    return User.query.filter(User.email == email).first()

def show_all_users():
    return User.query.all()

def get_user_by_id(id):
    return User.query.get(id)

def get_user_ratings(user_id):
    return Rating.query.filter_by(user_id = user_id)


#######################

def create_movie(title, description, release_date, img_url):
    new_movie = Movie(title, description, release_date, img_url)
    return new_movie

def show_all_movies():
    return Movie.query.order_by(Movie.title).all()

def get_movie_by_id(movie_id):
    return Movie.query.get(movie_id)


#######################

def create_rating(user, movie, score, description):
    new_rating = Rating(user = user, movie = movie, score = score, description = description)
    return new_rating

def get_ratings_by_id(movie_id):
    rating_list = Rating.query.filter_by(movie_id = movie_id).all()
    return rating_list

def get_rating_stats(movie_id):
    rating_list = Rating.query.filter_by(movie_id = movie_id).all()
    total_score = 0
    counter = 0
    for score in rating_list:
        total_score += score.score
        counter += 1
    average_rating = round(total_score/counter, 2)
    if average_rating < 2:
        average_rating = f"{average_rating} 👎"
    elif average_rating >=2 and average_rating <4:
        average_rating = f"{average_rating} 👌"
    else:
        average_rating = f"{average_rating} 🔥"

    return average_rating


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