from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()



class User(db.Model):

    __tablename__ = "user_table"

    id = db.Column(db.Integer, autoincrement = True, primary_key = True)
    first_name = db.Column(db.String(255), nullable = False)
    last_name = db.Column(db.String(255), nullable = True)
    email = db.Column(db.String(255), nullable = False, unique = True)
    password = db.Column(db.String(255), nullable = False)

    def __init__(self, first_name, last_name, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password

class Movie(db.Model):
    
    __tablename__ = "movie_table"

    id = db.Column(db.Integer, autoincrement = True, primary_key = True)
    title = db.Column(db.String(255), nullable = False, unique = True)
    description = db.Column(db.String(1000), nullable = False)
    genre = db.Column(db.String(255), nullable = False)
    release_date = db.Column(db.DateTime)
    img_url = db.Column(db.String(500), nullable = False)

    def __init__(self, title, description, genre, release_date, img_url):
        self.title = title
        self.description = description
        self.genre = genre
        self.release_date = release_date
        self.img_url = img_url

class Rating(db.Model):

    __tablename__ = "rating_table"

    id = db.Column(db.Integer, autoincrement = True, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey("user_table.id"), nullable = False)
    movie_id = db.Column(db.Integer, db.ForeignKey("movie_table.id"), nullable = False)
    rating = db.Column(db.Integer, nullable = False)
    description = db.Column(db.String(255), nullable = True)

    def __init__(self, user_id, movie_id, rating, description):
        self.user_id = user_id
        self.movie_id = movie_id
        self.rating = rating
        self.description = description

class Cast_Film_Index(db.Model):

    __tablename__ = "index_table"

    id = db.Column(db.Integer, autoincrement = True, primary_key = True)
    cast_id = db.Column(db.Integer, db.ForeignKey("cast_table.id"), nullable = False)
    movie_id = db.Column(db.Integer, db.ForeignKey("movie_table.id"), nullable = False)

    def __init__(self, cast_id, movie_id):
        self.cast_id = cast_id
        self.movie_id = movie_id

class Cast(db.Model):
    
    __tablename__ = "cast_table"
    
    id = db.Column(db.Integer, autoincrement = True, primary_key = True)
    first_name = db.Column(db.String(255), nullable = False)
    last_name = db.Column(db.String(255), nullable = False)
    dob = db.Column(db.DateTime, nullable = False)
    bio = db.Column(db.String(500), nullable = False)

    def __init__(self, first_name, last_name, dob, bio):
        self.first_name = first_name
        self.last_name = last_name
        self.dob = dob
        self.bio = bio








def connect_to_db(flask_app, db_uri="postgresql:///ratings", echo=True):
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)

    print("Connected to the db!")


if __name__ == "__main__":
    from server import app

    # Call connect_to_db(app, echo=False) if your program output gets
    # too annoying; this will tell SQLAlchemy not to print out every
    # query it executes.

    connect_to_db(app)
