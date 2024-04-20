import os
from flask_sqlalchemy import SQLAlchemy
from pdb import set_trace

db = SQLAlchemy()




class User(db.Model):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    username = db.Column(db.String(255), unique = True, nullable = False)
    password = db.Column(db.String(255), nullable = False)

    teams = db.relationship("Team", backref = "User", lazy = True)

    def __init__(self, username, password):
        self.username = username,
        self.password = password

class Team(db.Model):

    __tablename__ = "teams"

    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    team_name = db.Column(db.String(255), unique = True, nullable = False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable = False)

    user = db.relationship("User", backref = "Team", lazy = True)

    def __init__(self, team_name, user_id):
        self.team_name = team_name
        self.user_id = user_id

class Project(db.Model):

    __tablename__ = "projects"
    
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    project_name = db.Column(db.String(255), nullable = False)
    description = db.Column(db.String(255), nullable = True)
    completed = db.Column(db.Boolean, default = False)
    team_id = db.Column(db.Integer, db.ForeignKey("teams.id"), nullable = False)

    team = db.relationship("Team", backref = "Project", lazy = True)

    def __init__(self, project_name, description, completed, team_id):
        self.project_name = project_name
        self.description = description
        self.completed = completed
        self.team_id = team_id


def get_teams():
    all_teams = Team.query.all()
    return all_teams

def connect_to_db(app):
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ["POSTGRES_URI"]
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)

if __name__ == "__main__":
    from flask import Flask
    app = Flask(__name__)
    connect_to_db(app)
    print("We're connected to db ...")