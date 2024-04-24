"""DB Model classes"""

import os
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()



class User(db.Model):

    __tablename__ = "user_table"

    id = db.Column(db.Integer, autoincrement = True, primary_key = True)
    first_name = db.Column(db.String(255), nullable = False)
    last_name = db.Column(db.String(255))
    email = db.Column(db.String(255), nullable = False, unique = True)
    password = db.Column(db.String(255), nullable = False)

    # ratings =  a list of rating objects

    def __init__(self, first_name, last_name, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password

    def __repr__(self):
        return f'< User id={self.id}, first_name={self.first_name}, last_name={self.last_name}, email={self.email} >'

class Movie(db.Model):
    
    __tablename__ = "movie_table"

    id = db.Column(db.Integer, autoincrement = True, primary_key = True)
    title = db.Column(db.String(255), nullable = False, unique = True)
    description = db.Column(db.String(1000), nullable = False)
    release_date = db.Column(db.Date, nullable = False)
    img_url = db.Column(db.String(500), nullable = False)

    # ratings =  a list of rating objects
    # cast_list = a list of cast index objects

    def __init__(self, title, description, release_date, img_url):
        self.title = title
        self.description = description
        self.release_date = release_date
        self.img_url = img_url

    def __repr__(self):
        return f'< Movie id={self.id}, title={self.title} >'

class Rating(db.Model):

    __tablename__ = "rating_table"

    id = db.Column(db.Integer, autoincrement = True, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey("user_table.id"), nullable = False)
    movie_id = db.Column(db.Integer, db.ForeignKey("movie_table.id"), nullable = False)
    rating = db.Column(db.Integer, nullable = False)
    description = db.Column(db.String(255))

    user = db.relationship("User", backref = "ratings", lazy = "subquery")
    movie = db.relationship("Movie", backref = "ratings", lazy = "subquery")

    def __init__(self, user_id, movie_id, rating, description):
        self.user_id = user_id
        self.movie_id = movie_id
        self.rating = rating
        self.description = description

    def __repr__(self):
        return f'< Rating id={self.id}, user_submitted={self.user_id}, movie_id={self.movie_id}, rating={self.rating} >'

class Cast_Film_Index(db.Model):

    __tablename__ = "index_table"

    id = db.Column(db.Integer, autoincrement = True, primary_key = True)
    cast_id = db.Column(db.Integer, db.ForeignKey("cast_table.id"), nullable = False)
    movie_id = db.Column(db.Integer, db.ForeignKey("movie_table.id"), nullable = False)

    movie = db.relationship("Movie", backref = "cast_list", lazy = "subquery")
    actor = db.relationship("Cast", backref= "cast_list", lazy = "subquery")

    def __init__(self, cast_id, movie_id):
        self.cast_id = cast_id
        self.movie_id = movie_id

    def __repr__(self):
        return f'< Cast/Film_Index id={self.id} >'

class Cast(db.Model):
    
    __tablename__ = "cast_table"
    
    id = db.Column(db.Integer, autoincrement = True, primary_key = True)
    first_name = db.Column(db.String(255), nullable = False)
    last_name = db.Column(db.String(255), nullable = False)
    dob = db.Column(db.Date, nullable = False)
    bio = db.Column(db.String(500), nullable = False)

    # cast_list = a list of the cast index objects



    def __init__(self, first_name, last_name, dob, bio):
        self.first_name = first_name
        self.last_name = last_name
        self.dob = dob
        self.bio = bio

    def __repr__(self):
        return f'< Cast id={self.id}, first_name={self.first_name}, last_name={self.last_name} >'


def connect_to_db(flask_app, echo=True):                     # echo = True <> enables console logging of all psql submissions
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = os.environ["POSTGRES_URI"]
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = flask_app
    db.init_app(flask_app)

    print("Crank it up to 5432!")




if __name__ == "__main__":
    from server import app

    # Call connect_to_db(app, echo=False) if your program output gets
    # too annoying; this will tell SQLAlchemy not to print out every
    # query it executes.

    connect_to_db(app)
