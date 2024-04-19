from flask import Flask, render_template, flash, url_for, redirect
from pdb import set_trace
from forms import TeamForm, ProjectForm
from key import app_key
from model import User, Team, Project, connect_to_db, get_teams, db



app = Flask(__name__)

app.secret_key = app_key    



@app.route("/")
def homepage():
    team_form = TeamForm()
    project_form = ProjectForm()
    # set_trace()
    project_form.update_teams(get_teams())
                                        
    return render_template("home.html", team_form = team_form, project_form = project_form)


@app.route("/add_team", methods=["POST"])
def add_team():
    team_form = TeamForm()

    if team_form.validate_on_submit():
        team_name = team_form.team_name.data
        new_team = Team(team_name, 1)
        db.session.add(new_team)
        db.session.commit()
        flash(f"{team_form.team_name.data} team created!")
    else:
        flash("Form failed to validate on submit")
    return redirect(url_for("homepage"))


@app.route("/add_project", methods=["POST"])
def add_project():
    project_form = ProjectForm()
    project_form.update_teams(get_teams())



    if project_form.validate_on_submit():
        project_name = project_form.project_name.data
        description = project_form.description.data
        completed = project_form.completed.data
        team_owner = project_form.team_selection.data

        new_project = Project(project_name, description, completed, team_owner)
        db.session.add(new_project)
        db.session.commit()
        flash(f"{project_form.project_name.data} Project Created!")
    else:
        flash("Form failed to validate on submit")
    return redirect(url_for("homepage"))






if __name__ == "__main__":
    app.debug = "development"
    connect_to_db(app)                                           
    app.run(debug=True, port = 4040, host = "localhost")