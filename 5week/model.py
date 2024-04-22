from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


# Replace this with your code!

class User(db.Model):

    __tablename__ = "user_table"

    id = db.Column(db.Integer, autoincrement = True, primarykey = True)
    first_name = db.Column(db.String(255), nullable = False)
    last_name = db.Column(db.String(255), nullable = True)
    email = db.Column(db.String(255), nullable = False, unique = True)
    password = db.Column(db.String(255), nullable = False)

class Movie(db.Model):
    
    __tablename__ = "movie_table"

    id = db.Column(db.Integer, autoincrement = True, primarykey = True)
    name = db.Column(db.String(255), nullable = False, unique = True)
    description = db.Column(db.String(1000), nullable = False)
    genre = db.Column(db.String(255), nullable = False)
    release_date = db.Column(db.DateTime)
    img_url = db.Column(db.String(500), nullable = False)


class Rating(db.Model):

    __tablename__ = "rating_table"

    id = db.Column(db.Integer, autoincrement = True, primarykey = True)
    user_id = db.Column(db.Integer, db.ForeignKey("user_table.id"))
    movie_id = db.Column(db.Integer, db.ForeignKey("movie_table.id"))
    rating = db.Column(db.Integer, len)
    pass

class Class_Film_Index(db.Model):
    pass

class Cast(db.Model):
    pass


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
